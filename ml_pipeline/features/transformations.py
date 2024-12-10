from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def build_failure_features(df: DataFrame) -> DataFrame:
    w = Window.partitionBy("device_id", "component").orderBy("event_ts").rowsBetween(-24, 0)
    return (
        df.withColumn("temp_rolling_avg", F.avg("temperature_c").over(w))
        .withColumn("vibration_rolling_std", F.stddev("vibration_mm_s").over(w))
        .withColumn("pressure_delta", F.col("pressure_kpa") - F.lag("pressure_kpa", 1).over(w))
        .fillna({"vibration_rolling_std": 0.0, "pressure_delta": 0.0})
    )
