from setuptools import setup

setup(
 name='pubsub-pyspark-streaming',
 version='0.0.1',
 description='Pubsub interface for Spark Streaming',
 packages=['pubsub.pyspark.streaming'],
 install_requires=['google-cloud-pubsub', 'py4j']
)

