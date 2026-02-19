import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] > 100]


print('Filtro básico:\n', df_filtro_basico[['nome', 'idade']])

# Identificar outliers com Z-score
z_scores = stats.zscore(df['idade'].dropna()) #Dropna: Remover valores nulos
outliers_z = df[z_scores >= 3]
print('outliers pelo Z_score:\n', outliers_z)

# Filtrar outliers com Z_score
df_zscore = df[(stats.zscore(df['idade']) < 3)]

# Identificar outliers com IQR
q1 = df['idade'].quantile(0.25)
q3 = df['idade'].quantile(0.75)
iqr = q3 - q1

limite_baixo = q1 - 1.5 * iqr
limite_alto = q3 + 1.5 * iqr

print('Limites IQR:', limite_baixo, limite_alto)

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print('Outliers pelo IQR:\n', outliers_iqr)

# Filtrar outliers com iqr
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

#Evite apply quando possível. Use vetorização:
df['endereco'] = df['endereco'].fillna('').astype(str)

mask = df['endereco'].str.count('\n') < 2

df.loc[mask, 'endereco'] = 'endereco invalido'

# Filtrar endereços inválidos
df['endereco'] = df['endereco'].apply(lambda x: 'endereco invalido' if len(x.split('\n')) < 3 else x)
print('Qtd registros com endereços inválidos:', (df['endereco' ] == 'endereco invalido').sum())

#-Tratar campos de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome invalido' if isinstance(x, str) and len(x) > 50 else x)
print('Qtd registros com nomes grandes:', (df['nome' ] == 'Nome inválido').sum())

print('Dados com Outliers tratados:\n', df)

# Salvar dataframe
df.to_csv('clientes_remove_outliers.csv', index=False)
