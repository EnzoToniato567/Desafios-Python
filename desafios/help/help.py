with open("entrada.txt", "r") as entrada:
    with open("saida.txt", "w") as saida:

        linha = entrada.readline()

        while linha:
            n = int(linha)

            if n == 0:
                break

            erros = {}
            tempos = {}
            problemas = set()

            for i in range(n):
                letra, tempo, resultado = entrada.readline().split()
                tempo = int(tempo)

                if resultado == "incorrect":
                    erros[letra] = erros.get(letra, 0) + 1

                elif resultado == "correct":
                    problemas.add(letra)
                    tempos[letra] = tempo + erros.get(letra, 0) * 20

            s = len(problemas)
            p = sum(tempos.values())

            saida.write(f"{s} {p}\n")

            linha = entrada.readline()