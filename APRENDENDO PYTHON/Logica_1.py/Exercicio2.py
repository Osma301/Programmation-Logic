# entrada_dados
# numero = int(input("Digite um numero:"))

# #processamento
# if numero % 2 == 0:
#     print("O numero é par")

# else:
#     print("O numero é impar")
# EXERCICIO-4
# primer_valor = int(input("Digite um numero: "))
# if primer_valor > 10:
#     print("O primeiro valor é maior que dez")
# else:
#     print("O primeiro valor não é maior que dez")

# EXERCICIO_4
# numero = int(input('Digite um numero aqui: '))
# if numero % 2 == 0:
#     print("O numero é par ")
# elif numero % 2 == 1:
#     numero = numero * 2
#     print(f"o numero é impar e elevado a dois fica assim: {numero}")


# EXERCICIO_5
# numero = int(input("Digite um numero aqui: "))
# if numero >= 20 and numero < 90:
#     print("O numero esta dentro da faixa ")
# else:
#     print("o numero esta fora da faixa")


# valor_a = int(input("Digite o primer numero: "))
# valor_b = int(input("Digite o segundo numero: "))
# valor_c = int(input("Digite o tercer numero: "))


# if valor_a > valor_b and valor_a > valor_c:
#     print(f"O valor A {valor_a}")
# elif valor_b < valor_c:
#     print(f"O valor {valor_b} é maior")
# else:
#     print(f"O maior valor é: {valor_c}")

# Exercicio_¨6


# resultado = None
# a, b = 10, 2

# if a + b < 4:
#     resultado = "Abaixo"
# else:
#     resultado = "Acima"

# print(resultado)


"""
Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é 
Equilátero, Isósceles ou Escaleno. Sendo que:

Triângulo Equilátero: possui os 3 lados iguais.
Triângulo Isósceles: possui 2 lados iguais.
Triângulo Escaleno: possui 3 lados diferentes.
"""
# lado_1 = int(input("Primeiro lado: "))
# lado_2 = int(input("Segundo lado: "))
# lado_3 = int(input("Colocar o terceiro lado: "))

# if lado_1 == lado_2 and lado_2 == lado_3:
#     print("O triangûlo é: Equilátero")
# elif lado_1 == lado_2 and lado_2 != lado_3:
#     print("O triangûlo é: Isóseles")
# else:
#     print("O triangulo é: Escaleno")

#Exercicio_8
# import math


# numero = int(input("Digite um numero:"))

# if numero < 0:
#     print("O numero é negativo")
# if numero > 0:
#     numero = math.sqrt(numero)
#     print(numero)
#EXERCICIO_ 9
# numero = int(input("Digite um numero: "))

# if numero % 5 == 0:
#     print("Ele é dividido entre 5")
# else:
#     print("Ele não é dividido entre 5")

#Exercicio_10

# import math


# numero = int(input("Digite um numero: "))
# if numero < 0:
#     numero = numero * 2
#     print(f"O numero é negativo o resultado ao cuadrado : {numero}")
# if numero > 0:
#     numero = math.sqrt(numero)
#     print(f"O numero é positivo mas a sua raiz cuadrada é igual a isso daqui: {numero}")


#Exercicio_11
"""
Leia o salario de um trabalhador e o valor da prestação de um empréstimo. Se a prestaçao 
for maior que 20% do salário imprima: “empréstimo não concedido”, caso contrario imprima: 
“empréstimo concedido”.


"""
# salario = float(input("Colocar salario do trabalhador: R$"))
# valor_prestacao = float(input("Qual é o valor da prestação: R$"))

# if valor_prestacao > 0.20 * salario:
#     print("Emprestimo não concedido")
# else:
#     print("Emprestimo concedido")


#Exercicio_12
# time_1 = int(input("Gol primeiro time: "))
# time_2 = int(input("Gol segundo time: "))

# if time_1 > time_2:
#     print("Ganha o Time 1 😁")
# elif time_1 < time_2:
#     print("Ganha o Time 2 😁")
# else:
#     print("Time 1 e Time 2 ficaram em empate 😂😎")

#Exercicio_13
"""
Desenvolva um programa que receba do usuário a sua idade e informe a 
situação de voto dele 
("Não precisa votar", "Voto opcional", "Voto obrigatório").

"""

# idade = int(input("Informe a sua idade: "))

# if idade >= 18 or idade == 70:
#     print("Voto Obrigatorio")
# if idade < 16:
#     print("Não pode votar")
# if idade == 16:
#     print("Voto opcional")

#EXERCICIO_15

# numero_a = int(input("Colocar um numero: "))
# numero_b = int(input("Colocar outro numero: "))
# numero_c = int(input("Colocar un numero aqui: "))

# if numero_c > numero_b:
#     numero_c, numero_b = numero_b,numero_c

# if numero_b > numero_a:
#     numero_b, numero_a = numero_a , numero_b

# if numero_c > numero_b:
#     numero_c, numero_b = numero_b , numero_c
# print({numero_a}{numero_b}{numero_c})



# EXERCICIO_16

# idade = int(input("Digite a sua idade: "))

# if idade == 18 or idade < 67:
#     print("Não pode doar")
# else:
#     print("Pode doar")


#exercicio _ 17
# numero_0 = int(input('Digite un numero: '))

# if numero_0 == 1:
#     print("O seu mes escolhido é: Janeiro")
# elif numero_0 == 2:
#     print("O mes escolhido é: Fevreiro")
# elif numero_0 == 3:
#     print('Seu numero escolhido é: Março')
# elif numero_0 == 4:
#     print("Seu mes escolhido foi: Abril")
# elif numero_0 == 5:
#     print("Seu mes escolhido foi: Maio")
# elif numero_0 == 6:
#     print('O seu mes escolhido foi: Junho')
# elif numero_0 == 7:
#     print("O seu mes escolhido foi: Julho")

# elif numero_0 == 8:
#     print("O seu mes escolhido foi: Agosto")

# elif numero_0 == 9:
#     print("O seu mes escolhido foi: Septembro")
# elif numero_0 == 10:
#     print("O seu mes escolhido foi: Outubro")
# elif numero_0 == 11:
#     print("O seu mes escolhido foi: Novembro")
# elif numero_0 == 11:
#     print("O seu mes escolhido foi: Outubro")
# elif numero_0 == 12:
#     print("O seu mes escolhido foi: Dezembro")
# else:
#     print("O numero não concorda com nemhum mes")
    

#EXERCICIO_19
# turno_estuda = input("En que turno você estuda: ").upper() - TODAS AS LINGUAGENS TRANSFORMAN EN MAYUSCULA

#Switch - case
# if turno_estuda == "M":
#     print("Você estuda no turno: Bom dia!")
# elif turno_estuda == "V":
#     print("Voce estuda no turno: Boa tarde!")
# elif turno_estuda == "N":
#     print("Você estuda no turno: Boa noite!")
# else:
#     print("Valor inválido")

#Ultimo_Exercicio:

# salario = float(input("Informe o seu salario: R$ "))

# if salario < 600:
#     print("Isento")

# elif salario <= 600:
#     salario = salario - salario * .2
#     print(f"Foi retirado o 20% do salario {salario}")

# elif salario <= 1200:
#     salario = salario - salario * .25
#     print(f"Foi retirado o 25% do salario {salario}")

# elif salario <= 2000:
#     salario = salario - salario * .25
#     print(f"Foi retirado o 25% do salario {salario}")

# elif salario > 2000:
#     salario = salario - salario * .3
#     print(f"Foi retirado o 30% do salario {salario}")

# else:
#     print("O valor do salario é invalido")
