class ListaEst:
    def __init__(self):
        self.__qtd = 0
        self.__MAX = 100
        self.__itens = [0 for i in range(self.__MAX)]

    def insere_final(self, valor):
        if(self.__qtd == self.__MAX):
            return False

        self.__itens[self.__qtd] = valor
        self.__qtd = self.__qtd + 1
        return True

    def insere_inicio(self, valor):
        if(self.__qtd == self.__MAX):
            return False

        i = self.__qtd-1
        while(i >= 0):
            self.__itens[i + 1] = self.__itens[i]
            i = i - 1
            
        self.__itens[0] = valor
        self.__qtd = self.__qtd + 1
        return True

    def insere_ordenado(self, valor):
        if(self.__qtd == self.__MAX):
            return False

        i = self.__qtd
        while(i > 0 and valor < self.__itens[i-1]):
            self.__itens[i] = self.__itens[i-1]
            i = i - 1
        
        self.__itens[i] = valor
        self.__qtd = self.__qtd + 1
        return True

    def remove_final(self):
        if(self.__qtd == 0):
            return False

        self.__qtd = self.__qtd - 1
        return True

    def remove_inicio(self):
        if(self.__qtd == 0):
            return False

        for i in range(self.__qtd-1):
            self.__itens[i] = self.__itens[i+1]

        self.__qtd = self.__qtd - 1
        return True

    def remove_valor(self,valor):
        if(self.__qtd == 0):
            return False

        i = 0
        while(i < self.__qtd and self.__itens[i] != valor):
            i = i + 1

        if(i == self.__qtd):
            return False

        k = i
        while(k < self.__qtd-1):
            self.__itens[k] = self.__itens[k+1]
            k = k + 1

        self.__qtd = self.__qtd - 1
        return True
    
    def consulta(self,valor):
        for va in self.__itens:
            if(va == valor):
                return True
            
        return False        
        
    def vazia(self):
        return (self.__qtd == 0)

    def cheia(self):
        return (self.__qtd == self.__MAX)

    def tamanho(self):
        return self.__qtd

    def print(self):
        for i in range(self.__qtd):
            print(i,") ",self.__itens[i])


# ===================================================

V = [10, 40, 20, 51, -5]

pi = ListaEst()
print(pi.consulta(20))
print('-------------')
for v in V:
    pi.insere_final(v)
pi.print()

print('-------------')
print(pi.consulta(20))
print(pi.consulta(120))
print('-------------')

pi.remove_valor(20)
pi.print()
print('-------------')
print(pi.consulta(40))
print('-------------')


