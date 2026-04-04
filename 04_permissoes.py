principais = set(input("Permissões principais: ").lower().split(', '))
solicitadas = set(input("Permissões solicitadas: ").lower().split(', '))

print("Principais = ", principais)
print("Solicitadas = ", solicitadas)

if solicitadas.issubset(principais):
    print("As permissões solicitadas fazem parte das permissões principais.")
else:
    print("As permissões solicitadas não fazem parte das permissões principais.")