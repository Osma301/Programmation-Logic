"""
Construa um programa que leia vários valores númericos enquanto um valor 
negativo não for digitado. Após isso, mostre a média aritmética dos valores recebidos.

"""

soma = 0
contador = 0
while True:
    valor = int(input("Digite um numero aqui: "))
    if valor < 0:
        break
    soma += valor
    contador += 1

media = soma / contador
print(f"a media dos valores digitados é: {media:.2f}")