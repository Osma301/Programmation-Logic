"""
La alcaldia de la ciudad hizo una busqueda entre sus habitantes, 
colectando datos sobre el salario y numero de hijos. la alcaldia quiere saber:
a) media del salario de la populación
b) media del numero de hijos
c) mayor salario

Cree um script que lea las informaciones necesarias del usuario en cuanto el salario escrito no sea negativo.
Despues de las informaciones solicitadas.
Entrada:
3000
3
2000
1
4000
1
-100
Saída:
Média salarial: 3000
Média de filhos: 1.67
Maior salário: 4000

"""
while True: 
    media_salario = float(input("Digite o seu salario: "))
    if media_salario < 0:
        
        break
    media_filhos = float(input("Quantos filhos você tem: "))
    maior_salario = float(input("Maior salario recebido: "))
    if media_salario > 0:
        media_salario = media_salario / 2
    elif media_filhos > 0:
        media_filhos = media_filhos / 2
    
print(f"""
        Media Salario: {media_salario}
        Media Filhos: {media_filhos}
        Maior Salario: {maior_salario}

        """)
