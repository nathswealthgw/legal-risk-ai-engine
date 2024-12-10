from pyspark.sql import SparkSession


def build_spark(app_name: str = "legal-risk-feature-pipeline") -> SparkSession:
    return (
        SparkSession.builder.appName(app_name)
        .config("spark.sql.shuffle.partitions", "400")
        .config("spark.sql.adaptive.enabled", "true")
        .getOrCreate()
    )
