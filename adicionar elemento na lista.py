lista_elementos = []

while True:
    elemento = input("Digite um elemento para adicionar na lista ( ou digite 'parar' para encerrar): ")
    
    if elemento.lower() == 'parar':
        break
    
    lista_elementos.append(elemento)

print("\nlista completa:")
print(lista_elementos)