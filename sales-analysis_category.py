# Análise de Vendas por Categoria

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Dados simulados de vendas

data = {
    "Sale_ID": range(1, 21),
    "Category": [
        "Eletrônicos", "Roupas", "Eletrônicos", "Alimentos", "Alimentos", 
        "Roupas", "Móveis", "Eletrônicos", "Móveis", "Alimentos",
        "Roupas", "Móveis", "Eletrônicos", "Alimentos", "Móveis",
        "Roupas", "Eletrônicos", "Alimentos", "Móveis", "Roupas"
    ],
    "Date": [
        "2025-01-01", "2025-01-01", "2025-01-02", "2025-01-02", "2025-01-03", 
        "2025-01-03", "2025-01-04", "2025-01-04", "2025-01-05", "2025-01-05", 
        "2025-01-06", "2025-01-06", "2025-01-07", "2025-01-07", "2025-01-08", 
        "2025-01-08", "2025-01-09", "2025-01-09", "2025-01-10", "2025-01-10" 
    ],
    "Quantify": [5, 10, 7, 15, 20, 8, 6, 9, 12, 25, 10, 5, 8, 18, 7, 11, 9, 20, 4, 14],
    "Unit_Price": [500, 50, 400, 10, 8, 60, 200, 450, 250, 12, 55, 220, 480, 15, 230, 65, 490, 10, 210, 58],
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Convertendo a coluna Date para o formato datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculando a receita total por linha
df["Total_Revenue"] = df["Quantify"] * df["Unit_Price"]

# Receita total por categoria
category_revenue = df.groupby("Category")["Total_Revenue"].sum().sort_values(ascending=False)
print("Receita Total por Categoria:")
print(category_revenue)

# Quantidade média vendida por categoria
category_avg_quantify = df.groupby("Category")["Quantify"].mean().sort_values(ascending=False)
print("\n Quantidade Média Vendida por Categoria:")
print(category_avg_quantify)

# Gráfico de barras - Receita por Categoria
plt.figure(figsize=(10, 6))
category_revenue.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Receita Total por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Receita Total (R$)")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()

# Gráfico de barras - Quantidade Média Vendida por Categoria
plt.figure(figsize=(10, 6))
category_avg_quantify.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Quantidade Média Vendida por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Quantidade Média")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()

# Gráfico de pizza - Participação percentual da receita por categoria
plt.figure(figsize=(8, 8))
category_revenue.plot(kind="pie", autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
plt.title("Participação Percentual na Receita por Categoria")
plt.ylabel("")  # Remove o rótulo padrão do eixo Y
plt.show()