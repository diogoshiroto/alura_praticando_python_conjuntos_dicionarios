lista_laura = set(input("Lista de Laura: ").lower().split(', '))
lista_ana = set(input("Lista de Ana: ").lower().split(', '))

laura_exclusivo = lista_laura.difference(lista_ana)
ana_excplusivo = lista_ana.difference(lista_laura)
interseccao = lista_laura.intersection(lista_ana)

print(f"Itens em ambas as listas: {', '.join(interseccao)}")
print(f"Itens exclusivos de Laura: {', '.join(laura_exclusivo)}")
print(f"Itens exclusivos de Ana: {', '.join(ana_excplusivo)}")