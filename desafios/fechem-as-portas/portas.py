with open("entrada.txt", "r") as entrada:
    with open("saida.txt", "w") as saida:

        n = int(entrada.readline())

        while n != 0:
            portas = []

            for i in range(1, n + 1):
                if int(i ** 0.5) ** 2 == i:
                    portas.append(str(i))

            saida.write(" ".join(portas) + "\n")

            linha = entrada.readline()

            if linha == "":
                break

            n = int(linha)