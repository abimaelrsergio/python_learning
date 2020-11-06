import random

def play_forca():
    boas_vindas()
    palavra_para_adivinhar = buscar_palavras_adivinhar()
    acertos = inicializar_acertos(palavra_para_adivinhar)

    enforcado = False
    total_tentativas = 0
    ganhou = False
    print(acertos)
    while not enforcado and not ganhou:
        tentativa = solicitar_tentativa()
        if tentativa in palavra_para_adivinhar:
            armazenar_acertos(acertos, palavra_para_adivinhar, tentativa)
        else:
            total_tentativas += 1
            enforcando(total_tentativas)
        enforcado = total_tentativas == 7
        ganhou = '_' not in acertos
        print(acertos)
    if ganhou:
        mostrar_msg_sucesso()
    else:
        mostrar_msg_falha()
    print('Fim do jogo')


def enforcando(total_tentativas):
    print(" _______ ")
    print(" |/ | ")

    if(total_tentativas == 1):
        print(" | (_) ")
        print(" |    ")
        print(" |    ")
        print(" |    ")

    if(total_tentativas == 2):
        print(" | (_) ")
        print(" | \ ")
        print(" |    ")
        print(" |    ")

    if(total_tentativas == 3):
        print(" | (_) ")
        print(" | \| ")
        print(" |    ")
        print(" |    ")

    if(total_tentativas == 4):
        print(" | (_) ")
        print(" | \|/ ")
        print(" |    ")
        print(" |    ")

    if(total_tentativas == 5):
        print(" | (_) ")
        print(" | \|/ ")
        print(" |  | ")
        print(" |    ")

    if(total_tentativas == 6):
        print(" | (_) ")
        print(" | \|/ ")
        print(" |  | ")
        print(" | / ")

    if (total_tentativas == 7):
        print(" | (_) ")
        print(" | \|/ ")
        print(" |  | ")
        print(" | / \ ")

    print(" | ")
    print("_|___  ")
    print()


def mostrar_msg_falha():
    print('Perdeu!')


def mostrar_msg_sucesso():
    print('Parabéns, ganhou o jogo!')


def armazenar_acertos(acertos, palavra_para_adivinhar, tentativa):
    indice = 0
    for letra in palavra_para_adivinhar:
        if tentativa == letra:
            acertos[indice] = tentativa
        indice += 1


def solicitar_tentativa():
    tentativa = input('Informe uma letra: ')
    tentativa = tentativa.strip().upper()
    return tentativa


def inicializar_acertos(palavra_para_adivinhar):
    return ['_' for letra in palavra_para_adivinhar]


def buscar_palavras_adivinhar():
    lista_palavras = []
    file = open('arquivo.txt', 'r')
    for line in file:
        line = line.strip()
        lista_palavras.append(line)
    file.close()

    posicao_lista = random.randrange(0, len(lista_palavras))
    palavra_para_adivinhar = lista_palavras[posicao_lista].upper()
    return palavra_para_adivinhar


def boas_vindas():
    print('#################')
    print('# Game of Forca #')
    print('#################')


if __name__ == '__main__':
    play_forca()

