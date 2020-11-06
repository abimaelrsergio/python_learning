
def play_forca():
    print('#################')
    print('# Game of Forca #')
    print('#################')

    lista_palavras = []
    file = open('arquivo.txt','r')
    for line in file:
        line = line.strip()
        lista_palavras.append(line)
    file.close()
    print(lista_palavras)

    palavra_para_adivinhar = 'impressora'.upper()
    acertos = ['_' for letra in palavra_para_adivinhar]
    enforcado = False
    total_tentativas = 0
    ganhou = False
    print(acertos)
    while not enforcado and not ganhou:
        tentativa = input('Informe uma letra: ')
        tentativa = tentativa.strip().upper()
        if tentativa in palavra_para_adivinhar:
            indice = 0
            for letra in palavra_para_adivinhar:
                if tentativa == letra:
                    acertos[indice] = tentativa
                indice += 1
        else:
            total_tentativas += 1
        enforcado = total_tentativas == 7
        ganhou = '_' not in acertos
        print(acertos)
    if ganhou:
        print('Parabéns, ganhou o jogo!')
    else:
        print('Perdeu!')
    print('Fim do jogo')


if __name__ == '__main__':
    play_forca()

