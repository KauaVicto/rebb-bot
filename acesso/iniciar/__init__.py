from selenium import webdriver

def inic(nav):
    dados = {}
    try:
        if nav:
            dados['driver'] = webdriver.Opera()
        else:
            dados['driver'] = webdriver.Chrome()
        dados['driver'].get('https://www.google.com')
    except Exception as erro:
        print(f'Erro salvar o driver: {erro}')
    return dados
