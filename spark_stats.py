from pyspark.sql import SparkSession, functions as F

spark = (
    SparkSession.builder
    .appName("BaseballStats")
    .config("spark.driver.extraJavaOptions", "--enable-native-access=ALL-UNNAMED")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

data = spark.read.csv("appearances.csv", header=True, sep=';')

count_towards_atbats = ["1b", "2b", "3b", "HR", "K", "ROE", "RFC", "GO", "FO"]
count_as_hits = ["1b", "2b", "3b", "HR"]

stats = (
    data.withColumn("isAB", F.col("Appearance").isin(count_towards_atbats))
        .withColumn("isHit", F.col("Appearance").isin(count_as_hits))
        .groupBy("Name")
        .agg(
            F.sum(F.col("isAB").cast("int")).alias("AB"),
            F.sum(F.col("isHit").cast("int")).alias("H"),
            F.sum(F.col("RBI").cast("int")).alias("RBI"),
            F.sum(F.col("Run").cast("int")).alias("R"),
        )
        .withColumn("AVG", (F.col("H") / F.col("AB")))
)
stats.show()
