import random
import time
from selenium.webdriver.common.keys import Keys
import acao.arquivo
from interface import terminal
names = []


def comentar(dados, frase, names):
    driver = dados['driver']

    if len(frase) > 0:
        frase += ' '
    try:
        for i in names:
            frase += f'@{i[:-1]} '

        comentario_element = driver.find_element_by_xpath("//textarea[@class='Ypffh']")
        comentario_element.click()
        time.sleep(random.randint(2, 5))
        comentario_element = driver.find_element_by_xpath("//textarea[@class='Ypffh focus-visible']")
        digitar(frase, comentario_element)
        comentario_element.send_keys(Keys.ENTER)
        time.sleep(random.randint(1, 2)+random.random())

    except Exception as e:
        print(f'Erro ao tentar comentar: {e}')
        time.sleep(5)
    terminal.Printar(f'Comentário: {frase}')


def pegarSegui(dados, user, seguiQt, bSegui):
    global names
    driver = dados['driver']
    link = ''
    user = 'nilmoretto'

    if bSegui:
        link = '/followers/'
    else:
        link = '/following/'

    #Acessa o meu perfil
    driver.get('https://www.instagram.com/' + user + '/')
    time.sleep(random.random()+3)

    #Localiza e clica no botão de seguidores
    seguidores_element = driver.find_element_by_xpath("//a[@href='/" + user + link + "']")
    seguidores_element.click()
    time.sleep(random.random()+2)

    #Rola a tela para baixo
    diferenca_percent = 0
    while len(names) < seguiQt:
        names = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")

        percent = (len(names) * 100) / seguiQt
        qt_tracos = int(0.6 * percent) - diferenca_percent
        diferenca_percent += qt_tracos

        print('-' * qt_tracos, end="")

        driver.execute_script("window.document.getElementsByClassName('isgrP')[0].scrollBy(0,100)")
        time.sleep(random.random()+0.2)
    print('|\n')
    #Coloca os seguidores em uma lista

    pic_names = [elem.get_attribute('href')[26:-1] for elem in names]

    return pic_names


def digitar(frase, onde_digitar):
    for letra in frase:
        onde_digitar.send_keys(letra)
        time.sleep(random.randint(2, 5)/30)


def recomecar(dados, link, seguiQt, bSegui, user, senha):
    # Pega o link e a quantidade de seguidores caso esteja recomeçando
    seguidores = pegarSegui(dados, user, seguiQt, bSegui)
    seguidores.append(link)
    seguidores.append(user)
    seguidores.append(senha)
    f = arquivo.abrir()
    arquivo.guardarSegui(f, seguidores)


def disfarce(dados):
    driver = dados['driver']

    driver.get('https://www.instagram.com/')
    time.sleep(random.randint(1, 2)+random.random())
    for i in range(1, random.randint(20, 30)):
        driver.execute_script("window.document.getElementsByClassName('sDN5V')[0].scrollBy(0,100)")
        time.sleep(random.randint(0, 2)+random.random())
    #likes = driver.find_elements_by_xpath("//a[@class='wpO6b  ']")


def seguir_perfis(dados, perfil):
    driver = dados['driver']

    #acessa perfil
    driver.get(f'https://www.instagram.com/{perfil}/')
    try:
        btn_seguindo = driver.find_elements_by_css_selector(".-nal3  .g47SY ")[2]
    except:
        print('Não encontrou o botão "Seguindo"')
    else:
        qt_seguindo = int(btn_seguindo.text)
        btn_seguindo.click()
        time.sleep(4)
        print(len(driver.find_elements_by_css_selector('div.Pkbci button.L3NKy')))

