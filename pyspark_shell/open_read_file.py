class OpenReadFile:

    def __init__(self):
        pass

    def open_read_csv(self, sc):
        # abrindo e lendo o arquivo csv
        f = open('arquivo.csv', 'r')

        # lendo o cabecalho do arquivo e separando cada coluna atraves da virgula
        header = f.readline().replace('\n', '').replace('\r', '').split(',')

        # criando um array vazio, para adicionarmos cada registro do csv que sera separado para ficar no formato de
        # tabela
        data_array = []

        # lendo cada linha do arquivo
        for i in f.readlines():
            # adicionando ao array cada linha do arquivo
            data_array.append(i.replace('\n', '').replace('\r', '').split(','))
        f.close()

        # todo arquivo externo quando eh lido, eh tranformado inicialmente em rdd, mas para conseguir trabalhar
        #  melhor com os dados, eh recomendavel converter o arquivo para o formato DataFrame aqui, estamos passando
        #  os registros lidos, junto com o cabecalho, para juntos serem transformados em um DF. O parallelize eh
        #  utilizado para distribuir em datasets e executa-los em paralelo, para uma maior rapidez e eficiencia
        rdd = sc.parallelize(data_array)
        return rdd.toDF(header)

