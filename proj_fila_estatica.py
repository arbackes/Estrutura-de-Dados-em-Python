class FilaEst:
    def __init__(self):
        self.__qtd = 0
        self.__inicio = 0
        self.__final = 0
        self.__MAX = 100
        self.__itens = [0 for i in range(self.__MAX)]
        
    def insere(self, valor):
        if(self.__qtd == self.__MAX):
            return False

        self.__itens[self.__final] = valor
        self.__final = (self.__final + 1) % self.__MAX
        self.__qtd = self.__qtd + 1
        return True

    def remove(self):
        if(self.__qtd == 0):
            return False

        self.__inicio = (self.__inicio + 1) % self.__MAX
        self.__qtd = self.__qtd - 1
        return True

    def consulta(self):
        if(self.__qtd == 0):
            return None

        return self.__itens[self.__inicio]

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

pi = FilaEst()
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


