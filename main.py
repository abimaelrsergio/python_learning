print('#######################')
print('# Ask To Oráculo Game #')
print('#######################')

sequencia_numerica = 43
numero_jogadas = 4
round = 1

for round in range(1, numero_jogadas + 1):
    print('jogada {} de {}'.format(round, numero_jogadas))
    tentativa = int(input('Adivinhe a sequência numérica, digite um número:'))
    print('Você digitou:', tentativa)

    adivinhou = tentativa == sequencia_numerica
    numero_maior = tentativa > sequencia_numerica
    numero_menor = tentativa < sequencia_numerica

    if adivinhou:
        print('Adivinhou, parabéns!')
    else:
        if numero_maior:
            print('Sua sugestão foi maior do que a sequência numérica')
        elif numero_menor:
            print('Sua sugetão foi menor do que a sequência numérica')
        print('Infelizmente, vocẽ não acertou.')
    print('----------------')
print('Game Over!')