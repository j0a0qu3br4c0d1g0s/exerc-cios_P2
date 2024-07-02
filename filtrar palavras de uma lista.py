Palavras = ['Tilapia', 'Bacalhau', 'Salmão', 'Sardinha', 'Baiacu', 'Tubarão', 'Pesca', 'Barco']


Letra = input("Digite uma letra para filtrar as palavras: ")


print(f"Palavras que começam com '{Letra}': ")
for palavra in Palavras:
    if palavra.startswith(Letra):
        print(palavra)