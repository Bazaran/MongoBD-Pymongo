import pandas as pd
import pymongo
## Conexão MongoBD
mongo_conect =pymongo.MongoClient("mongodb://localhost:27017")
db = mongo_conect.get_database('pytest')
collection = db.get_collection('pytestando')

## Extração dos dados CSV
df =pd.read_csv("dados_produtos.csv")
print(f"\n{df}")
vendas_total = df.groupby("Produto")["Valor"].sum() #Agrupa o Valor dos produtos e soma o total.
df['Total'] = df['Quantidade'] * df['Valor'] #Soma a QTD * Valor
print(f"\nValor Total Vendido:\n{vendas_total}")
vendas_total.to_csv("Total_Vendas.csv") #Criação de Um arquivo CSV com os Totais Vendidos.

## INSERÇÃO NO MONGODB ##
dados_formatados = df.to_dict(orient='records') # Formatando para entrar em Chave/valor
collection.insert_many(dados_formatados)

