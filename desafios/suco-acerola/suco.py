with open("entrada.txt", "r") as entrada:
    with open("saida.txt", "w") as saida:

        linha = entrada.readline()

        while linha:
            n, f = map(int, linha.split())

            if n == 0 and f == 0:
                break

            suco = (f * 50) / n / 1000

            saida.write("%.2f\n" % suco)

            linha = entrada.readline()