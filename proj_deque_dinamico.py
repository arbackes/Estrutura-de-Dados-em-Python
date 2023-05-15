class NO:
    def __init__(self, valor):
        self.ant = None
        self.valor = valor
        self.prox = None
        
class DequeDin:
    def __init__(self):
        self.__inicio = None
        self.__final = None
        self.__qtd = 0

    def insere_inicio(self, valor):
        no = NO(valor)
        no.prox = self.__inicio
        if(self.__inicio == None):
            self.__final = no
        else:
            self.__inicio.ant = no

        self.__inicio = no
        self.__qtd = self.__qtd + 1
        return True
    
    def insere_final(self, valor):
        no = NO(valor)
        if(self.__final == None):
            self.__inicio = no
        else:
            no.ant = self.__final
            self.__final.prox = no

        self.__final = no
        self.__qtd = self.__qtd + 1
        return True
    
    def remove_inicio(self):
        if(self.__inicio == None):
            return False

        no = self.__inicio
        self.__inicio = self.__inicio.prox
        if(self.__inicio == None):
            self.__final = None
        else:
            self.__inicio.ant = None

        self.__qtd = self.__qtd - 1
        return True

    def remove_final(self):
        if(self.__inicio == None):
            return False

        no = self.__final
        if(self.__inicio == no): # remover o primeiro?
            self.__final = None
            self.__inicio = None
        else:
            no.ant.prox = None
            self.__final = no.ant

        self.__qtd = self.__qtd - 1
        return True
    
    def consulta_inicio(self):
        if(self.__inicio == None):
            return None
        else:
            return self.__inicio.valor

    def consulta_final(self):
        if(self.__final == None):
            return None
        else:
            return self.__final.valor
        
    def vazia(self):
        return (self.__inicio == None)

    def cheia(self):
        return False

    def tamanho(self):        
        return self.__qtd

    def print(self):
        i = 0
        no = self.__inicio
        while(no != None):
            print(i,") ",no.valor)
            i = i + 1
            no = no.prox

# ===================================================

pi = DequeDin()
print(pi.consulta_inicio())
print('-------------')
pi.insere_inicio(10)
pi.insere_final(40)
pi.insere_inicio(20)
pi.insere_final(30)
pi.print()

print('-------------')
print(pi.consulta_final())
print('-------------')

pi.remove_inicio()
pi.print()
print('-------------')
print(pi.consulta_inicio())
print('-------------')

pi.remove_final()
pi.print()


