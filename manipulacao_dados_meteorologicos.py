import pandas as pd
import numpy as np

# Criando o DataFrame com os dados fornecidos
data = {
    'Data': ['15/01/2025', '15/01/2025', '15/01/2025', '15/01/2025', '15/01/2025'],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Porto Alegre', 'Salvador'],
    'Temperatura Máxima (°C)': [30.5, 35.0, 24.0, 28.0, 31.0],
    'Temperatura Mínima (°C)': [22.0, 25.0, 18.0, 20.0, 24.5],
    'Precipitação (mm)': [12.0, np.nan, 8.0, 15.0, np.nan],
    'Umidade Relativa (%)': [78, 70, np.nan, 82, 80]
}

df = pd.DataFrame(data)

# Substituir valores ausentes na coluna Precipitação pela média da Precipitação
media_precipitacao = df['Precipitação (mm)'].mean()
df['Precipitação (mm)'].fillna(media_precipitacao, inplace=True)

# Substituir valores ausentes na coluna Umidade Relativa pela mediana da Umidade Relativa
mediana_umidade = df['Umidade Relativa (%)'].median()
df['Umidade Relativa (%)'].fillna(mediana_umidade, inplace=True)

# Adicionar a coluna 'Amplitude Térmica' (Temperatura Máxima - Temperatura Mínima)
df['Amplitude Térmica'] = df['Temperatura Máxima (°C)'] - df['Temperatura Mínima (°C)']

# Criar um novo DataFrame com cidades que têm Temperatura Máxima acima de 30°C
df_filtrado = df[df['Temperatura Máxima (°C)'] > 30]

# Reordenar o DataFrame conforme solicitado
df_filtrado = df_filtrado[['Data', 'Cidade', 'Temperatura Máxima (°C)', 'Temperatura Mínima (°C)', 'Amplitude Térmica', 'Precipitação (mm)', 'Umidade Relativa (%)']]

print(df_filtrado)

