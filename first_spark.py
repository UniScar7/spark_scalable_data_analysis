from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FirstSparkRun") \
    .master("local[*]") \
    .getOrCreate()

data = [("Atharv", 21), ("Spark", 10)]
df = spark.createDataFrame(data, ["name", "value"])

df.show()

spark.stop()