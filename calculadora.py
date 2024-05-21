###
# atividade calculadora
# Aluno: caio schaedler
# data 10/05/2024
###

print("Escolha uma opção:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("X - Sair")
#mostrando o menu ao usuario
soma = 0
dim = 0
multi = 0
divi = 0
#dando valores as variaveis
while True:
    opcao = input("Digite a opção desejada: ")
#solicitando a opcao desejada
    if opcao.upper() == "X":
        print("Encerrando a calculadora. Até logo!")
        break
# finalizando o programa caso o usuario digite "x"
    opcao = int(opcao)
#transformando opcao em variavel inteira
    if opcao == 1:
        s = int(input("Digite a quantidade de valores a serem somados: "))
        for i in range(s):
            valor = float(input(f"Digite o valor {i+1}: "))
            soma += valor
        print(f"A soma dos valores digitados é: {soma:.2f}")
#somando caso o usuario escolha a opcao 1 
    elif opcao == 2:
        d = int(input("Digite a quantidade de valores a serem subtraídos: "))
        for i in range(d):
            valor = float(input(f"Digite o valor {i+1}: "))
            dim -= valor
        print(f"A subtração dos valores digitados é: {dim:.2f}")
#diminuindo caso o usuario escolha a opcao 2 
    elif opcao == 3:
        m = int(input("Digite a quantidade de valores a serem multiplicados: "))
        for i in range(m):
            valor = float(input(f"Digite o valor {i+1}: "))
            multi *= valor
        print(f"A multiplicação dos valores digitados é: {multi:.2f}")
#multiplicando caso o usuario escolha a opcao 3 
    elif opcao == 4:
        a = int(input("Digite a quantidade de valores a serem divididos: "))
        for i in range(a):
            valor = float(input(f"Digite o valor {i+1}: "))
            divi *= valor
        print(f"A divisão dos valores digitados é: {divi:.2f}")
#dividindo caso o usuario escolha a opcao 4
    else:
        print("Opção inválida. Tente novamente.")
#aparecendo opcao invalida caso o usuario tenha escolhido uma opcao invalida do menu