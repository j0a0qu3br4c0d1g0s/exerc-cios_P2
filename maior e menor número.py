entrada = input('Digite uma lista de números: ')

numeros_str = entrada.split()

Lista_de_numeros = []

for num_str in numeros_str:
    Lista_de_numeros.append(int(num_str))

if Lista_de_numeros:
    menor = Lista_de_numeros[0]
    maior = Lista_de_numeros[0]

    for numero in Lista_de_numeros:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero

    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
else:
    print("Lista vazia. Não há mais números aqui.")
