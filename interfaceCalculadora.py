from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "16")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 5
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 5
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quarto_1Container = Frame(master)
        self.quarto_1Container["pady"] = 20
        self.quarto_1Container.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="calculadora")
        self.titulo["font"] = ("Arial", "16", "bold")
        self.titulo.pack()

        self.numero_aLabel = Label(self.segundoContainer,text="Primeiro numero", font=self.fontePadrao)
        self.numero_aLabel.pack(side=LEFT)

        self.numero_a = Entry(self.segundoContainer)
        self.numero_a["width"] = 15
        self.numero_a["font"] = self.fontePadrao
        self.numero_a.pack(side=LEFT)

        self.numero_bLabel = Label(self.terceiroContainer, text="Segundo numero", font=self.fontePadrao)
        self.numero_bLabel.pack(side=LEFT)

        self.numero_b = Entry(self.terceiroContainer)
        self.numero_b["width"] = 15
        self.numero_b["font"] = self.fontePadrao
        self.numero_b.pack(side=LEFT)

        self.executar = Button(self.quartoContainer)
        self.executar["text"] = "somar +"
        self.executar["font"] = ("Calibri", "12")
        self.executar["width"] = 12
        self.executar["command"] = self.soma
        self.executar.pack(side=LEFT)

        self.executar = Button(self.quartoContainer)
        self.executar["text"] = "subtrair -"
        self.executar["font"] = ("Calibri", "12")
        self.executar["width"] = 12
        self.executar["command"] = self.subtracao
        self.executar.pack(side=LEFT)

        self.executar = Button(self.quartoContainer)
        self.executar["text"] = "multiplicar *"
        self.executar["font"] = ("Calibri", "12")
        self.executar["width"] = 12
        self.executar["command"] = self.multiplicacao
        self.executar.pack(side=LEFT)

        self.executar = Button(self.quartoContainer)
        self.executar["text"] = "dividir /"
        self.executar["font"] = ("Calibri", "12")
        self.executar["width"] = 12
        self.executar["command"] = self.divisao
        self.executar.pack(side=LEFT)

        self.executar = Button(self.quarto_1Container)
        self.executar["text"] = "raiz quadrada √"
        self.executar["font"] = ("Calibri", "12")
        self.executar["width"] = 12
        self.executar["command"] = self.raiz
        self.executar.pack(side=LEFT)

        self.executar = Button(self.quarto_1Container)
        self.executar["text"] = "elevado ao quadrado"
        self.executar["font"] = ("Calibri", "12")
        self.executar["width"] = 16
        self.executar["command"] = self.quadrado
        self.executar.pack(side=LEFT)

        self.executar = Button(self.quarto_1Container)
        self.executar["text"] = "histórico de operações"
        self.executar["font"] = ("Calibri", "12")
        self.executar["width"] = 16
        self.executar["command"] = self.gravar
        self.executar.pack(side=LEFT)

        self.executar = Button(self.quarto_1Container)
        self.executar["text"] = "esconder histórico"
        self.executar["font"] = ("Calibri", "12")
        self.executar["width"] = 14
        self.executar["command"] = self.apagar
        self.executar.pack(side=LEFT)

        self.mensagem = Label(self.quintoContainer, text="O resultado é:", font=self.fontePadrao, background= "#ff9999")
        self.mensagem.pack(side= TOP)

        self.historico = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.historico.pack(side= TOP)  

       

        self.lista = []

    

    #Método executar operações
    
        

    def soma(self):
        a = self.numero_a.get()
        b = self.numero_b.get()
        num = int(a) + int(b)
        self.mensagem['text'] = num
        self.lista.append( str(a) + " + " + str(b) + " = " + str(num))
    
    def subtracao(self):
        a = self.numero_a.get()
        b = self.numero_b.get()
        num = int(a) - int(b)
        self.mensagem['text'] = num
        self.lista.append( str(a) + " - " + str(b) + " = " + str(num))
    
    def multiplicacao(self):
        a = self.numero_a.get()
        b = self.numero_b.get()
        num = int(a) * int(b)
        self.mensagem['text'] = num
        self.lista.append( str(a) + " * " + str(b) + " = " + str(num))
    
    def divisao(self):
        a = self.numero_a.get()
        b = self.numero_b.get()
        num = int(a) / int(b)
        self.mensagem['text'] = num
        self.lista.append( str(a) + " / " + str(b) + " = " + str(num))
    
    def raiz(self):
        a = self.numero_a.get()
        num = int(a) ** 0.5
        self.mensagem['text'] = num
        self.lista.append("raiz quadrada de " + str(a) + " = " + str(num))
    
    def quadrado(self):
        a = self.numero_a.get()
        num = int(a) ** 2
        self.mensagem['text'] = num
        self.lista.append(str(a) + " elevado ao quadrado = " + str(num))
        


    def gravar(self):
        gravado = self.lista
        self.historico['text'] = gravado

    def apagar(self):
        self.historico ['text'] = ""

#comentario2       

root = Tk()
Application(root)
root.mainloop()
