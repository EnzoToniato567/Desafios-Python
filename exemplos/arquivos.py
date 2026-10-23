# Exemplo simples dos modos de arquivo: w, a e r.

from pathlib import Path

arquivo_exemplo = Path(__file__).with_name("exemplo_arquivo.txt")

# "w" cria o arquivo ou substitui seu conteúdo.
with open(arquivo_exemplo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha\n")

# "a" acrescenta texto ao final, sem apagar a primeira linha.
with open(arquivo_exemplo, "a", encoding="utf-8") as arquivo:
    arquivo.write("Segunda linha\n")

# "r" lê o conteúdo do arquivo.
with open(arquivo_exemplo, "r", encoding="utf-8") as arquivo:
    print(arquivo.read(), end="")
