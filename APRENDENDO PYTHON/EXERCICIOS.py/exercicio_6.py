"""

Faça um programa que peça ao usuario para digitar 5 valores. 
Ao final, mostre a soma desses valores e média desses valores 
(arredondado para duas casas decimais).

"""
soma = 0
for i in range(5):
    valor = int(input("Digite um valor aqui: "))
    soma += valor
print(soma)
print(f"{soma / 5:.2f}")



