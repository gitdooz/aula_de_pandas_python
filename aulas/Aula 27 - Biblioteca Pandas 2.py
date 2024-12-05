import pandas as pd

# Leitura e conversão de um arquvio CSV
df = pd.read_csv('DADOS_FAKE.CSV', delimiter=',')
print(df)
print()

# Primeiros registros
print(df.head())
print()

# Últimos registros
print(df.tail())
print()

# Informações sobre as colunas
print(df.info())
print()

# Tipos de dados de um DataFrame
print(df.dtypes)
print()

# Troca do índice para CPF
NovoIndice = df['CPF']
df.index = NovoIndice
print(df)
print()

# Salvar o DataFrame em uma pasta de trabalho
# df.to_excel('DADOS_FAKE.xlsx', index=False)
# print('Arquivo gerado com sucesso!')
# print()
# LEMBRETE: Caso o arquivo xlsx não seja gerado, 
# abrir o terminal e digitar "pip install openpyxl"

# Salvar o DataFrame como Parquet
# LEMBRETE: Abrir o Power BI Desktop
df.to_parquet('DADOS_FAKE.pqt', index=False)
print('Arquivo gerado com sucesso!')
print()

