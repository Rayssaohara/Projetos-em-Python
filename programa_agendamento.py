def criar_agendamento():
    agend = agendamento('-', 1, 1, 1,
                        '-')  # as variaveis representam o nome como str, o dia o mes e a hora como inteiros e a cond. booleana de V ou F para o convenio
    print('Olá. Você começou a fazer um agendamento. Por favor digite o nome do paciente.')
    agend.nome = input()
    #while(agend.nome ):
        #print('valor invalido')
        #agend.nome = input()
    while(True):
        try:
            print('Digite o dia')
            agend.dia = int(input())
            while(agend.dia <1 or agend.dia>31):
                print('Valor invalido')
                agend.dia = int(input())
        except ValueError: print(' Erro de valor inserido.')
        else: break

    while(True):
        try:
            print('mês')
            agend.mes = int(input())
            while(agend.mes<1 or agend.mes > 12):
                print('Valor errado')
                agend.mes = int(input())
        except ValueError:
            print('Erro de valor inserido')
        else: break
    while(True):
        try:
            print('horário')
            agend.hora = int(input())
            while(agend.hora < 8 or agend.hora > 17):
                print('horario invalido')
                agend.hora = int(input())
        except ValueError:
            print('Erro de valor inserido')
        else: break

    print('Digite S para Convênio ou Digite N para particular')
    agend.convenio = input()
    while(agend.convenio != "S" and agend.convenio != "N"):
        print("Opcao incorreta, tente de novo")
        agend.convenio = input()
    return agend

def buscar_agendamento1(lista):
        print('Digite o dia do agendamento')
        dia = int(input())
        print('Digite o mês')
        mes = int(input())
        print('Digite a hora')
        hora = int(input())
        for a in lista:
            if (a.dia == dia and a.mes == mes and a.hora == hora):
                return a


def buscar_agendamento(lista):

        print('Digite o nome do paciente')
        nome = input()
        for a in lista:
            if (a.nome == nome):
                return a




class agendamento:
    def __init__(self, nome, dia, mes, hora, convenio):
        self.nome = nome
        self.dia = dia
        self.mes = mes
        self.hora = hora
        self.convenio = convenio

    def exibir(self):
        print("\nA paciente:" + self.nome + ".")
        print("Sua consulta está marcada para o dia: " + str(self.dia) + '/' + str(self.mes) + ", às " + str(
            self.hora) + " horas")
        if (self.convenio == 'S'): print('Consulta via covenio\n')
        else: print("Consulta particular\n")




lista_de_agendamentos = []


opcao = 0
while (opcao != 5):
    print("ola. Escolha as opções abaixo")
    print("1 para incluir agendamento")
    print("2 para mostrar todos os agendamentos")
    print('3 Excluir agendamento')
    print('4 buscar agendamento')
    print("5 para sair do programa")

    opcao = int(input())
    if (opcao == 1):
        #impedir agendamentos duplicados
        lista_de_agendamentos.append(criar_agendamento())
    elif (opcao == 2):
        for a in lista_de_agendamentos:
            a.exibir()
    elif (opcao == 3):
        try:
            excluir = buscar_agendamento1(lista_de_agendamentos)
            lista_de_agendamentos.remove(excluir)
            print("\nItem excluido com sucesso!\n")
        except ValueError:
            print('\nValor não encontrado\n')
    elif (opcao == 4):
        try:
            buscar = buscar_agendamento(lista_de_agendamentos)
            buscar.exibir()
        except AttributeError:
            print('Valor incorreto')
    elif (opcao == 5):
        print("ok")
    else:
        print("não entendi oque você quer dizer")
print("programa encerrado")
