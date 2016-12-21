from pyspark.storagelevel import StorageLevel
from pyspark.streaming import DStream
from pyspark.serializers import NoOpSerializer


def createStream(ssc, projectName, topic, subscription,
                 checkpointInterval,
                 storageLevel=StorageLevel.MEMORY_AND_DISK_2):
    jlevel = ssc._sc._getJavaStorageLevel(storageLevel)
    jduration = ssc._jduration(checkpointInterval)
    try:
        helper = ssc._jvm.com.brokenindustries.spark.streaming.pubsub.PubsubPythonHelper()
    except TypeError as e:
        if str(e) == "'JavaPackage' object is not callable":
            _printErrorMsg(ssc.sparkContext)
        raise

    jstream = helper.createStream(ssc._jssc, projectName, topic, subscription, jduration, jlevel)
    stream = DStream(jstream, ssc, NoOpSerializer())
    return stream.map(lambda v: v.decode("utf-8"))


def _printErrorMsg(sc):
    print("""
________________________________________________________________________________________________
Spark Streaming's Pubsub libraries not found in class path.
________________________________________________________________________________________________
""" % (sc.version, sc.version))