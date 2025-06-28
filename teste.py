import pandas as pd
import matplotlib.pyplot as plt

# Lê o CSV
df = pd.read_csv('dados.csv')

# Gráfico de barras de VENDAS por mês
plt.figure(figsize=(10, 6))
plt.bar(df['mes'], df['vendas'], color='cornflowerblue')
plt.title('Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
