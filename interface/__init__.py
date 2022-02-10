from PySimpleGUI import PySimpleGUI as sg
from sys import exit
import principal
import threading

sg.theme('DarkGray14')
# sg.theme_previewer()


def janela_inicial():
    layout = [
        [sg.Button('Seguir Perfis', size=(40, 1))],
        [sg.Button('Comentar', size=(40, 1))]
    ]
    window_inicial = sg.Window('Bot Pix', layout)

    while True:
        eventos_init, valores_init = window_inicial.read()

        if eventos_init == sg.WINDOW_CLOSED:
            break
        if eventos_init == 'Comentar':
            window_inicial.close()
            janela_comentar()
            break
        if eventos_init == 'Seguir Perfis':
            window_inicial.close()
            janela_seguir()
            break


def janela_comentar():
    layout = [
        [sg.Text('Recomeçar:'),
         sg.Radio('Sim', 'recomecar', key='rSim', default=True, enable_events=True),
         sg.Radio('Não', 'recomecar', key='rNao', enable_events=True)],

        [sg.Text('Usuário:', size=(8, 1), key='usuarioTxt', visible=True)],
        [sg.Input(key='usuario', size=(20, 1), visible=True)],
        [sg.Text('Senha:', size=(8, 1), key='senhaTxt')], [sg.Input(key='senha', password_char='*', size=(20, 1))],
        [sg.Text('Frase:', size=(8, 1), key='fraseTxt')], [sg.Input(key='frase', size=(20, 1))],

        [sg.Text('Link do Post:', key='linkTxt', visible=True)],
        [sg.Input(key='link', size=(40, 1), visible=True)],
        [sg.Text('Número de seguidores:', size=(33, 1), key='qtSeguiTxt', visible=True)],
        [sg.Input(key='qtSegui', size=(15, 1), visible=True)],
        [sg.Text('Buscar:', visible=True, key='buscaTxt')],
        [sg.Radio('Seguidores', 'busca', key='bSeguidor', visible=True, default=True, enable_events=True)],
        [sg.Radio('Seguindo', 'busca', key='bSeguindo', visible=True, enable_events=True)],

        [sg.Text('Navegador:'),
         sg.Radio('Opera', 'navegador', key='opera', default=True),
         sg.Radio('Google Chrome', 'navegador', key='chrome')],
        [sg.Text('Marcações:')],
        [sg.Slider(range=(0, 5), default_value=3, size=(20, 15), orientation='h', key='marcar')],
        [sg.Text('Quantidade de comentarios:')],
        [sg.Slider(range=(1, 300), default_value=20, size=(40, 15), orientation='h', key='comQuant')],
        [sg.Button('Enviar')]
        # [sg.Output(size=(80, 20), key='output')]
    ]
    window = sg.Window('Bot de comentários', layout, resizable=True)

    while True:
        eventos, valores = window.read()
        #window['output'].update(value=f'{"Informações":-^60}')
        if eventos == sg.WINDOW_CLOSED:
            exit()
            break
        if eventos == 'rSim':
            window['link'].update(disabled=False)
            window['qtSegui'].update(disabled=False)
            window['usuario'].update(disabled=False)
            window['senha'].update(disabled=False)
            window['frase'].update(disabled=False)
            window['bSeguidor'].update(disabled=False)
            window['bSeguindo'].update(disabled=False)
        elif eventos == 'rNao':
            window['link'].update(disabled=True)
            window['qtSegui'].update(disabled=True)
            window['usuario'].update(disabled=True)
            window['senha'].update(disabled=True)
            window['frase'].update(disabled=True)
            window['bSeguidor'].update(disabled=True)
            window['bSeguindo'].update(disabled=True)

        if eventos == 'Enviar':
            try:
                valores['marcar'] = int(valores['marcar'])
                valores['comQuant'] = int(valores['comQuant'])
                if valores['rSim']:
                    valores['qtSegui'] = int(valores['qtSegui'])
                window.close()
                janela_terminal(valores, 'comentar')
            except:
                print('Erro! Digite os valores inteiros válidos!')


def janela_terminal(valores, acao):
    layout_terminal = [
        [sg.Output(size=(80, 20), key='output', font=('Courier 11'))],
        [sg.Button('Iniciar')]
    ]
    window = sg.Window('Bot de comentários', layout_terminal, resizable=True)

    while True:
        eventos2, valores2 = window.read()
        # window['output'].update(value=f'{"Informações":-^60}')
        if eventos2 == sg.WINDOW_CLOSED:
            exit()
            break

        if eventos2 == 'Iniciar':
            try:
                if acao == 'comentar':
                    threading.Thread(target=principal.principal_comentar, args=(valores,), daemon=True).start()
                elif acao == 'seguir':
                    threading.Thread(target=principal.principal_seguir, args=(valores,), daemon=True).start()
            except:
                print('Erro! Digite os valores inteiros válidos!')


def janela_seguir():
    layout = [
        [sg.Text('Usuário:', size=(8, 1), key='usuarioTxt', visible=True)], [sg.Input(key='user', size=(40, 1), visible=True)],
        [sg.Text('Senha:', size=(8, 1), key='senhaTxt')], [sg.Input(key='senha', password_char='*', size=(40, 1))],

        [sg.Text('Perfil:', key='linkTxt', visible=True)],
        [sg.Input(key='perfil', size=(40, 1), visible=True)],
        [sg.Text('Navegador:'),
         sg.Radio('Opera', 'navegador', key='opera', default=True),
         sg.Radio('Google Chrome', 'navegador', key='chrome')],
        [sg.Button('Enviar')]
    ]
    window_seguir = sg.Window('Seguir pessoas', layout)

    while True:
        eventos_seguir, valores_seguir = window_seguir.read()

        if eventos_seguir == sg.WINDOW_CLOSED:
            break

        if eventos_seguir == 'Enviar':
            window_seguir.close()
            janela_terminal(valores_seguir, 'seguir')
