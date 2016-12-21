# Pyspark Streaming Pubub
A python module for connecting to Google pubsub as a source for Spark Streaming. 

This python package requires this JAR is available on the CLASSPATH of Spark:
https://github.com/jasonmotylinski/spark-streaming-pubsub

1. Set SPARK_HOME
```
export SPARK_HOME=/opt/spark-2.0.1-bin-hadoop2.7

2. Set PYTHONPATH
```
export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
```