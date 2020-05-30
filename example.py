indicate_mismatched = df_parsed.withColumn(
	"sn_mismatch", when(col("extracted_udis.udi_sn") != col("extracted_udis.sudi_sn"), 1).otherwise(0))


grouped_by_udi_pid_and_mismatch = indicate_mismatched.groupby(
	col("extracted_udis.udi_pid"), col("sn_mismatch")).agg(
	collect_set(
		col("extracted_udis.sudi_sn")).alias(
		"uniq_sudi_sn")).withColumn("num_distinct_sudi_sn", size(col("uniq_sudi_sn")))

matched_sn = grouped_by_udi_pid_and_mismatch.filter(
	col("sn_mismatch") == 0).drop("sn_mismatch").withColumnRenamed(
	"num_distinct_sudi_sn", "distinct_matched_sudi_sn").withColumnRenamed(
	"uniq_sudi_sn", "uniq_matched_sudi_sn")

mismatched_sn = grouped_by_udi_pid_and_mismatch.filter(
	col("sn_mismatch") == 1).drop("sn_mismatch").withColumnRenamed(
	"num_distinct_sudi_sn", "distinct_mismatched_sudi_sn").withColumnRenamed(
	"uniq_sudi_sn", "uniq_mismatched_sudi_sn")

grouped_by_udi_pid = matched_sn.join(mismatched_sn, "udi_pid", "outer").fillna(0).cache()


grouped_by_udi_pid.drop(
	"uniq_matched_sudi_sn", 
	"uniq_mismatched_sudi_sn").withColumn(
	"pct_mismatched", col("distinct_mismatched_sudi_sn") / (
		col("distinct_matched_sudi_sn") + col(
			"distinct_mismatched_sudi_sn"))).filter(col(
	"pct_mismatched") != 0.0).sort("pct_mismatched", ascending=True).show(50, False, False)

# grouped_by_udi_pid.drop("uniq_matched_sudi_sn", "uniq_mismatched_sudi_sn").show(10, False, False)