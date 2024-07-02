fila_de_atendimento = []

fila_de_atendimento.append("Carlos")
print(f"Cliente Carlos foi adicionado à fila.")
fila_de_atendimento.append("Aldaberto")
print(f"Cliente Aldaberto foi adicionado à fila.")
fila_de_atendimento.append("Mário")
print(f"Cliente Mário foi adicionado à fila.")
fila_de_atendimento.append("Antônio")
print(f"Cliente Antônio foi adicionado à fila.")
fila_de_atendimento.append("Guilherme")
print(f"Cliente Guilherme foi adicionado à fila.")

if fila_de_atendimento:
    print("Fila de atendimento:")
    for i, cliente in enumerate(fila_de_atendimento, start=1):
        print(f"{i}. {cliente}")
else:
    print("Fila de atendimento está vazia.")

if fila_de_atendimento:
    cliente = fila_de_atendimento.pop(0)
    print(f"Cliente {cliente} foi atendido.")
else:
    print("Não há clientes para atender.")

if fila_de_atendimento:
    print("\nFila de atendimento atualizada:")
    for i, cliente in enumerate(fila_de_atendimento, start=1):
        print(f"{i}. {cliente}")
else:
    print("Fila de atendimento está vazia.")

if fila_de_atendimento:
    cliente = fila_de_atendimento.pop(0)
    print(f"\nCliente {cliente} foi atendido.")
else:
    print("\nFila vazia, não há clientes para atender.")

if fila_de_atendimento:
    print("\nFila de atendimento atualizada:")
    for i, cliente in enumerate(fila_de_atendimento, start=1):
        print(f"{i}. {cliente}")
else:
    print("Fila de atendimento vazia.")

while fila_de_atendimento:
    cliente = fila_de_atendimento.pop(0)
    print(f"\nCliente {cliente} foi atendido.")

if fila_de_atendimento:
    print("\nFila de atendimento atualizada:")
    for i, cliente in enumerate(fila_de_atendimento, start=1):
        print(f"{i}. {cliente}")
else:
    print("Fila de atendimento vazia.")