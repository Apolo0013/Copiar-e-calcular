import sqlite3
import time
from threading import Thread


class BancoDeDados():
    #responsavel por add os dados no banco
    def add_dados(self , calculo , resultado):
        self.Abrindo_banco()

        # Obter a hora local como uma estrutura struct_time
        hora_local = time.localtime()

        # Formatar hora, minutos e data
        hora_atual = time.strftime("%H:%M", hora_local)
        data_atual = time.strftime("%d/%m/%Y", hora_local)
        try:#adicionando dados no banco de dados pae
            self.cursor.execute(f'INSERT INTO historico VALUES ("{calculo}","{resultado}","{hora_atual}","{data_atual}")')
        except Exception as error:
            print('algo deu errado', error)
        else:
            self.banco.commit()


    def add_threadDados(self , calculo , resultado):#adicionar a conta na log
        add_dados_thread = Thread(target=self.add_dados , args=(calculo , resultado))
        add_dados_thread.start()
        add_dados_thread.join()


    def puxar_dados(self): # puxar a logs
        self.Abrindo_banco()
        try:
            self.cursor.execute('SELECT  * FROM historico')
            return self.cursor.fetchall()
        except Exception as error:
            print(error)
        else:
            self.Fechar_banco()


    def Abrindo_banco(self):


        self.banco = sqlite3.connect('Dados.db')

        self.cursor = self.banco.cursor()

        self.cursor.execute('CREATE TABLE IF NOT EXISTS historico (conta text , resultado integer , horario text , data text)')

        #banco.close()

    
    def Fechar_banco(self):
        self.banco.close()

if __name__ == '__main__':
    print(BancoDeDados().puxar_dados())