with open("entrada.txt", "r") as entrada:
    with open("saida.txt", "w") as saida:

        n = int(entrada.readline())

        while n != 0:
            comandos = entrada.readline().strip()
            direcao = 0

            for comando in comandos:
                if comando == "D":
                    direcao += 1
                else:
                    direcao -= 1

            direcao = direcao % 4

            direcoes = ["N", "L", "S", "O"]

            saida.write(direcoes[direcao] + "\n")

            n = int(entrada.readline())