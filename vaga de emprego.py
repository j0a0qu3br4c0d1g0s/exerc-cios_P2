idade = int(input("Digite a sua idade: "))
nacionalidade = str(input("Digite a sua nacionalidade: "))
experiência = int(input("Quantos anos de experiência você tem?: "))
if idade >= 18 and nacionalidade == "brasileira" or "brasileiro" and experiência >= 2:
   print("Você é elegível para a vaga de emprego.")
else:
   print("Desculpe, você não tem os requisistos para a vaga de emprego.")