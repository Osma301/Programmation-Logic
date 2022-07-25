"""
Crie um script que leia 5 valores e mostre qual o maior e o menor valor lido.
Entrada:
-1
0
9
2
3
Saída:
O menor valor digitado foi -1
O maior valor digitado foi 9


"""
maior = 0
menor = 0

for i in range(5):
    valor = int(input("Digite um valor aqui: "))
    if i == 0:
        maior = valor
        menor = valor
    if valor > maior:
        maior = valor
    if valor <  menor:
        menor = valor
print(maior, menor)


