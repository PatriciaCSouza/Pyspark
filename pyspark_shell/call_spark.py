# Bibliotecas PYSPARK
from pyspark import SparkConf, SparkContext


class CallSpark:

    def __init__(self):
        pass

    def get_context(self):
        # Iniciando o contexto spark
        conf = SparkConf().setAppName('NBA - Mensuracao') \
            .set('spark.executor.cores', 2) \
            .set('spark.executor.memory', '2g') \
            .set('spark.executor.instances', 25) \
            .set('spark.shuffle.service.enabled', 'true') \
            .set('spark.shuffle.service.port', 7337) \
            .set("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
            .set("spark.sql.hive.convertMetastoreOrc", "false") \
            .set("hive.exec.dynamic.partition", "true") \
            .set("hive.exec.dynamic.partition.mode", "nonstrict")

        sc = SparkContext(conf=conf)

        return sc
