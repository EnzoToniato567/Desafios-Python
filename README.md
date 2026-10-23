# Desafios em Python

Soluções de quatro desafios de programação. Cada pasta contém um programa Python, um `entrada.txt` com casos de exemplo e um `saida.txt` com a saída esperada. Os programas leem e escrevem esses arquivos na própria pasta.

## Desafios

| Desafio | O que faz |
| --- | --- |
| [Esquerda Volver](desafios/esquerda-volver/) | Descobre a direção final após uma sequência de giros. |
| [Fechem as Portas](desafios/fechem-as-portas/) | Lista as portas que ficam abertas após as trocas de estado. |
| [Help](desafios/help/) | Calcula problemas resolvidos e a penalidade de uma competição. |
| [Suco de Acerola](desafios/suco-acerola/) | Calcula a quantidade de suco por pessoa. |

## Como testar localmente

É preciso ter Python 3 instalado. No Prompt de Comando (CMD), na raiz do projeto, confira a instalação com `python --version`. Se `python` não executar, substitua-o nos exemplos pelo caminho do interpretador instalado (ou por `py -3`, se disponível).

Entre na pasta do desafio e execute o programa. Por exemplo:

```bat
cd desafios\help
python help.py
type saida.txt
```

O programa usa o `entrada.txt` da pasta atual e **sobrescreve** o `saida.txt`; ele não imprime a resposta no terminal. Para comparar a saída com o exemplo incluído, faça uma cópia do resultado esperado antes de executar:

```bat
copy saida.txt esperado.txt
python help.py
fc esperado.txt saida.txt
del esperado.txt
```

O comando `fc` compara os arquivos e informa se há diferenças; `del` remove a cópia temporária. Para testar outro desafio, volte à raiz com `cd ..\..` e entre na pasta correspondente. Os outros programas são `esquerda.py`, `portas.py` e `suco.py`, conforme indicado nos READMEs de cada pasta.

## Leitura e escrita de arquivos

Os programas usam `open()` para abrir arquivos. O segundo argumento define o modo de abertura:

| Modo | O que acontece |
| --- | --- |
| `"r"` | Abre um arquivo existente para leitura. Gera erro se ele não existir. |
| `"w"` | Abre para escrita, criando o arquivo se necessário. **Apaga o conteúdo anterior** ao abrir um arquivo existente. |
| `"a"` | Abre para escrita no final do arquivo, preservando o conteúdo anterior; também cria o arquivo se necessário. |

Exemplo com os arquivos de um desafio:

```python
with open("entrada.txt", "r") as entrada:
    primeira_linha = entrada.readline()

with open("saida.txt", "w") as saida:
    saida.write(primeira_linha)
```

Esse exemplo lê a primeira linha de `entrada.txt` e a grava em `saida.txt`. `readline()` lê uma linha por vez, `write()` grava o texto recebido e `with` fecha cada arquivo automaticamente. Nos desafios, o modo `"w"` faz a saída ser gerada novamente a cada execução; com `"a"`, novas linhas seriam acrescentadas ao resultado anterior.

## Exemplos para praticar

Cada assunto abaixo tem um arquivo Python na pasta [`exemplos`](exemplos/). Os trechos mostram a ideia principal; abra o arquivo para ver o programa completo.

| Assunto | Exemplo rápido | Arquivo |
| --- | --- | --- |
| Trabalhando com arquivos | `open("dados.txt", "r")` lê; `"w"` substitui; `"a"` acrescenta. | [arquivos.py](exemplos/arquivos.py) |
| Listas | `nomes.append("Ana")` adiciona um item; `nomes[0]` acessa o primeiro. | [listas.py](exemplos/listas.py) |
| Formatando saídas | `"Preço: %.2f" % 5.5` produz `Preço: 5.50`. | [formatando_saidas.py](exemplos/formatando_saidas.py) |
| Margem (largura) | `"%8s" % "Ana"` ocupa 8 posições: 5 espaços seguidos de `Ana`. | [margem.py](exemplos/margem.py) |
| Alinhamento | `%10s` alinha à direita; `%-10s` alinha à esquerda. | [alinhamento.py](exemplos/alinhamento.py) |
| Precisão | `"%.2f" % 5.679` produz `5.68`. | [precisao.py](exemplos/precisao.py) |
| Preenchimento | `"%05d" % 42` produz `00042`. | [preenchimento.py](exemplos/preenchimento.py) |
| Números com sinais | `"%+d" % 12` produz `+12`. | [numeros_com_sinais.py](exemplos/numeros_com_sinais.py) |

No CMD, execute qualquer exemplo a partir da raiz do projeto, trocando o nome do arquivo conforme a tabela:

```bat
python exemplos\listas.py
python exemplos\arquivos.py
```

O exemplo de arquivos cria `exemplos\exemplo_arquivo.txt` e mostra seu conteúdo no terminal. Ele recomeça esse arquivo a cada execução para demonstrar o modo `"w"`.
