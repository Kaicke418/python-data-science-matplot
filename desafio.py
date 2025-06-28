import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk

dados = pd.read_csv('dados.csv')
df = pd.DataFrame(dados)


def grafico_barras():
    plt.bar(df['mes'], df['vendas'], color='cornflowerblue')
    plt.xlabel('Mês')
    plt.ylabel('Vendas')
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
    

def grafico_pizza():
    plt.pie(df['vendas'], labels=df['mes'], autopct= '%.1f%%')
    plt.show()

def grafico_linha():
    plt.plot(df['mes'], df['vendas'], color='purple')
    plt.show()

def grafico_scatter():
    plt.scatter(df['mes'], df['vendas'], color='blue')
    plt.show()

root = tk.Tk()
root.geometry('300x300')
root.title('gerenciamento de vendas')

btn_barra = tk.Button(root, text='gráfico de barras', command=grafico_barras)
btn_barra.grid(row=0, column=5, padx=10, pady=10)
btn_pizza = tk.Button(root, text='grafico de pizza', command=grafico_pizza)
btn_pizza.grid(row=1, column=5, padx=10, pady=10)
btn_linha = tk.Button(root, text='grafico de linha', command=grafico_linha)
btn_linha.grid(row=2, column=5, padx=10, pady=10)
btn_scatter = tk.Button(root, text='grafico de dispersão', command=grafico_scatter)
btn_scatter.grid(row=3, column=5, padx=10, pady=10)

root.mainloop()


# Atividade Prática: Visualização de Dados com Matplotlib

# Objetivo

# Criar quatro gráficos diferentes para analisar dados de vendas de uma loja.

# Dados -  crie um arquivo csv

# | Mês | Vendas | Lucro |
# | --- | --- | --- |
# | Jan | 100 | 500 |
# | Fev | 120 | 600 |
# | Mar | 150 | 700 |
# | Abr | 180 | 800 |
# | Mai | 200 | 900 |

# Tarefas

# 1. Gráfico de Pizza: Mostre a distribuição de vendas por mês.
# 2. Gráfico de Dispersão: Relacione vendas e lucro.
# 3. Gráfico de Barras: Compare vendas por mês.
# 4. Gráfico de Linha: Mostre a evolução do lucro ao longo dos meses.






# Dados

# com pandas

# Seu código aqui


# Dicas

# 1. Use plt.pie() para gráfico de pizza.
# 2. Use plt.scatter() para gráfico de dispersão.
# 3. Use plt.bar() para gráfico de barras.
# 4. Use plt.plot() para gráfico de linha.
# 5. Adicione títulos, legendas e labels aos eixos.


# Entrega

# 1. Código Python completo.
# 2. Imagens dos quatro gráficos.
# 3. Breve descrição da análise realizada.


# Referências

# - Documentação oficial Matplotlib
# https://matplotlib.org/stable/


# ------------------------------------------------//------------------------



