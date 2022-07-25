"""
Escreva um algoritmo que calcule a média aritmética das 3 notas dos alunos de uma classe. O algoritmo deverá ler, 
além das notas, o código do aluno e deverá ser encerrado quando o código for igual a zero. Entrada:
0012021
10
8
9
0022021
10
10
10
0
Saída:
A média do aluno com a matrícula 0012021 é 9.00
A média do aluno com a matrícula 0022021 é 10.00

"""
while True:
    matricula = int(input("Digite a sua matricula aqui: "))
    if matricula == 0:
        break
    nota1 = float(input("Digite a sua primeira nota: "))
    nota2 = float(input("Digite a sua segunda nota: "))
    nota3 = float(input("Digite a sua terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    print(f"A media do aluno com a matricula: {matricula} é {media}")    

