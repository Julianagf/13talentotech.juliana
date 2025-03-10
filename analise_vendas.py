import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Dados fictícios de vendas
dados_vendas = {
    'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'],
    'Vendas': [200, 220, 250, 275, 300, 350, 400],
    'Numero de Clientes': [50, 55, 60, 65, 70, 80, 90],
    'Lucro': [1000, 1100, 1200, 1300, 1400, 1600, 1800]
}

df_vendas = pd.DataFrame(dados_vendas)

# 1. Gráfico de Barras: Total de vendas por dia
plt.figure(figsize=(8,6))
sns.barplot(x='Dia', y='Vendas', data=df_vendas)
plt.title('Total de Vendas por Dia')
plt.xlabel('Dia da Semana')
plt.ylabel('Vendas')
plt.show()

# 2. Gráfico de Dispersão: Número de clientes vs Vendas
plt.figure(figsize=(8,6))
sns.scatterplot(x='Numero de Clientes', y='Vendas', data=df_vendas, color='r', s=100)
plt.title('Número de Clientes vs Vendas')
plt.xlabel('Número de Clientes')
plt.ylabel('Vendas')
plt.show()

# 3. Heatmap: Correlação entre Vendas, Número de Clientes e Lucro
correlacao = df_vendas[['Vendas', 'Numero de Clientes', 'Lucro']].corr()
plt.figure(figsize=(6,4))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlação entre Vendas, Número de Clientes e Lucro')
plt.show()
