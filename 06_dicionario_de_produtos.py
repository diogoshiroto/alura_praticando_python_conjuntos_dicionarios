produtos = {}

for i in range(3):
    nome = input("Digite o nome do produto: ")
    quantidade = input("Digite a quantidade: ")

    produtos[nome] = quantidade

print("Dicionário de produtos: ", produtos)