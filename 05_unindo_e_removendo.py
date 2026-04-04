equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}
equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

combindados = equipe_a.union(equipe_b)

remover = input("Tarefa a ser removida: ").lower()

if remover in combindados:
    combindados.remove(remover)

print("Tarefas finais: ", combindados)