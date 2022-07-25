"""
Crie uma função que receba uma array e retorne o primeiro e o 
último elemento desse array como um novo array.
O array pode ter qualquer tamanho.

"""

def receber(lista = [1,2,3,4,5,6,7,8,9,10]):
    return [lista[0],lista[-1]]
print(receber())