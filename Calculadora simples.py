operacao = input("Escolha uma operaçãO(+ , - , * , / ) ")
N1 = float(input("Digite o primeiro número: "))
N2 = float(input("Digite o segundo número: "))
if operacao == '+':
    print("Resultado da adição é: ",(N1 + N2))
elif operacao == '-':
    print("Resultado da subtração é: ",(N1 - N2))
elif operacao == '*':
    print("Resultado da multiplicação é: ",(N1 * N2))
elif operacao == '/':
     if N2 != 0:
        print("Resultado da divisão é: ",(N1 / N2))
     else:
        print("Não é possível dividir por 0")
else:
    print ("Operação inválida, tente novamente")