from time import sleep


def Printar(t):
    print(f'{t:<60}|')


def Linha():
    print('-'*60 + '|')


def barra_espera(tempo):
    for i in range(0, 60):
        print('-', end='')
        sleep(tempo / 60)
    print('|')