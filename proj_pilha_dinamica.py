class NO:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
        
class PilhaDin:
    def __init__(self):
        self.__inicio = None

    def insere(self, valor):
        no = NO(valor)
        no.prox = self.__inicio
        self.__inicio = no        
        return True

    def remove(self):
        if(self.__inicio == None):
            return False

        no = self.__inicio
        self.__inicio = no.prox
        return True

    def consulta(self):
        if(self.__inicio == None):
            return None
        else:
            return self.__inicio.valor

    def vazia(self):
        return (self.__inicio == None)

    def cheia(self):
        return False


    def tamanho(self):
        qtd = 0
        no = self.__inicio
        while(no != None):
            qtd = qtd + 1
            no = no.prox

        return qtd
    
    def print(self):
        qtd = 0
        no = self.__inicio
        while(no != None):
            print(qtd,") ",no.valor)
            qtd = qtd + 1
            no = no.prox

# ===================================================

pi = PilhaDin()
print(pi.consulta())
print('-------------')
pi.insere(10)
pi.insere(40)
pi.insere(20)
pi.print()

print('-------------')
print(pi.consulta())
print('-------------')

pi.remove()
pi.print()
print('-------------')
print(pi.consulta())
print('-------------')


