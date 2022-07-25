"""
Escreva um algoritmo que receba um número e 
calcule o fatorial desse número.
Entrada:
5
Saída: 120 / 
Escriba un algoritmo que reciba un número y calcule
el factorial de ese número: entrada
5 
salida: 120
"""

numero = int(input("Digite um número: "))
fatoracao = numero
i = 0
for i in range(numero - 1, 0, -1):
    fatoracao *= i

print(f"O fator de {numero} é: {fatoracao}")
