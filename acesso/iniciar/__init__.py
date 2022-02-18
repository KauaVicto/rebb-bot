from selenium import webdriver
import os

def inic(nav, login):
    dados = {}
    try:
        if nav:
            dados['driver'] = webdriver.Opera()
        else:
            dir_path = os.getcwd()
            profile = os.path.join(dir_path, "profile", login)
            options = webdriver.ChromeOptions()
            options.add_argument(
                r"user-data-dir={}".format(profile))

            dados['driver'] = webdriver.Chrome("./chromedriver.exe", chrome_options=options)
        dados['driver'].get('https://www.google.com')
    except Exception as erro:
        print(f'Erro salvar o driver: {erro}')
    return dados
