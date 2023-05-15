class NO:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
        
class ListaDinCirc:
    def __init__(self):
        self.__final = None
	
    def insere_final(self, valor):
        no = NO(valor)
        if(self.__final == None):
            self.__final = no
            no.prox = no
        else:
            no.prox = self.__final.prox
            self.__final.prox = no
            self.__final = no
            
        return True
	    
    def insere_inicio(self, valor):
        no = NO(valor)
        if(self.__final == None):
            self.__final = no
            no.prox = no
        else:
            no.prox = self.__final.prox
            self.__final.prox = no
            
        return True

    def insere_ordenado(self, valor):
        no = NO(valor)
        if(self.__final == None):
            self.__final = no
            no.prox = no
        else:
            if(self.__final.valor <= valor): #insere final
                no.prox = self.__final.prox
                self.__final.prox = no
                self.__final = no
            else:
                ant = self.__final
                atual = self.__final.prox
                while(atual != self.__final and atual.valor < valor):
                    ant = atual
                    atual = atual.prox

                ant.prox = no
                no.prox = atual
                    
        return True

    def remove_final(self):
        if(self.__final == None):
            return False

        if(self.__final == self.__final.prox):# lista fica vazia
            self.__final = None
        else:
            ant = self.__final
            while(ant.prox != self.__final):#procura o penúltimo
                ant = ant.prox

            ant.prox = self.__final.prox
            self.__final = ant

        return True

    def remove_inicio(self):
        if(self.__final == None):
            return False

        if(self.__final == self.__final.prox):# lista fica vazia
            self.__final = None
        else:
            no = self.__final.prox
            self.__final.prox = no.prox

        return True

    def remove_valor(self, valor):
        if(self.__final == None):
            return False

        no = self.__final
        if(no.valor == valor):# remover do final
            if(no == no.prox):# lista fica vazia
                self.__final = None
            else:
                ant = self.__final
                while(ant.prox != self.__final):#procura o penúltimo
                    ant = ant.prox

                ant.prox = self.__final.prox
                self.__final = ant  
        else:
            ant = no
            no = no.prox
            while(no != self.__final and no.valor != valor):
                ant = no
                no = no.prox

            if(no == self.__final):#não encontrado
                return False

            ant.prox = no.prox
            
        return True

    def consulta(self,valor):
        if(self.__final == None):
            return None

        no = self.__final
        while(no.prox != self.__final and no.valor != valor):
            no = no.prox

        if(no.valor != valor):
            return False
        else:
            return True        
        
    def vazia(self):
        return (self.__final == None)        

    def cheia(self):
        return False

    def tamanho(self):        
        qtd = 0
        no = self.__final
        while(True):
            qtd = qtd + 1
            no = no.prox
            if(no == self.__final):
                break

        return qtd

    def print(self):
        if(self.__final == None):
            return
        
        qtd = 0
        ant = None
        no = self.__final.prox
        while(ant != self.__final):
            print(qtd,") ",no.valor)
            qtd = qtd + 1
            ant = no
            no = no.prox
            #if(no == self.__final):
            #    break
            
# ===================================================

V = [10, 40, 20, 51, -5]

pi = ListaDinCirc()
print(pi.consulta(20))
print('-------------')
for v in V:
    #pi.insere_ordenado(v)
    #pi.insere_inicio(v)
    pi.insere_final(v)
pi.print()
print('tamanho: ',pi.tamanho())

print('-------------')
print(pi.consulta(20))
print(pi.consulta(120))
print('-------------')

pi.remove_valor(20)
#pi.remove_inicio()
#pi.remove_final()
pi.print()
print('-------------')
print(pi.consulta(40))
print('-------------')


