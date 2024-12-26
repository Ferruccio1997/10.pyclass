import pandas as pd


class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filtrar_por(self, colunas: list, atributos: list):
        if len(colunas) != len(atributos):
            raise ValueError('Nao tem o mesmo numero de colunas e atributos')
        
        if len(colunas) == 0:
            return self.df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas) == 1:
            return df_filtrado
        else:
            return self.filtrar_por(colunas[1:], atributos[1:])
    

arquivo_csv = './exemplo.csv'
filtro: list[str] = ['estado', 'id']
limite: list = ['SP', 7]

arquivo_csv = CsvProcessor(arquivo_csv)
arquivo_csv.carregar_csv()
print(arquivo_csv.filtrar_por(filtro, limite))
