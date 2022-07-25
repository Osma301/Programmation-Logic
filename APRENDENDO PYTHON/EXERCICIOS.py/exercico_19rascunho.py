while True:
    matricula = int(input("coloque a sua matricula:  "))
    if matricula == 0:
        break
    nota1 = float(input("Coloque sua primera nota: "))
    nota2 = float(input("Coloque sua segunda nota: "))
    nota3 = float(input("Coloque sua tercera nota: "))
    media = (nota1 + nota2 + nota3) / 3
    print(f"A media do aluno com a matricula: {matricula} é {media:.2f}")
