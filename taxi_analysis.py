from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("NYC Taxi Analysis") \
    .getOrCreate()

# Load PARQUET dataset
df = spark.read.parquet(
    "C:\\spark_project\\data\\yellow_tripdata.parquet"
)

print("Initial partitions:", df.rdd.getNumPartitions())
df = df.repartition(2)
print("Partitions after repartition:", df.rdd.getNumPartitions())
print("Schema:")
df.printSchema()

print("Row count:")
print(df.count())

print("Sample rows:")
df.show(5)
print("Trips per passenger count:")
df.groupBy("passenger_count").count().orderBy("passenger_count").show()

spark.stop()

