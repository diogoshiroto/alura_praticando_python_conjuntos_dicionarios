lista_nomes = set()

while True:
    nome = input("Digite o nome do convidado: ")

    if nome.lower() == "sair":
        break

    lista_nomes.add(nome)
    

print(f"Convidados confirmados: {', '.join(lista_nomes)}")