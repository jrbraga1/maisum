
def criar_no(valor, nome, renda):
    return{ "codigo": valor,"nome":nome, "renda":renda, "prox":None}

def inserir_lista_circular(lista, valor, nome, renda):
    novo_no = criar_no(valor, nome, renda)
    if not lista:# se a lista estiver vazia
        novo_no["prox"] = novo_no
        return novo_no
    atual = lista
    while atual["prox"] != lista: 
        atual = atual["prox"]
    atual["prox"] = novo_no
    novo_no["prox"] = lista
    return lista

def imprimir_lista_circular(lista):
    if not lista:
        print('Lista vazia!')
        return
    else:
        atual = lista
        while True:
            print(atual["codigo"], atual["nome"], atual["renda"], end="\n")
            atual = atual["prox"]
            if atual == lista:
                break;

def remover_lista_circular(lista, valor):
    if not lista:
        print('Lista vazia!')
        return None
    atual = lista
    anterior = None
    while True:
        if atual["codigo"] == valor:
            if anterior:
                anterior["prox"] = atual["prox"]
                if atual == lista:
                    lista = atual["prox"]
            else:#se tenho so 1 elemento
                if atual["prox"] == lista:
                    return None
                else:#se quem eu quero apagar é o 1o    
                    lista = atual["prox"]
                    temp = lista
                    while temp["prox"] != atual:
                        temp = temp["prox"]
                    temp["prox"] = lista
                return lista
        anterior = atual
        atual = atual["prox"]
        if atual == lista:
            break
    print('Elemento nao encontrado')
    return lista
        

#main

lista = None
lista = inserir_lista_circular(lista, 1, 'Ana Maria', 4525.00)
lista = inserir_lista_circular(lista, 2, 'Pedro', 4525.00)
lista = inserir_lista_circular(lista, 3, 'Patricia', 4525.00)
lista = inserir_lista_circular(lista, 4, 'Joao', 4525.00)
imprimir_lista_circular(lista)
lista = remover_lista_circular(lista, 4)
imprimir_lista_circular(lista)
    