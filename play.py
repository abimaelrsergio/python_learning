import forca
import oraculo

print('#####################')
print('# Selecione um jogo #')
print('#####################')

print('(1) Forca  (2) Oráculo')
game = int(input('> '))

if game == 1:
    print('Forca')
    forca.play_forca()
elif game == 2:
    print('Oráculo')
    oraculo.play_oraculo()

