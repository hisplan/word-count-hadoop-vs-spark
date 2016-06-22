 val file = spark.textFile("hdfs://...")
 val counts = file.flatMap(line => line.split(" ")).map(word => (word, 1)).reduceByKey(_ + _)
 counts.saveAsTextFile("hdfs://...")
