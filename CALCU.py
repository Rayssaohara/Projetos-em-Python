class calculadora:
    def __init__(self,n1, n2):
        self.a = n1
        self.b = n2

    def raiz(self):
        return self.a ** 0.5

    def quad(self):
        return self.a ** 2

    def subtracao (self):
        return self.a - self.b

    def multiplicacao (self):
        return self.a * self.b

    def soma (self):
        return self.a + self.b

    def divisao (self):
        return self.a / self.b

cal = calculadora(1,1)
print('Digito o primeiro numero')
cal.a = int(input())
lista_cal = []
ope = 0
while( ope != 9):

    print('\no atual numero é: ' + str(cal.a))

    print('\ndigite 1 para somar')
    print('digite 2 para subtrair')
    print('digita 3 para multiplicar')
    print('digite 4 para dividir')
    print('digite 5 para raiz quadrada')
    print('digite 6 para elevar ao quadrado')
    print('digite 7 para limpar e adicionar outro numero')
    print('digite 8 para historico')
    print('digite 9 para sair')


    ope = int(input())
    if (ope == 1):
        print('digite o segundo numero')
        cal.b = int(input())
        resultado = cal.soma()
        print('o resultado é: ' + str(resultado))
        lista_cal.append( str(cal.a) + " + " + str(cal.b) + " = " + str(resultado))
        cal.a = resultado
    elif(ope == 2):
        print('digite o segundo numero')
        cal.b = int(input())
        resultado = cal.subtracao()
        print('o resultado é: ' + str(resultado))
        lista_cal.append(str(cal.a) + " - " + str(cal.b) + " = " + str(resultado))
        cal.a = resultado
    elif( ope == 3):
        print('digite o segundo numero')
        cal.b = int(input())
        resultado = cal.multiplicacao()
        print('o resultado é: ' + str(resultado))
        lista_cal.append(str(cal.a) + " * " + str(cal.b) + " = " + str(resultado))
        cal.a = resultado
    elif(ope == 4):
        print('digite o segundo numero')
        cal.b = int(input())
        resultado = cal.divisao()
        print('o resultado é: ' + str(resultado))
        lista_cal.append(str(cal.a) + " / " + str(cal.b) + " = " + str(resultado))
        cal.a = resultado
    elif(ope ==5):
        resultado= cal.raiz()
        print('o resultado é: ' + str(resultado))
        lista_cal.append('raiz quadrada de ' + str(cal.a)  +' = ' + str(resultado))
        cal.a = resultado
    elif(ope == 6):
        resultado = cal.quad()
        print('o resultado é: ' + str(resultado))
        lista_cal.append(str(cal.a) + ' elevado a 2 = ' + str(resultado))
        cal.a = resultado
    elif(ope ==7):
        print('preencha com um novo numero')
        cal.a = int(input())
    elif(ope == 8):
        for a in lista_cal:
            print(a)
    elif( ope == 9):
        print('ok')
    else:
        print('valor errado')
print('programa encerrado')




