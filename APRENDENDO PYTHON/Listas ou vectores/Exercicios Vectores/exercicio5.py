"""
Ler um vetor com 5 nomes de pessoas, após pedir que o usuário digite um nome qualquer 
de pessoa. Escrever a mensagem “ACHEI”, se o nome estiver 
armazenado no vetor de nomes ou 
“NÃO ACHEI” caso contrário. 

"""
nomes = ["osmando", "johanna", "mariana",]
for i in range(5):
    nomeis =input("Digite o nome que quer achar: ")
    if nomeis in nomes:
        print('Achei!')
    else:
        print("Não achei!")