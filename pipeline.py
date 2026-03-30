# Impotando as bibliotecas necessárias
import pandas as pd

## 1. Tarefa de extração
# Lendo arquivo .csv com dados de clientes
try:
    #  Tentando ler o arquivo de origem
    df = pd.read_csv("clientes.csv")
except FileNotFoundError as e:
    # Exibindo  o  erro
    print(f"Não  foi possivel encontrar o arquivo informado",  e)
    raise SystemExit("Encerrando execução devido a erro de arquivo")
finally:
    # Concluindo operação
    print("Finalizando a operação de leitura/extração" )

# Verificando amostra - comente as linhas abaixo se  desejar.
print("**  Amostra dos dados originais. **")
print(df.head(n=10))
print()

## 2. Tarefa de transformação
# 1 - Alterando os nomes  das colunas
df.columns = ["ID", "Cliente", "Telefone", "Pais"]

# 2 - Acrecentando uma coluna "Atualizado", True ou False, sendo que para clientes do  Brasil 
# será True e para clientes  de outros  paises será False
df["Atualizado"] = df["Pais"].apply(lambda x: "True" if x == "Brazil" else "False")

# 3 - Passando nomes de clientes e paises para caixa alta
df["Cliente"] = df["Cliente"].str.upper()
df["Pais"] = df["Pais"].str.upper()

# Verificando amostra - comente as linhas abaixo se  desejar.
print("** Amostra da transformação. ** ")
print(df.head(n=10))
print()

## 3. Tarefa de carga
# Gerando novo arquivo formato .csv e .xls
df.to_csv("transformado.csv")
# Gerando novo arquivo no formato .xlsx
df.to_excel("transformado.xlsx", index=False)

