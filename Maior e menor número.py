entrada = input("Digite uma lista de números: ")

numeros_str = entrada.split()

lista_numeros = []

for num_str in numeros_str:
    lista_numeros.append(int(num_str))

if lista_numeros:
    menor = lista_numeros[0]
    maior = lista_numeros[0]

    for numero in lista_numeros:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero

    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
else:
    print("Lista vazia. Não há mais números.")