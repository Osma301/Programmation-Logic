"""
Faça um algoritmo que calcule e mostre os 20 primeiros números primos.
Saída:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71
"""
contador_numeros_primos = 0
numero_atual = 2    
flag = False
primos = ""

while (contador_numeros_primos < 20):         
    for i in range(2, numero_atual):
        if numero_atual % i == 0:
            flag = True
            break

    if not flag:
        primos += f"{numero_atual} "
        contador_numeros_primos += 1

    flag = False
    numero_atual += 1

print(primos)