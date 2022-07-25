"""
2) Escreva um programa que leia 5 numeros e os armazene em um vetor. Mostre o vetor, o 
maior elemento e a posição que ele se encontra.

"""


# lista = []

# for i in range(5):
#     lista.append(int(input(f"Digite o {i + 1}º: ")))
#     pos_maior = lista.index(max(lista))
# print(lista)
# print(f"numero maior {max(lista)}")
# print(f"A posição do numero é: {pos_maior}")
numeros = []
maior = 0
posicao = 0
for i in range(5):
    valor = int(input("Digite um número: "))
    numeros.append(valor)

    if valor > maior:
        maior = valor
        posicao = i

print(numeros)
print(maior)
print(posicao)
