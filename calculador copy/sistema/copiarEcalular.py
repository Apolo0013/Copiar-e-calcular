'''
Este projeto pessoal faz nada mais nada menos doque fazer uma conta so copiando uma conta e ele retorna ja calculador
'''
import pyperclip # responvael pela parte de colar e copiar
from keyboard import add_hotkey , press ,wait# responsavel pela parte de atalho ex: ctrl + x da  vai exercutar tal funcao
from numexpr import evaluate
from plyer import notification
from .historico import BancoDeDados
from time import sleep



#como usar-lo. basta copiar primeiro a conta e depois pressionar (ctrl + y), que a conta ja vai ter feita, no caso a conta esta copiada é so da ctrl+v, e para finalizar o script ctrl+u.
class CopiarECopiar():
    def __init__(self):
        self.script()


    def Dispara_notificação(self , Nome , titulo , conteudo ):
        notification.notify(
            title = titulo,
            app_name = Nome,
            message = conteudo,
            timeout = 1,
            app_icon = r'sistema\imagem\icone.ico'
            )


    def script(self):# Essa funcao vai copiar e calculo e depois retorna o resultado da conta, como se voce tivesse da ctrl + c em uma conta e ao mesmo tempo o seu sistema tem copiado o resultado sei fodase
        def copiarEcalcular():
            try:
                calculo = pyperclip.paste() # Responvel por copiar a conta
                resultado = evaluate(calculo.strip().replace('÷','/').replace('x','*')) # aqui nois pegar a funcao do python 'eval' ele praticamente faz a conta sozinho, so dei uma tratada nele para tirar os espaços e cambal
                resultado = str(resultado)
                
                if '.' in resultado:
                    resultado = float(resultado)
                
            except Exception: # caso tenha uma 'chugeira' ex: a conta: 2+2x2. O script nao vai reconhece o 'conta' como numero
                self.Dispara_notificação(Nome='Erro em calcular.',
                                        titulo='Aviso' ,
                                        conteudo='Algo deu errado tente novamente.'
                                        )
            else:
                calculo = calculo.replace('*','x').replace('/','÷')
                resultado = str(f'{resultado}').replace('.',',')
                self.Dispara_notificação(Nome='Calculo' , titulo='Aviso' , conteudo=f'{calculo} = {resultado}')
                sleep(2)
                self.Dispara_notificação(Nome='Calculo' , titulo='Aviso' , conteudo='Resultado copiado!!!')
                #add_dados_thread.join()
                BancoDeDados().add_threadDados(calculo=calculo , resultado=resultado)
                return pyperclip.copy(resultado) # aqui retonamos a conta..


        add_hotkey('ctrl+y' , copiarEcalcular) # se o usuario fazer essa conbinação ele exercuta
        self.Dispara_notificação(Nome='Aviso',titulo='Como usar',conteudo='Para fazer conta: `crtl+y`')
        sleep(3)
        self.Dispara_notificação(Nome='Aviso',titulo='Como usar',conteudo='Para fechar script: `esc+u`')
        print('script inicializador...')

        wait('esc+u')
        self.Dispara_notificação(Nome='Parando...',titulo='Aviso.' , conteudo='Script parando...')
        return False


if __name__ == '__main__':
    CopiarECopiar()
    

