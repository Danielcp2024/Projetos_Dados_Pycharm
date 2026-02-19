import pandas as pd

arquivo = r"C:\Users\danie\Downloads\clientes.csv"

df = pd.read_csv(arquivo)

print(df)

# Verificar os primeiros registros
print(df.head().to_string())  # Início dos dados

print(df.tail().to_string())  # O final dos dados

# Verificar quantidades de linhas e registros
print('Qtd: ', df.shape)

# Verificar tipos de dados
print('Tipagem:\n ', df.dtypes)

# Checar valores nulos
print('Valores nulos:\n ', df.isnull().sum())
