#!/bin/bash -x
export HADOOP_CLIENT_OPTS="-Djline.terminal=jline.UnsupportedTerminal"
export PYSPARK_PYTHON=/usr/bin/python

MASTER=yarn-client
DRIVER_MEMORY=2G
EXECUTOR_MEMORY=2G
EXECUTOR_CORES=2
QUEUE=next

spark-submit --master ${MASTER} \
  --queue ${QUEUE} \
  --conf spark.ui.port=7337 \
  --driver-memory ${DRIVER_MEMORY} \
  --executor-memory ${EXECUTOR_MEMORY} \
  --executor-cores ${EXECUTOR_CORES} \
  main.py

  ret1=$?
  if [ ${ret1} -eq 0 ]
  then
      echo "Fim de processamento do $1 returncode=" ${ret1}
      ret1=$?
  else
      echo "Erro no Processamento do $1. Passando para o proximo..."
  fi

