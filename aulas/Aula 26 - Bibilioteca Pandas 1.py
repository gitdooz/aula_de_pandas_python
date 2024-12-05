# Bibilioteca pandas - Parte 1
# Series

# Site oficial: https://pandas.pydata.org/

import pandas as pd

# Criação de um DataFrame a partir de um Dictionary

lista_pessoas = {"Nome":["Alessandro","Márcia","Amanda","André"],
                 "Idade":[51,50,40,50],
                 "Gênero":['M','F','F','M']}

df = pd.DataFrame(lista_pessoas) #Tabela bidimensional (linhas e colunas)
print(df)
print()
# Series é uma coluna e seu índice é gerado automaticamente
print(df["Nome"])
print()

# Criação de uma Series
Valores = [1,2,3,4]
ValoresSeries = pd.Series(Valores,index=['a','b','c','d'])
print(ValoresSeries)
print()

# Acessar o primeiro elemento de uma series
print('Primeiro elemento: ', ValoresSeries[0])
print('índice C...:', ValoresSeries['c'])
print()

# Nova Serie para ser adicionada ao DataFrame

DiaAniversario = pd.Series([11,7,7,12])
print('DiaAniversario\n', DiaAniversario)

#Adicionar ao DataFrame
df['DiaAniversário'] = DiaAniversario
print(df)
print()

# Métodos de uma Series / DataFrame

print('Maior idade:', df['Idade'].max())
print('Menor idade:', df['Idade'].min())
print('Quantos nomes:', df['Nome'].count())
print('Média de idade:', df['Idade'].mean())
print('Somatória das idades:', df['Idade'].sum(),'anos')
print('Classificação:\n', df['Idade'].sort_values())
print()

# Estatística completa

print(df.describe())
print()