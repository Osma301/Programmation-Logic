"""
Faça um script que receba valores inteiros e 
mostre na tela quantos desses valores recebidos estão no intervalo [10, 20] e quantos não estão.
O programa irá parar de pedir números quando o usuário digitar um número negativo.

"""

numeros_dentro = 0

numeros_fora = 0

while True:
    valor_digitado = int(input("Valor digitado: "))

    if valor_digitado < 0:
        break

    if valor_digitado >= 10 and valor_digitado <= 20:

        numeros_dentro += 1
    else:
        numeros_fora += 1

print(f"{numeros_dentro} os nomeros dentro do intervalo")

print(f"{numeros_fora} os nomeros fora do intervalo")
