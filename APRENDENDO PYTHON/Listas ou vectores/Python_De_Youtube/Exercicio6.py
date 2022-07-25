"""
6) Faça um programa que possua um vetor denominado 
A que armazene 6 numeros inteiros.
O programa deve executar os seguintes passos:

(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
(b) Armazene em uma variavel a soma entre os valores das posições A[0], 
A[1] e A[5] do vetor e mostre na tela esta soma.
(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
(d) Mostre na tela cada valor do vetor A, um em cada linha.

"""
denominado = [1,0,5,-2,-5,7]

denominado = [1,0,5,-2,-5,7]

soma = denominado[0] + denominado[1] + denominado[5]
print(soma)
"""
modifique o vector na posição 4 , atribuindo a esta posição o valor 100

"""
denominado = [1,0,5,-2,-5,7]
denominado[4] = 100

for item in denominado:
    print(item)
