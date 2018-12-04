from pyspark import SparkConf,SparkContext

conf = SparkConf().setAppName("Spark Demo").setMaster("local")
sc = SparkContext(conf=conf)

inputPath = "/Users/mishael/PycharmProjects/Python Tutorials/wordcount.txt"
outputPath = "/Users/mishael/PycharmProjects/Python Tutorials/wordcount1"

"""
Instead of using a named function, we will use an anonymous function (with the lambda keyword in Python). 
This line of code will map the lambda to each element of words. Therefore, each x is a word, and the word will 
be transformed into a tuple (word, 1) by the anonymous closure
"""
#Make sure outputPath does not exist
for i in sc.textFile(inputPath).\
map(lambda w: (w, 1)).\
reduceByKey(lambda t, e: t + e).\
take(100):print(i)

#Saving to file
"""
the .textfile() method loads the input file into a Resilient Distributed Dataset (RDD)
the .map() method map each word to a key value pair, where the key is the word and the value is a 1, and then use a reducer to sum the 1s for each key.
the .reduceByKey() method gets our word counts 
"""

sc.textFile(inputPath).\
map(lambda w: (w, 1)).\
reduceByKey(lambda t, e: t + e).\
saveAsTextFile(outputPath)
