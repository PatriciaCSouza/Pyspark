class InsertTable:

    def __init__(self):
        pass

    def insert_result(self, df, hc):
        # Funcoes usadas para permitir a alocacao dinamica das particoes
        hc.setConf("hive.exec.dynamic.partition", "true")
        hc.setConf("hive.exec.dynamic.partition.mode", "nonstrict")

        # Inserindo resultados na tabela
        df.write.mode('append').insertInto('sbx_semantix.eng_atuais')

        print('inserido com sucesso!')
