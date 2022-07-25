"""Faça um programa que receba um número N e mostre na tela todos os números ímpares de 0 até N.
Entrada: 5
Saída: 1, 3, 5"""

numero = int(input("Digite um numero: "))
for i in range(1, numero + 1, 2):
    print(i)
