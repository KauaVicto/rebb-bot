def abrir():
    try:
        f = open('seguidores.txt', 'w', encoding='UTF-8')
    except:
        print('Erro ao abrir o aquivo.')
    else:
        f = open('seguidores.txt', 'w', encoding='UTF-8')
        return f


def guardarSegui(f, names):
    for i in names:
        f.write(f'{i}\n')
    f.close()


def ler():
    try:
        f = open('seguidores.txt', 'r', encoding='UTF-8')
        c = f.readlines()
        return c
    except:
        print('Erro ao ler o arquivo.')


def atualizar(c):
    # Reescrevendo o arquivo com seguidores removendo os que já foram usados
    f = open('seguidores.txt', 'w', encoding='UTF-8')
    f.writelines(c)
    f.close()
