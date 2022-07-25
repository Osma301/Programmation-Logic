"""
Faça um programa que receba do usuario um vetor 
com 5 posições. Em seguida, mostre
o maior e o menor elemento do vetor.

"""

lista_user = []
maior = 0
menor = 0
for i in range(5):
    numero = int(input("Digite um valor: "))
    lista_user.append(numero)
    if i == 0:
        maior = numero
        menor = numero
    elif numero > maior:
        maior = numero
    elif menor < numero :
        menor = numero
print(menor)
print(maior)



    

    