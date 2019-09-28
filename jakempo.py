from random import randrange

itens = ['papel', 'pedra', 'tesoura']
computador = randrange(0, 2)

print('''Suas opções são:
[0] papel
[1] pedra
[2] tesoura''')
jogador = int(input('Qual sua jogada? '))
print('-=-'* 12)
print('Você jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[computador]))
print('-=-'* 12)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('''VOCÊ PERDEU!
BOA SORTE NA PROXIMA VEZ''')
    elif jogador == 2:
        print('PARABÉNS VOCÊ GANHOU')
    else:
        print('JOGADA INVÁLIDA')
    
elif computador == 1:
    if jogador == 0:
        print('PARABÉNS VOCÊ GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('''VOCÊ PERDEU
        BOA SORTE NA PROXIMA VEZ''')
    else:
        print('JOGADA INVÁLIDA')
    
elif computador == 2:
    if jogador == 0:
        print('''VOCÊ PERDEU
        BOA SORTE NA PROXIMA VEZ''')
    elif jogador == 1:
        print('PARABÉNS VOCÊ GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')









