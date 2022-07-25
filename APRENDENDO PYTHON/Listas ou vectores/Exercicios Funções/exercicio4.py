"""
Escreva um script que receba o ano em que 
você nasceu e calcule a sua idade. Utilize uma função que retorna a
idade.
"""
from datetime import date

def calcular_edad(fecha_nac):
    diferencia_datas = date.today()-fecha_nac
    diferencia_datas_dias = diferencia_datas.days
    edad_numerica = diferencia_datas_dias / 365.2425
    edad = int(edad_numerica)
    return edad
fecha_nac = date()
print(calcular_edad(fecha_nac))