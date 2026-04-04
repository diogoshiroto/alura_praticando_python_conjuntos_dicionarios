texto_1 = set(input("Texto 1: ").lower().split())
texto_2 = set(input("Texto 2: ").lower().split())

interseccao = texto_1.intersection(texto_2)

print("Palavras em comum: ", interseccao)