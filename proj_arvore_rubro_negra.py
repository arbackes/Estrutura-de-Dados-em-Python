import copy
import math

RED = True
BLACK = False

class NO:
    def __init__(self,info):
        self.info = info
        self.cor = RED
        self.esq = None
        self.dir = None    
        
class ArvLLRB:
    def __init__(self):
        self.__raiz = None

    def _cor(self, H):
        if(H == None):
            return BLACK
        else:
            return H.cor

    def _trocaCor(self,H):
        H.cor = not H.cor
        if(H.esq != None):
            H.esq.cor = not H.esq.cor

        if(H.dir != None):
            H.dir.cor = not H.dir.cor

    def _rotacionaEsquerda(self, A):
        B = A.dir
        A.dir = B.esq
        B.esq = A
        B.cor = A.cor
        A.cor = RED
        return B

    def _rotacionaDireita(self, A):
        B = A.esq
        A.esq = B.dir
        B.dir = A
        B.cor = A.cor
        A.cor = RED
        return B

    def _move2EsqRED(self, H):
        self._trocaCor(H)
        if(self._cor(H.dir.esq) == RED):
            H.dir = self._rotacionaDireita(H.dir)
            H = self._rotacionaEsquerda(H)
            self._trocaCor(H)
    
        return H

    def _move2DirRED(self, H):
        self._trocaCor(H)
        if(self._cor(H.esq.esq) == RED):
            H = self._rotacionaDireita(H)
            self._trocaCor(H)
    
        return H

    def _balancear(self, H):
        # nó Vermelho é sempre filho à esquerda
        if(self._cor(H.dir) == RED):
            H = self._rotacionaEsquerda(H)

        # Filho da esquerda e neto da esquerda são vermelhos
        if(H.esq != None and self._cor(H.esq) == RED and self._cor(H.esq.esq) == RED):
            H = self._rotacionaDireita(H)

        # 2 filhos Vermelhos: troca cor!
        if(self._cor(H.esq) == RED and self._cor(H.dir) == RED):
            self._trocaCor(H)

        return H


    def _insereNO(self, H, valor):
        if(H == None):# árvore vazia ou nó folha
            novo = NO(valor)
            return novo
        else:
            if(valor < H.info):
                H.esq = self._insereNO(H.esq,valor)
            else:
                H.dir = self._insereNO(H.dir,valor)

            # nó Vermelho é sempre filho à esquerda
            if(self._cor(H.dir) == RED and self._cor(H.esq) == BLACK):
                H = self._rotacionaEsquerda(H)

            # Filho e Neto são vermelhos
            # Filho vira pai de 2 nós vermelhos
            if(self._cor(H.esq) == RED and self._cor(H.esq.esq) == RED):
                H = self._rotacionaDireita(H)

            # 2 filhos Vermelhos: troca cor!
            if(self._cor(H.esq) == RED and self._cor(H.dir) == RED):
                self._trocaCor(H)

            return H
    
    def insere(self, valor):
        if(self.busca(valor)):
            return False #valor já existe na árvore
        else:
            self.__raiz = self._insereNO(self.__raiz, valor)
            self.__raiz.cor = BLACK
            return True

    def _removerMenor(self, H):
        if(H.esq == None):
            return None

        if(self._cor(H.esq) == BLACK and self._cor(H.esq.esq) == BLACK):
            H = self._move2EsqRED(H)

        H.esq = self._removerMenor(H.esq)
        return self._balancear(H)

    def _procuraMenor(self, atual):
        no1 = atual
        no2 = atual.esq
        while(no2 != None):
            no1 = no2
            no2 = no2.esq

        return no1

    def _removeNO(self, H, valor):
        if(valor < H.info):
            if(self._cor(H.esq) == BLACK and self._cor(H.esq.esq) == BLACK):
                H = self._move2EsqRED(H)

            H.esq = self._removeNO(H.esq, valor)
        else:
            if(self._cor(H.esq) == RED):
                H = self._rotacionaDireita(H)

            if(valor == H.info and (H.dir == None)):
                return None
            
            if(self._cor(H.dir) == BLACK and self._cor(H.dir.esq) == BLACK):
                H = self._move2DirRED(H)

            if(valor == H.info):
                menor = self._procuraMenor(H.dir)
                H.info = menor.info
                H.dir = self._removerMenor(H.dir)
            else:
                H.dir = self._removeNO(H.dir, valor)

        return self._balancear(H)

    def remove(self, valor):
        if(self.__raiz == None or not self.busca(valor)):
            return False #árvore vazia ou valor não existe na árvore
        else:
            self.__raiz = self._removeNO(self.__raiz, valor)
            if(self.__raiz != None):
                self.__raiz.cor = BLACK

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

    def _preOrdem(self,raiz):
        if(raiz != None):
            if(raiz.cor):
                print('RED) ',raiz.info)
            else:
                print('BLACK) ',raiz.info)
            self._preOrdem(raiz.esq)
            self._preOrdem(raiz.dir)

    def preOrdem(self):
        if(self.__raiz != None):
            self._preOrdem(self.__raiz)

    def _emOrdem(self,raiz):
        if(raiz != None):            
            self._emOrdem(raiz.esq)
            if(raiz.cor):
                print('RED) ',raiz.info)
            else:
                print('BLACK) ',raiz.info)
            self._emOrdem(raiz.dir)

    def emOrdem(self):
        if(self.__raiz != None):
            self._emOrdem(self.__raiz)
        
    def _posOrdem(self,raiz):
        if(raiz != None):            
            self._posOrdem(raiz.esq)            
            self._posOrdem(raiz.dir)
            if(raiz.cor):
                print('RED) ',raiz.info)
            else:
                print('BLACK) ',raiz.info)

    def posOrdem(self):
        if(self.__raiz != None):
            self._posOrdem(self.__raiz)

#=================================================
"""
V = [1,2,3,10,4,5,9,7,8,6]
#V = [1,2,3,4,5,6,7,8,9,10]
#V = [10,9,8,7,6,5,4,3,2,1]

arv = ArvLLRB()
for v in V:
    print('Insere: ',v)
    arv.insere(v)
    arv.emOrdem()
    print('--------------')

#arv.preOrdem()
arv.emOrdem()
#arv.posOrdem()

"""

#"""
#V = [1,2,3,4]
#V = [4,2,7,1,3]
V = [1,2,3,10,4,5,9,7,8,6]

arv = ArvLLRB()
for v in V:
    print('Insere: ',v)
    arv.insere(v)
    #arv.emOrdem()
    print('--------------')
arv.emOrdem()
print('--------------')

R = [7,8,9]
for v in R:
    print('Remove: ',v)
    arv.remove(v)
    arv.emOrdem()
    print('--------------')

#"""
