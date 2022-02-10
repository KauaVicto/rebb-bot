import acao
from acesso import iniciar, login
from interface import terminal
from acao import arquivo
from acao import recomecar, comentar, disfarce
from random import randint
from time import sleep

#Pega os dados
'''usuario = str(input('Digite seu Usuário: '))
senha = str(input('Digite sua Senha: '))
marcar = dado.lerInt('Quantas pessoas você deve marcar por comentário? ')
conti = dado.lerInt('Deseja continuar[0] ou recomeçar[1] com a lista de seguidores? ')
comQuant = dado.lerInt('Quantos comentarios você deseja comentar? ')
frase = str(input('Deseja por alguma frase antes? (Caso não, pule a pergunta) ')).strip()'''


def principal_comentar(valores):
    marc_com = []

    try:
        #Guarda os dados de login e senha e do navegador em um dicionário
        dados = iniciar.inic(valores['opera'])
        dados['num_marcar'] = valores['marcar']
    except:
        terminal.Printar('Erro ao iniciar os dados.')
    else:
        terminal.Linha()
        terminal.Printar('Iniciando...')

        #Cria ou ler a lista dos seguidores
        if valores['rSim']:
            link = valores['link']
            qtSegui = valores['qtSegui']
            bSegui = valores['bSeguidor']
            user = valores['usuario']
            senha = valores['senha']

            #Realiza o login
            login.login(user, senha, dados)

            terminal.Linha()
            terminal.Printar('Pegando os seguidores...')
            recomecar(dados, link, qtSegui, bSegui, user, senha)

        c = arquivo.ler()

        if valores['rNao']:
            user = c[-2]
            senha = c[-1]
            login.login(user, senha, dados)

        #Acessa o foto que irá comentar
        login.acessar(dados, c[-3])

        #Realiza os comentarios
        for j in range(0, valores['comQuant']):
            terminal.Linha()

            #Busca do arquivo os seguidores de acordo a quantidade de marcações que deve fazer
            if len(c) >= valores['marcar']:
                for i in range(0, valores['marcar']):
                    marc_com.append(c.pop(randint(0, len(c)-4)))
            else:
                break
            terminal.Printar(f'Comentários hoje: {j+1}/{valores["comQuant"]}')
            terminal.Printar(f'Faltam marcar: {len(c)-3} pessoas')

            arquivo.atualizar(c)
            comentar(dados, valores['frase'], marc_com)
            marc_com.clear()

            valor = randint(0, 100)
            terminal.Printar(f'Valor entre 1 e 100 para o disfarce: {valor}')

            #Executa com 70% de chance o disfarce
            if valor > 70:
                disfarce(dados)
                login.acessar(dados, c[-3])
            else:
                tempo = randint(40, 180)
                terminal.Printar(f'Tempo de espera: {tempo} segundos')
                for t in range(0, 60):
                    print('-', end='')
                    sleep(tempo/60)
                print('|\n')

    print('Fim!')


def principal_seguir(valores):
    try:
        dados = iniciar.inic(valores['opera'])
    except:
        print('deu ruim')
    else:
        terminal.Linha()
        terminal.Printar('Iniciando...')

        # Realiza o login
        login.login(valores['user'], valores['senha'], dados)

        #acessa perfil e segui os 'seguindo'
        acao.seguir_perfis(dados, valores['perfil'])
