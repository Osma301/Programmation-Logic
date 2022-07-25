"""
Faça um programa que simule a urna eleitoral. Apresente um menu com as seguintes informações para o usuário:
1 - José Bolinha
2 - Maria Nascimento
3 - João da Silva
4 - Voto nulo
5 - Voto em branco
Após isso, leia o voto digitado pelo usuário até que ele digite o valor 0. Ao final mostre:

Total de votos para cada candidato;
Total de votos nulos;
Total de votos em branco.
Entrada:
1
1
2
3
3
4
5
0

Saída:
Total de Votos
José Bolinha: 2 voto(s)
Maria Nascimento: 1 voto(s)
João da Silva: 2 voto(s)
Votos nulos: 1 voto(s)
Votos em branco: 1 voto(s)

"""

voto_jose = 0
voto_maria = 0
voto_joão = 0
voto_N = 0
voto_B = 0

while True:
    voto = int(input("Por qual candidato deseja votar: \n1*Jose Bolinha:\n2* Maria Nacimento:\n3 *João da Silva\n4* Para voto nulo\n5* Para voto em branco\nColoque a sua opção:  "))
    if voto == 0:
        
        break
    if voto == 1:
        voto_jose += 1
    elif voto == 2:
        voto_maria += 1
    elif voto == 3:
        voto_joão += 1
    elif voto == 4:
        voto_N += 1
    elif voto == 5:
        voto_B += 1
    else:
        print("Opção invalida")

print(f"1-José Bolinha: {voto_jose} voto (s)\n2-Maria Nacimento: {voto_maria} voto (s)\n3-João da silva: {voto_joão} voto (s)\n4-Votos Nulos: {voto_N} votos (s)\n5-Votos em branco: {voto_B} voto(s)")
