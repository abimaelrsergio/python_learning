print('#######################')
print('# Ask To Oráculo Game #')
print('#######################')

sequencia_numerica = 43

tentativa = input('Adivinhe a sequência numérica, digite um número:')
print('Você digitou:', tentativa)

if (tentativa == sequencia_numerica):
    print('Adivinhou, parabéns!')
else:
    print('Infelizmente, vocẽ não acertou.')

