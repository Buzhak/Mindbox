import pyspark
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('spark_df').getOrCreate()

product_data = [
    ["1", "велосипед", "1"],
    ["2", "велосипед", "2"],
    ["3", "машина", "1"],
    ["4", "самолёт", "1"],
    ["5", "автобус", "1"]
]

columns = ['ID', 'title', 'category']
product_df = spark.createDataFrame(product_data, columns)

category_data = [
    ["1", "Транспорт"],
    ["2", "Спорт инвентать"],
]

columns = ['ID', 'title']
category_df = spark.createDataFrame(category_data, columns)

product_df.join(
    category_df,
    product_df.category == category_df.ID,
    "left"
).show()
