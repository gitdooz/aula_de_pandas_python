from faker import Faker
import pandas as pd

fake = Faker(locale='pt-BR')
fakeVI = Faker(locale=['pt-BR','es-ES','en-US'])
print()


print(fake.text())
print(fake.address())
print(fake.ascii_email())
print(fake.ascii_free_email())
print(fake.mac_address())

for _ in range(10):
    print(fake.name())
print()
for _ in range(10):
    print(fake.name_female())
print()

print(fake.random_letter())
print(fake.random_letters(8))
print(fake.random_digit_not_null())
print(fake.year())
print(fake.date())
print(fake.date_time())
print(fake.time())
print(fake.url())
print(fake.image_url())
print(fake.cpf())
print(fake.rg())
print(fake.cellphone_number())
print(fake.bairro())
print(fake.city())
print()

nome = []
empresa = []
cidade = []
pais = []
funcao = []
endereco = []
email = []
data_nascimento = []
cpf = []
idade = []

for i in range(0,2000):
    nome.append(fake.name())
    empresa.append(fake.company())
    cidade.append(fake.city())
    pais.append(fake.country())
    funcao.append(fake.job())
    endereco.append(fake.street_address())
    email.append(fake.email())
    data_nascimento.append(fake.date_of_birth())
    cpf.append(fake.cpf())
    idade.append(fake.random_number(digits=2))

# Gerar um DataFrame a partir de várias listas
    
df = pd.DataFrame({
    'NOME': nome,
    'EMPRESA': empresa,
    'CIDADE':cidade,
    'PAIS': pais,
    'CARGO': funcao,
    'ENDERECO': endereco,
    'EMAIL': email,
    'DATA_NASCIMENTO': data_nascimento,
    'CPF':cpf,
    'IDADE': idade
})

df.to_csv('./DADOS_FAKE.CSV',index=False)