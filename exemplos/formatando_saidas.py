# Mostrar valores em uma frase usando marcadores de formato.

produto = "Acerola"
quantidade = 3
preco = 2.5

print("Produto: %s | Quantidade: %d | Preço: R$ %.2f" % (produto, quantidade, preco))
print("Total: R$ %.2f" % (quantidade * preco))
