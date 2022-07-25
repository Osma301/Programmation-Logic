"""
Faça um programa que receba um número n e mostra na tela os n primeiros números bem como a 
informação se o número é ímpar ou par.
Entrada:
5
Saída:
1 - Ímpar
2 - Par
3 - Ímpar
4 - Par
5 - Ímpar

"""
# contador_n = 0
# contador_p = 0

# for i in range(5):
#     if i == 0:
#         continue
#     elif i % 2 == 0:
#         print(f"Par : {i}")
#     elif i % 2 == 1:
#         contador_p = i
#         print(f"Impar : {i}")


N = int(input("Digite um numero: "))

for i in range(1, N + 1):
    if  i == 0:
        continue
    elif i % 2 == 0:
        print(f"Par : {i}")
    elif i % 2 == 1:
        print(f"Impar : {i}")
    
    
    