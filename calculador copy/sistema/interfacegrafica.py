from tkinter import  *
from tkinter.ttk import Treeview , Style
from threading import Thread
from time import sleep
from .copiarEcalular import *
from .historico import BancoDeDados
from keyboard import add_hotkey


#Inter face dele vai se bem simples.

class InterFaceGrafica():
    parar_animacao = esconder = False

    def __init__(self):
        self.Gui()


    def Gui(self): # interface grafica principal

        cor_botao = '#C5C5C5'

        self.janela = Tk()
        self.janela.title('ContaRápida')
        self.janela.config(bg = '#999999')
        self.janela.geometry('160x70')
        self.janela.resizable(width = False , height=False)
        self.icone = PhotoImage(file=r'sistema\imagem\icone.png')
        self.janela.iconphoto(False ,self.icone ) #imagem: https://br.freepik.com/search

        #botao de iniciar o script.
        self.botao_iniciar = Button(self.janela , width =13 , height= 1 , text = 'Rodar', font = 'Arial 12 bold' , relief = 'flat' , bg = cor_botao , command=self.Rodar_Script)
        self.botao_iniciar.place(x = 10 , y = 33)
        #imagem de: https://br.freepik.com/search
        imagem_help = PhotoImage(file=r'sistema\imagem\help.png')
        # imagem de: https://br.freepik.com/search
        imagem_historico = PhotoImage(file=r'sistema\imagem\historico.png')
        #imagem de https://br.freepik.com/search
        self.imagem_volta = PhotoImage(file=r'sistema\imagem\volta.png')

        #botao de historico onde irar fica os calcular ja feito, que terar os valores de hora de calulo e resultado
        self.botao_historico = Button(self.janela , width =18 , height = 0 , bg = '#999999' , relief='flat' , image=imagem_historico , command=self.Historico)
        self.botao_historico.place(x = 35 , y = 5)

        #Botao de help, que vai exbir um texto ensinando como usar o mesmo.
        self.botao_help = Button(self.janela , width=18 ,height=0 , bg = '#999999' ,  relief='flat' , image=imagem_help , command=self.Help)
        self.botao_help.place(x= 10 , y = 5)

        add_hotkey('alt+esc' , self.Esconder_Janela) # esconder janela
        
        self.janela.mainloop()

        
    def Rodar_Script(self): # funcao que irar criar os thread para a animacao e o proprio script
        self.animcao_thread = Thread(target=self.Animação)
        self.script_thread = Thread(target=self.CopiareCulcular)
        self.animcao_thread.start()
        self.script_thread.start()


    def CopiareCulcular(self):# responsavel por pegar a funcao de outro arquivo e dizer, quando ou que situação a animação deve parar.
        script = CopiarECopiar()
        if not self.parar_animacao:
            BancoDeDados().Fechar_banco()
            self.parar_animacao = True


    def Help(self):

        def voltar():
            self.janela.deiconify()
            janela_ajudar.destroy()

        self.janela.withdraw()

        janela_ajudar = Toplevel()
        janela_ajudar.title('Ajudar')
        janela_ajudar.config(bg = '#999999')
        janela_ajudar.iconphoto(False , self.icone)
        janela_ajudar.resizable(width = False , height=False)
        janela_ajudar.geometry('640x420')

        frame_titulo = Frame(janela_ajudar , width=650 , height=50 , bg = '#B5B5B5').place(x= 0 , y=0)

        Label_titulo = Label(janela_ajudar , width = 10 , height = 1 , text = 'Ajuda' , font='Arial 20 bold' , bg = '#B5B5B5' , fg = 'white' , anchor=W).place(x = 50 ,y = 10)
        
        #botao voltar para janela principal
        botao_volta = Button(janela_ajudar ,  relief='flat' ,bg = '#B5B5B5' ,image=self.imagem_volta , command=voltar)
        botao_volta.place(x= 10 , y= 10)

        texto = ''
        with open(r'sistema\Como usar.txt','r' , encoding='utf-8') as file:
            linhas = file.readlines()
            for linha in linhas:
                texto+=linha

        #texto de ajuda
        label_ajuda = Label(janela_ajudar , text = texto , anchor= 'w' ,font = 'arial 10 bold', bg = '#999999').place(x= 0 , y = 60)


    def Historico(self):

        def voltar():
            self.janela.deiconify()
            janela_historico.destroy()

        self.janela.withdraw()
        
        janela_historico = Toplevel()
        janela_historico.title('Historico de Calcular')
        janela_historico.config(bg = '#999999')
        janela_historico.resizable(width = False , height=False)
        janela_historico.iconphoto(False , self.icone)
        janela_historico.geometry('522x530')
        
        #Frame de titulo
        frame_titulo = Frame(janela_historico , width = 530 , height = 50 , bg ='#B5B5B5').place(x= 0 , y = 0)

        #Botao de voltar
        botao_voltar = Button(janela_historico , bg = '#B5B5B5' , image=self.imagem_volta , command=voltar ,relief='flat')
        botao_voltar.place(x= 10 , y = 10)

        #label titulo
        label_titulo = Label(janela_historico , width = 10 , height = 1 , text ='Historico' , bg = '#B5B5B5' , fg = 'white' , relief='flat' ,font = 'arial 20 bold' , anchor=W).place(x = 50 ,y = 10)

        #Tree view o visualizador do historico

        style = Style()
        style.configure('Treeview' ,  font = ('Arial' ,10 , 'bold' , ))
        style.configure('Treeview.Heading' , font = ('Arial' , 10 ,'bold'))

        tree = Treeview(janela_historico , columns=('Calculo','Resultado' ,'Hora','Data') ,show='headings')

        tree.column('Calculo',width = 150 , anchor=CENTER)
        tree.column('Resultado' , width= 80 , anchor=CENTER)
        tree.column('Hora',width = 100 , anchor=CENTER)
        tree.column('Data' , width= 100 , anchor=CENTER)

        tree.heading('Calculo' ,text='Calculo' , anchor=W)
        tree.heading('Resultado' , text='Resultado' , anchor=W)
        tree.heading('Hora' , text='Hora' , anchor=W)
        tree.heading('Data', text='Data' , anchor=W)

        tree.place(x = 10 , y= 70 , width=500 , height=450)

        for valores in BancoDeDados().puxar_dados():
            tree.insert(parent='', index='end',values=valores)

        tree.update()


    def Animação(self): # animacao de falso progresso...
        contador = 0
        self.botao_iniciar['state'] = 'disabled'
        try:    
            while True: # aqui fiz uma pequena animação bonito >>> feio
                if contador == 0:
                    self.botao_iniciar['text'] = 'Rodando'

                elif contador == 1:
                    self.botao_iniciar['text'] = 'Rodando.'

                elif contador == 2:
                    self.botao_iniciar['text'] = 'Rodando..'
                
                elif contador == 3:
                    contador = -1
                    self.botao_iniciar['text'] = 'Rodando...'

                if self.parar_animacao:
                    break

                self.botao_iniciar.update()
                sleep(0.5)
                contador += 1

            self.botao_iniciar['text'] = 'Parando...'
            sleep(2)
            self.botao_iniciar['state'] = 'normal'
            self.botao_iniciar.update()
            self.botao_iniciar['text'] = 'Rodar'
        except Exception as error:
            print(error)

    def Esconder_Janela(self):

        if not self.esconder:
            self.janela.withdraw()
            self.esconder = True

        else:
            self.janela.deiconify()
            self.esconder = False


if __name__ == '__main__':
    InterFaceGrafica()