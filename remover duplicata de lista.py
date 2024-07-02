Lista = []

while True:
    entrada = input("Digite um número (ou deixe um espaço em branco para finalizar): ")
    
    if entrada == "":
        break

    else:
        numero = int(entrada)
        Lista.append(numero)

print("\nLista original:", Lista)


Lista_sem_duplicatas = list(set(Lista))


print("Lista sem duplicatas:", Lista_sem_duplicatas)