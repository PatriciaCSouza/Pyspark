# Introdução

Projeto desenvolvido em pyspark e shell, onde a chamada inicial é feita pelo arquivo shell executar.sh, onde é chamado o arquivo principal main.py, 
que aloca os recursos do spark conforme mostrado no call_spark.py, lê o arquivo csv local, através do open_read_file.py e com o arquivo insert_table.py, 
grava o resultado final na tabela sbx_semantix.eng_dados.


## Requerimentos
Python 3.7

## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar o pyspark.

```bash
pip install pyspark
```

## Execução

Usando o terminal linux, executar o arquivo shell

```bash
bash executar.sh
```
