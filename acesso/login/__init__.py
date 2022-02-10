from selenium.webdriver.common.keys import Keys
import time
import random
import acao


def login(user, senha, dados):
    driver = dados['driver']
    driver.get('https://www.instagram.com')
    time.sleep(random.random()+3)
    #usuário
    user_element = driver.find_element_by_xpath("//input[@name='username']")
    user_element.clear()
    acao.digitar(user, user_element)
    #senha
    password_element = driver.find_element_by_xpath("//input[@name='password']")
    password_element.clear()
    acao.digitar(senha, password_element)
    time.sleep(2)
    driver.find_element_by_css_selector('button.L3NKy').click()
    #password_element.send_keys(Keys.ENTER)
    time.sleep(random.random()+4)


def acessar(dados, link):
    driver = dados['driver']
    # Acessa a foto que é pra comentar
    driver.get(link)
