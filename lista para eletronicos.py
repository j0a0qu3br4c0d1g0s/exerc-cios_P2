comidas = ['leite', 'couve', 'computador', 'tomate', 'garfo', 'faca', 'tablet', 'refrigerante']
bebidas = ['uva', 'colher', 'TV', 'vinho', 'cerveja', 'celular', 'banana']
talheres = ['arroz', 'iPhone', 'concha', 'whisky', 'vodka', 'feijão', 'colher de chá']

eletronicos = []

comidas = sorted([item for item in comidas if item not in bebidas and item not in talheres])
bebidas = sorted([item for item in bebidas if item not in comidas and item not in talheres])
talheres = sorted([item for item in talheres if item not in comidas and item not in bebidas])

for lista in [comidas, bebidas, talheres]:
    for item in lista:
        if item in ['computador', 'tablet', 'TV', 'iPhone', 'celular']:
            eletronicos.append(item)
        else:
            continue

print("Comidas:", comidas)
print("Bebidas:", bebidas)
print("Talheres:", talheres)
print("Eletrônicos:", eletronicos)