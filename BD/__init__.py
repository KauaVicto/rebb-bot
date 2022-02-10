from multiprocessing import connection
import mysql.connector


class Usuario:

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="", database="bot_pix")
        except:
            print('Não conectou ao banco')
    
    def verificar_usuario(self):
        try:
            sql = "SELECT * FROM usuario WHERE nome = %s LIMIT 1"
            values = [self.nome]
            cursor = self.con.cursor()
            cursor.execute(sql, values)

            result = cursor.fetchall()

            if cursor.rowcount == 1:
                pass
        except:
            print('erro na consulta')
            
                


user = Usuario('laylinha', 'senha')
user.verificar_usuario()