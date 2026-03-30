# Impotando as bibliotecas necessárias
import pandas as pd

# 1. Tarefa de extração
# Lendo arqquivo .csv com ados de clientes
df = pd.read_csv("clientes.csv")

# Descomente apenas para teste
#print(df.head(n=15))

# 2. Tarefa de transformação
# Passando nomes de clientes e paises para caixa alta
df["nome"] = df["nome"].str.upper();
df["country"] = df["country"].str.upper();
# Descomente apenas para teste
#print(df.head(n=15))

# 3. Tarefa de carga
# Gerando novo arquivo formato .csv e .xls
df.to_csv("transformado.csv")
# Gerando novo arquivo no formato .xlsx
df.to_excel("transformado.xlsx", index=False)

