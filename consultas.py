import pymongo
import os
##Mongo Connection
try:
    mongo_conect =pymongo.MongoClient("mongodb://localhost:27017")
    db = mongo_conect.get_database('pytest')
    collection = db.get_collection('pytestando')
    print("Conectado ao MongoBD")
except:
    print("Problemas ao conectar!")

## Consultas ##
## Menu
def exibir_menu():
    print("Menu:")
    print("1- Adicionar")
    print("2- Exibir existentes")
    print("3- Consultar")
    print("4- Update")
    print("5- Remove")
    print("6- Sair")
    
## 1-Adicionar
def adicionar(produto,data,quant,valor):
    total = quant *valor
    dado = {"Produto":produto,
            "Data":data,
            "Quantidade":quant,
            "Valor":valor,
            "Total":total
        }
    collection.insert_one(dado)
    print("Dado Inserido")
    os.system("Pause")
    os.system("cls")
    return dado

## 2-Mostra Todos Os Resultados
def exibir():
    resultado = collection.find({})   
    for dado in resultado:
        print()
        print(dado)
    os.system("Pause")
    os.system("cls")

## 3-Consultar
def consulta_Produto(nome_prod):
    i= 0
    resultado = collection.find({"Produto":nome_prod})   
    for dado in resultado:
        print()
        i += 1
        print(dado)
    if i == 0:
        print("Produto Não Encontrado")
    os.system("pause")
    
## 4-Update ##
def update(nome_atual,novo_nome):
    prod_nome = collection.find_one({"Produto":nome_atual})
    update_nome ={"$set":{"Produto":novo_nome}}
    update_prod = collection.update_one(prod_nome,update_nome)
    update_prod = collection.find({"Produto":novo_nome})
    for dado in update_prod:
        print()
        print(dado)

## 5-REMOVER ##
def remover(nome_remove):
    remove =collection.delete_one({"Produto":nome_remove})
    if remove.deleted_count > 0:
        print(f"Dado Removido: {nome_remove}")
    else:
        print(f"Dado Não Removido: {nome_remove}")
    return remove

## MAIN ##
while True:
    exibir_menu()
    opcao = int(input("Opção: "))
    os.system("cls")  
     
    if opcao == 1: ## Adicionar ##
        produto = input("Nome Produto: ")
        data = input("Data:")
        valor = float(input("Valor: "))
        quant = int(input("Quantidade:"))
        adicionar(produto,data,valor,quant)
        
    elif opcao == 2:## Exibir todos resultados ##
        exibir()

    elif opcao == 3: ## Consulta ##
        nome_prod = input("Digite o nome do produto a ser consultado: ")
        consulta_Produto(nome_prod)
    
    elif opcao == 4:## UPDATE ##
        nome_atual = input("Nome Atual Do Produto: ")
        novo_nome =input("Novo Nome Produto: ")
        update(nome_atual,novo_nome)
        
    elif opcao ==5: ## REMOVER ##
        nome_remove = input("Produto para Remover: ")
        remover(nome_remove)
        
    elif opcao == 6:## SAIR ##
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida.")
        os.system('pause')

