import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
vendas_df = pd.read_csv('data/vendas.csv')

# Exibir as primeiras linhas do dataframe
print(vendas_df.head())

# Análise simples: Total de vendas por produto
vendas_por_produto = vendas_df.groupby('Produto')['Receita'].sum().sort_values(ascending=False)
print("\nTotal de vendas por produto:")
print(vendas_por_produto)

# Gráfico de barras para total de vendas por produto
plt.figure(figsize=(8, 6))
vendas_por_produto.plot(kind='bar', color='skyblue')
plt.title('Total de Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Receita')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Análise por região: Total de vendas por região
vendas_por_regiao = vendas_df.groupby('Região')['Receita'].sum().sort_values(ascending=False)
print("\nTotal de vendas por região:")
print(vendas_por_regiao)

# Gráfico de barras para total de vendas por região
plt.figure(figsize=(8, 6))
vendas_por_regiao.plot(kind='bar', color='lightgreen')
plt.title('Total de Vendas por Região')
plt.xlabel('Região')
plt.ylabel('Receita')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Análise por data: Total de vendas ao longo dos dias
vendas_por_data = vendas_df.groupby('Data')['Receita'].sum()
print("\nTotal de vendas por data:")
print(vendas_por_data)

# Gráfico de linha para total de vendas por data
plt.figure(figsize=(8, 6))
vendas_por_data.plot(kind='line', color='coral', marker='o')
plt.title('Total de Vendas por Data')
plt.xlabel('Data')
plt.ylabel('Receita')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Média de vendas por produto
media_vendas_produto = vendas_df.groupby('Produto')['Receita'].mean()
print("\nMédia de vendas por produto:")
print(media_vendas_produto)
