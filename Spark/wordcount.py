from pyspark import SparkConf,SparkContext

conf = SparkConf().setAppName("Spark Demo").setMaster("local")
sc = SparkContext(conf=conf)

inputPath = "/Users/mishael/PycharmProjects/Python Tutorials/wordcount.txt"
outputPath = "/Users/mishael/PycharmProjects/Python Tutorials/wordcount1"

#Make sure outputPath does not exist

for i in sc.textFile(inputPath).\
flatMap(lambda l: l.split(" ")).\
map(lambda w: (w, 1)).\
reduceByKey(lambda t, e: t + e).\
take(100):
print(i)

#Saving to file

sc.textFile(inputPath).\
flatMap(lambda l: l.split(" ")).\
map(lambda w: (w, 1)).\
reduceByKey(lambda t, e: t + e).\
saveAsTextFile(outputPath)
