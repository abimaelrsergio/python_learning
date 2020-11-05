
def play_forca():
    print('#################')
    print('# Game of Forca #')
    print('#################')

    palavra_para_adivinhar = 'impressora'
    enforcado = False
    ganhou = False

    while not enforcado and not ganhou:
        tentativa = input('Informe uma letra: ')
        tentativa = tentativa.strip()
        indice = 0
        for letra in palavra_para_adivinhar:
            if tentativa.upper() == letra.upper():
                print('Encontrada a letra: {}, no indice: {}'.format(letra, indice))
            indice = indice + 1
        print('jogando...')

    print('Fim do jogo')


if __name__ == '__main__':
    play_forca()

