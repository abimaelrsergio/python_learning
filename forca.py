
def play_forca():
    print('#################')
    print('# Game of Forca #')
    print('#################')

    palavra_para_adivinhar = 'impressora'.upper()
    acertos = ['_','_','_','_','_','_','_','_','_','_']
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

    print('Fim do jogo')


if __name__ == '__main__':
    play_forca()

