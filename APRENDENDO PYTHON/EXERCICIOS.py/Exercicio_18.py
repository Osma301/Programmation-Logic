"""
Faça um algoritmo que mostre os conceitos finais dos alunos de uma classe de 4 alunos.
a) a média de cada aluno será fornecida pelo usuário.
b) a tabela de conceitos se encontra abaixo:
Nota	Conceito
de 0.0 à 4.9	D
de 5.0 à 6.9	C
de 7.0 à 8.9	B
de 9.0 à 10.0	A

"""
for i in range(5):
    media = float(input("Digite a média: "))

    if media < 0 or media > 10:
        print("Valor inválido")
    elif media < 5 and media >= 0:
        print("Conceito D")
    elif media < 7:
        print("Conceito C")
    elif media < 9:
        print("Conceito B")
    else:
        print("Conceito A")