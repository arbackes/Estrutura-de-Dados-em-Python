import copy
import math

class NO:
    def __init__(self,info):
        self.info = info
        self.esq = None
        self.dir = None
        
class ArvBin:
    def __init__(self):
        self.__raiz = None

    def vazia(self):
        if(self.__raiz == None):
            return True
        else:
            return False

    def totalNO(self):
        if(self.__raiz == None):
            return 0
        else:
            return self._totalNO(self.__raiz)

    def _totalNO(self, raiz):
        if(raiz == None):
            return 0
        
        total_esq = self._totalNO(raiz.esq)
        total_dir = self._totalNO(raiz.dir)
        return (total_esq + total_dir + 1)

    def altura(self):
        if(self.__raiz == None):
            return 0
        else:
            return self.__altura(self.__raiz)

    def __altura(self, raiz):
        if(raiz == None):
            return 0
        
        alt_esq = self.__altura(raiz.esq)
        alt_dir = self.__altura(raiz.dir)
        if(alt_esq > alt_dir):
            return alt_esq + 1
        else:
            return alt_dir + 1
    
    def insere(self, valor):
        novo = NO(valor)        

        if(self.__raiz == None):
            self.__raiz = novo
        else:
            atual = self.__raiz
            ant = None
            while(atual != None):
                ant = atual
                if(valor == atual.info):
                    return False # elemento já existe

                if(valor > atual.info):
                    atual = atual.dir
                else:
                    atual = atual.esq
            
            if(valor > ant.info):
                ant.dir = novo
            else:
                ant.esq = novo
        
        return True

    def busca(self, valor):
        if(self.__raiz == None):
            return False

        atual = self.__raiz
        while(atual != None):
            if(valor == atual.info):
                return True
            
            if(valor > atual.info):
                atual = atual.dir
            else:
                atual = atual.esq
        
        return False
    

    def remove(self, valor):
        if(self.__raiz == None):
            return False
        
        ant = None
        atual = self.__raiz
        while(atual != None):
            if(valor == atual.info):
                if(atual == self.__raiz):
                    self.__raiz = self.__remove_atual(atual)
                else:
                    if(ant.dir == atual):
                        ant.dir = self.__remove_atual(atual)
                    else:
                        ant.esq = self.__remove_atual(atual)
                
                return True
            
            ant = atual
            if(valor > atual.info):
                atual = atual.dir
            else:
                atual = atual.esq
        
        return False
    
    def __remove_atual(self, atual):

        if(atual.esq == None):
            return atual.dir
        
        no1 = atual
        no2 = atual.esq
        while(no2.dir != None):
            no1 = no2
            no2 = no2.dir
        
        # no2 é o nó anterior a r na ordem e-r-d
        # no1 é o pai de no2
        if(no1 != atual):
            no1.dir = no2.esq
            no2.esq = atual.esq
        
        no2.dir = atual.dir
        return no2

    def __preOrdem(self,raiz):
        if(raiz != None):
            print(raiz.info)
            self.__preOrdem(raiz.esq)
            self.__preOrdem(raiz.dir)

    def preOrdem(self):
        if(self.__raiz != None):
            self.__preOrdem(self.__raiz)

    def __emOrdem(self,raiz):
        if(raiz != None):            
            self.__emOrdem(raiz.esq)
            print(raiz.info)
            self.__emOrdem(raiz.dir)

    def emOrdem(self):
        if(self.__raiz != None):
            self.__emOrdem(self.__raiz)
        
    def __posOrdem(self,raiz):
        if(raiz != None):            
            self.__posOrdem(raiz.esq)            
            self.__posOrdem(raiz.dir)
            print(raiz.info)

    def posOrdem(self):
        if(self.__raiz != None):
            self.__posOrdem(self.__raiz)
        
    

arv = ArvBin()
print(arv.altura())

arv.insere(50)
arv.insere(100)
arv.insere(30)
arv.insere(20)
arv.insere(40)
arv.insere(45)
arv.insere(35)
arv.insere(37)

print(arv.altura())
#arv.preOrdem()
#arv.emOrdem()
#arv.posOrdem()

print("busca: ",arv.busca(41))
arv.remove(40)
arv.remove(100)
arv.remove(10)
arv.emOrdem()
