"""
Ler um vetor de 5 elementos. Crie um segundo vetor, 
com todos os elementos na ordem 
inversa, ou seja, o último elemento passará a ser o primeiro, 
o penúltimo será o segundo 
e assim por diante. Mostre os dois vetores. 
"""
lista1 = []
lista2 = []

for i in range(5):
    lista1.append(int(input("Digite o valor da primera lista: ")))
for i in range(5):
    lista2.append(int(input("Digite o valor da segunda lista: ")))
print(lista1)
print(lista2[::-1])
    