class Elemento:
    def __init__(self, prioridade, nome):
        self.prioridade = prioridade
        self.nome = nome
        
class FilaPrioridade:
    def __init__(self):
        self.__qtd = 0
        self.__MAX = 100
        self.__itens = [None for i in range(self.__MAX)]
        
    def insere(self, prioridade, nome):
        if(self.__qtd == self.__MAX):
            return False

        i = self.__qtd - 1
        while(i >= 0 and self.__itens[i].prioridade >= prioridade):
            self.__itens[i+1] = self.__itens[i]
            i = i - 1
        
        self.__itens[i + 1] = Elemento(prioridade,nome)
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

        return self.__itens[self.__qtd-1].nome

    def vazia(self):
        return (self.__qtd == 0)

    def cheia(self):
        return (self.__qtd == self.__MAX)

    def tamanho(self):
        return self.__qtd

    def print(self):
        for i in range(self.__qtd-1,-1,-1):
            print(i,") ",self.__itens[i].prioridade,': ',self.__itens[i].nome)


# ===================================================

pi = FilaPrioridade()
print(pi.consulta())
print('-------------')
pi.insere(1,'Andre')
pi.insere(2,'Rosana')
pi.insere(5,'Carlos')
pi.insere(10,'Nilza')
pi.insere(9,'Inacio')
pi.insere(2,'Eduardo')
pi.print()

print('-------------')
print(pi.consulta())
print('-------------')

pi.remove()
pi.print()
print('-------------')
print(pi.consulta())
print('-------------')

