import os
import pyspark
from pyspark.sql import *
from pyspark.sql.types import *
from pyspark import SparkContext, SparkConf

# create a Spark session
conf = SparkConf()
conf.set("spark.ui.port", "4050")
conf.set("spark.executor.memory", "12g")
conf.set("spark.driver.memory", "4g") 
conf.set("spark.jars", "/home/ugrads/k/kingrc15/postgresql-42.3.3.jar")

# create a Spark context
sc = SparkContext(conf=conf)


spark = SparkSession.builder.getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/postgres") \
    .option("dbtable", "omop.death") \
    .option("user", "postgres") \
    .option("password", "postgres") \
    .option("driver", "org.postgresql.Driver") \
    .load()

df.printSchema()