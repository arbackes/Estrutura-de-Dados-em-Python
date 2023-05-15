class NO:
    def __init__(self, valor):
        self.valor = valor
        self.ant = None
        self.prox = None
        
class ListaDinDupla:
    def __init__(self):
        self.__inicio = None

    def insere_final(self, valor):
        no = NO(valor)        
        if(self.__inicio == None):#lista vazia: insere início
            self.__inicio = no
        else:
            aux = self.__inicio
            while(aux.prox != None):
                aux = aux.prox

            aux.prox = no
            no.ant = aux
        return True

    def insere_inicio(self, valor):
        no = NO(valor)
        no.prox = self.__inicio

        if(self.__inicio != None):
            self.__inicio.ant = no
        
        self.__inicio = no
        return True

    def insere_ordenado(self, valor):
        no = NO(valor)
        if(self.__inicio == None):#lista vazia: insere início
            self.__inicio = no
        else:
            anterior = None
            atual = self.__inicio
            while(atual != None and atual.valor < valor):
                anterior = atual
                atual = atual.prox

            if(atual == self.__inicio):
                self.__inicio.ant = no
                no.prox = self.__inicio
                self.__inicio = no
            else:
                no.prox = anterior.prox
                no.ant = anterior
                anterior.prox = no
                if(atual != None):
                    atual.ant = no
                
        return True

    def remove_final(self):
        if(self.__inicio == None):
            return False

        no = self.__inicio
        while(no.prox != None):
            no = no.prox

        if(no.ant == None):
            self.__inicio = no.prox
        else:
            no.ant.prox = None

        return True

    def remove_inicio(self):
        if(self.__inicio == None):
            return False

        no = self.__inicio
        self.__inicio = no.prox
        if(no.prox != None):
            no.prox.ant = None
            
        return True

    def remove_valor(self,valor):
        if(self.__inicio == None):
            return False

        no = self.__inicio
        while(no != None and no.valor != valor):
            no = no.prox

        if(no == None):
            return False

        if(no.ant == None):
            self.__inicio = no.prox
        else:
            no.ant.prox = no.prox
            
        if(no.prox != None):
            no.prox.ant = no.ant

        return True

    def consulta(self,valor):
        if(self.__inicio == None):
            return None

        no = self.__inicio
        while(no != None and no.valor != valor):
            no = no.prox

        if(no == None):
            return False
        else:
            return True        

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

V = [10, 40, 20, 51, -5]

pi = ListaDinDupla()
print(pi.consulta(20))
print('-------------')
for v in V:
    #pi.insere_ordenado(v)
    #pi.insere_inicio(v)
    pi.insere_final(v)
pi.print()

print('-------------')
print(pi.consulta(20))
print(pi.consulta(120))
print('-------------')

#pi.remove_valor(20)
#pi.remove_inicio()
#pi.remove_final()
pi.print()
print('-------------')
print(pi.consulta(40))
print('-------------')


