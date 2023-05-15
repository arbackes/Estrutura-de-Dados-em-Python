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

        self.__itens[self.__qtd] = Elemento(prioridade,nome)
        self.__promoverElemento(self.__qtd)
        self.__qtd = self.__qtd + 1
        return True

    def __promoverElemento(self, filho):
        pai = int((filho - 1) / 2)
        
        while((filho > 0) and (self.__itens[pai].prioridade <= self.__itens[filho].prioridade)):
            temp = self.__itens[filho]
            self.__itens[filho] = self.__itens[pai]
            self.__itens[pai] = temp;

            filho = pai
            pai = int((pai - 1) / 2)
    
    def remove(self):
        if(self.__qtd == 0):
            return False

        self.__qtd = self.__qtd - 1
        self.__itens[0] = self.__itens[self.__qtd]
        self.__rebaixarElemento(0)
        
        return True

    def __rebaixarElemento(self, pai):
        filho = 2 * pai + 1;
        while(filho < self.__qtd):
            if(filho < self.__qtd - 1): #verifica se tem 2 filhos
                if(self.__itens[filho].prioridade < self.__itens[filho+1].prioridade):
                    filho = filho + 1 # filho aponta para filho menor 

            if(self.__itens[pai].prioridade >= self.__itens[filho].prioridade):
                break; # encontrou lugar

            temp = self.__itens[pai];
            self.__itens[pai] = self.__itens[filho];
            self.__itens[filho] = temp;

            pai = filho;
            filho = 2 * pai + 1;    

    def consulta(self):
        if(self.__qtd == 0):
            return None

        return self.__itens[0].nome

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

