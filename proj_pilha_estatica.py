class PilhaEst:
    def __init__(self):
        self.__qtd = 0
        self.__MAX = 100
        self.__itens = [0 for i in range(self.__MAX)]

    def insere(self, valor):
        if(self.__qtd == self.__MAX):
            return False

        self.__itens[self.__qtd] = valor
        self.__qtd = self.__qtd + 1
        return True

    def remove(self):
        if(self.__qtd == 0):
            return False

        self.__qtd = self.__qtd - 1
        return True

    def consulta(self):
        if(self.__qtd == 0):
            return None

        return self.__itens[self.__qtd-1]

    def vazia(self):
        return (self.__qtd == 0)

    def cheia(self):
        return (self.__qtd == self.__MAX)

    def tamanho(self):
        return self.__qtd

    def print(self):
        for i in range(self.__qtd-1,-1,-1):
            print(i,") ",self.__itens[i])
    
# ===================================================

pi = PilhaEst()
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


