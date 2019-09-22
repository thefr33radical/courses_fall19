from pyspark import SparkContext 

sc= SparkContext.getOrCreate()
sc.setLogLevel("ERROR")

line= sc.parallelize([" I I am I am here stdyuing in the morning hai"])

words=line.flatMap(lambda x:x.split(" "))
print(words)
wcount=words.map(lambda w:(w,1))
print(wcount)

res=wcount.reduceByKey(lambda a,b:a+b)
for r in res.collect():
  print(r)
