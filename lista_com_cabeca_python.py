def criar_lista():
    # Cria o nó cabeça que aponta para None inicialmente
    return {'quant': None, 'proximo': None}

def criar_no(codigo, descricao, valor):
    return {'codigo': codigo, 'descricao': descricao, 'valor': valor, 'proximo': lista['proximo']}
    
def inserir_inicio(lista, codigo, descricao, valor):
    novo = criar_no(codigo, descricao, valor)
    lista['proximo'] = novo

def imprimir(lista):
    atual = lista['proximo']
    if atual is None:
        print("Lista vazia.")
        return
    print("Lista:", end=" ")
    while atual:
        print(atual['codigo'], atual['descricao'], end=" ")
        atual = atual['proximo']
    print()


def remover(lista, valor):
    anterior = lista
    atual = lista['proximo']
    while atual:
        if atual['codigo'] == valor:
            anterior['proximo'] = atual['proximo']
            print(f"Elemento {valor} removido.")
            return
        anterior = atual
        atual = atual['proximo']
    print(f"Elemento {valor} não encontrado.")

# Exemplo de uso lista com cabeça
lista = criar_lista()
inserir_inicio(lista, 10, 'coca-cola', 2.35)
inserir_inicio(lista, 20, 'batata', 3.25)
inserir_inicio(lista, 30, 'arroz', 5.60)
imprimir(lista)
remover(lista, 20)
imprimir(lista)
remover(lista, 10)
imprimir(lista)
remover(lista, 30)
imprimir(lista)