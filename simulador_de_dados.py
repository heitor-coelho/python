#simudalor  de dado
#simular o uso de um dado, gerando um valor de um até 6 
import random


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Você gostaria de gerar um novo valor ?"

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == "sim" or resposta == 's':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Agradecemos sua participação.')
            else:
                print('favor, digitar sim ou não.')
        except:
            print('Ocorreu um erro ao tentar isso.')



simulador = SimuladorDeDado()
simulador.Iniciar()

