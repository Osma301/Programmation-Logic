"""
Funções: são trechos de codigos que podem ser utilizados.
Funções x Procedimentos:
-Funções retornam valores
-Procedimentos não retornam valores
#Sempre definir as funções encima do codigo

"""
# def lavar_louça():
#     print("ALISON VAI LAVAR LOUÇA!")
# def limpar_chao():
#     return "ALEXANDRE VAI LIMPAR O CHÃO"

# def levar_lixo(nome:str):
#     print(f"{nome} VAI LEVAR O LIXO")







# retorno = lavar_louça()
# print(retorno)

# print(limpar_chao())

# levar_lixo("Osmando")









"""
PARTE 2

"""
def somar(numero_1: int, numero_2: int):
    """A função  retorna a soma de dois numeros"""
    return numero_1 + numero_2

def substrair(numero_1: int, numero_2: int):
    """A função retorna a subistração de dois numeros"""
    return numero_1 - numero_2

def multiplicar(numero_1: int, numero_2: int) -> int:
    """Esta função vai multiplicar"""
    return numero_1 * numero_2
def dividir(numero_1: int, numero_2: int) -> float:
    """Esta função faz uma divisão"""
    return numero_1 / numero_2

def mostrar_menu()->int:
    """A função mostra o menu de opções"""
    return int(input("""
        CALCULADORA 
    1)somar:  
    2)restar:
    3)multiplicar:
    4)dividir: 
    5)sair
    Opção escolhida: 
        """))

while True:
    opcao = mostrar_menu()
    if opcao == 5:
        break
    if opcao > 5 or opcao < 1:
        print("Poderia digitar uma opção POR FAVOR!!")
        continue
    numero_1 = int(input("Digite o 1 numero: "))
    numero_2 = int(input("Digite o 2 numero: "))
    resultado = None
    
    if opcao == 1:
        resultado = somar(numero_1, numero_2)
    elif opcao == 2:
        resultado = substrair(numero_1, numero_2)
    elif opcao == 3:
        resultado = multiplicar(numero_1, numero_2)
    elif opcao == 4:
        resultado = dividir(numero_1, numero_2)
    print(f"O resultado da operação é {resultado}")
