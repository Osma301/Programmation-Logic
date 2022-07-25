"""

1) Leia um vetor de 10 posições. 
Calcule e escreva quantos valores pares ele possui.

"""

lista = []

for i in range(10):
    valor = int(input(f"Digite o primeiro {i + 1}º valor: "))
    if i % 2 == 0:
        lista.append(valor)
print(f"A quantidade de numeros pares é de: {len(lista)} valor(es) par(es)")