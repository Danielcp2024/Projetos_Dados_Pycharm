import pandas as pd
from datetime import datetime


pd.set_option('display.width', None)

df = pd.read_csv('clientes_limpeza.csv')

# Converter a coluna data para datetime
df['data'] = pd.to_datetime(df['data'], errors='coerce')

# Criar coluna idade
hoje = datetime.today()

df['idade'] = (hoje - df['data']).dt.days // 365

print(df.columns)


df = pd.read_csv(r"C:\Users\danie\Downloads\clientes.csv")  # seu arquivo original

# salvar novo arquivo com a coluna criada
df.to_csv('clientes_limpeza.csv', index=False)

print('Arquivo salvo com a coluna idade!')

# Sempre que for trabalhar com texto, faça esse ritual:
df['coluna'] = df['coluna'].fillna('').astype(str)

