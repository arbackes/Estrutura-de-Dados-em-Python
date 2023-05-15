class NO:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
        
class FilaDin:
    def __init__(self):
        self.__inicio = None
        self.__final = None

    def insere(self, valor):
        no = NO(valor)
        if(self.__final == None):
            self.__inicio = no
        else:
            self.__final.prox = no

        self.__final = no
        return True
    
    def remove(self):
        if(self.__inicio == None):
            return False

        no = self.__inicio
        self.__inicio = no.prox
        if(self.__inicio == None):
            self.__final = None
            
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

pi = FilaDin()
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


