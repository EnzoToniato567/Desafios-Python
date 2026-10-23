# Criar, alterar e percorrer uma lista.

nomes = ["Caio", "Ana", "Bia"]
nomes.append("Davi")

print("Primeiro nome:", nomes[0])

nomes.sort()
print("Nomes em ordem:")
for nome in nomes:
    print(nome)
