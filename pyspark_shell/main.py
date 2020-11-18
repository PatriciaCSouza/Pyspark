from pyspark.sql import HiveContext

from call_spark import *
from open_read_file import *
from insert_table import *


if __name__ == '__main__':
    sc = CallSpark().get_context()
    hc = HiveContext(sc)
    df = OpenReadFile().open_read_csv(sc)
    InsertTable().insert_result(df, hc)

