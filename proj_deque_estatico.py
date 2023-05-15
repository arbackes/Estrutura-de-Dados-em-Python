class DequeEst:
    def __init__(self):
        self.__qtd = 0
        self.__inicio = 0
        self.__final = 0
        self.__MAX = 100
        self.__itens = [0 for i in range(self.__MAX)]

    def insere_final(self, valor):
        if(self.__qtd == self.__MAX):
            return False

        self.__itens[self.__final] = valor
        self.__final = (self.__final + 1) % self.__MAX
        self.__qtd = self.__qtd + 1
        return True

    def insere_inicio(self, valor):
        if(self.__qtd == self.__MAX):
            return False

        self.__inicio = self.__inicio - 1
        if(self.__inicio < 0):
            self.__inicio = self.__MAX - 1
            
        self.__itens[self.__inicio] = valor
        self.__qtd = self.__qtd + 1
        return True    

    def remove_final(self):
        if(self.__qtd == 0):
            return False

        self.__final = self.__final - 1
        if(self.__final < 0):
            self.__final = self.__MAX - 1
            
        self.__qtd = self.__qtd - 1
        return True

    def remove_inicio(self):
        if(self.__qtd == 0):
            return False

        self.__inicio = (self.__inicio + 1) % self.__MAX
        self.__qtd = self.__qtd - 1
        return True    

    def consulta_inicio(self):
        if(self.__qtd == 0):
            return None
        
        return self.__itens[self.__inicio]

    def consulta_final(self):
        if(self.__qtd == 0):
            return None
        
        pos = self.__final - 1
        if(pos < 0):
            pos = self.__MAX-1

        return self.__itens[pos]
    
    def vazia(self):
        return (self.__qtd == 0)

    def cheia(self):
        return (self.__qtd == self.__MAX)

    def tamanho(self):
        return self.__qtd

    def print(self):
        i = self.__inicio
        for n in range(self.__qtd):
            print(i,") ",self.__itens[i])
            i = (i + 1) % self.__MAX


# ===================================================

pi = DequeEst()
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


