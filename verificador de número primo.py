numero = int(input("Digite um número inteiro positivo para verificar se é primo: "))
 
if numero <= 1:
        print(f"O número {numero} não é primo.")
else:
        
        primo = True
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break
        
        if primo:
            print(f"O número {numero} é primo.")
        else:
            print(f"O número {numero} não é primo.")

            print("Esse número não é primo, digite um outro número.")
