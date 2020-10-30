
def play_forca():
    print('#################')
    print('# Game of Forca #')
    print('#################')

    palavra_para_adivinhar = 'impressora'
    enforcado = False
    ganhou = False

    while not enforcado and not ganhou:
        tentativa = input('Informe uma letra: ')
        for letra in palavra_para_adivinhar:
            if tentativa == letra:
                print(letra)
        print('jogando...')

    print('Fim do jogo')


if __name__ == '__main__':
    play_forca()

