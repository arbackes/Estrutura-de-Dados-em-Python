import copy

class Aluno:
    def __init__(self,Matricula,Nome,Nota):        
        self.Matricula = Matricula
        self.Nome = Nome
        self.Nota = Nota
        
    def __str__(self):
        return '%d, %s, %f' % (self.Matricula,self.Nome,self.Nota)
        
        
class Hash:
    def __init__(self,tamanho):
        self.__qtd = 0
        self.__TABLE_SIZE = tamanho
        self.__itens = [None for i in range(tamanho)]

    def __chaveDivisao(self,chave):
        return (chave & 0x7FFFFFFF) % self.__TABLE_SIZE

    def __chaveMultiplicacao(self,chave):
        A = 0.6180339887
        val = chave * A
        val = val - int(val)
        return val * self.__TABLE_SIZE

    def __chaveDobra(self, chave):
        num_bits = 10
        parte1 = chave >> num_bits
        parte2 = chave & (self.__TABLE_SIZE - 1)
        return parte1 ^ parte2

    def __valorString(self,str):
        valor = 7
        for letra in str:
            valor = 31 * valor + ord(letra)
        return valor

    def insereHash_SemColisao(self,Matricula,Nome,Nota):
        if(self.__qtd == self.__TABLE_SIZE):
            return False

        chave = Matricula
        pos = self.__chaveDivisao(chave)
        self.__itens[pos] = Aluno(Matricula,Nome,Nota)
        self.__qtd = self.__qtd + 1
        print('pos = ',pos)
        return True

    def buscaHash_SemColisao(self,Matricula):
        chave = Matricula
        pos = self.__chaveDivisao(chave)
        return copy.copy(self.__itens[pos])

    def __sondagemLinear(self, pos, i):
        return ((pos + i) & 0x7FFFFFFF) % self.__TABLE_SIZE


    def __sondagemQuadratica(self, pos, i):
        pos = pos + 2*i + 5*i*i
        return (pos & 0x7FFFFFFF) % self.__TABLE_SIZE

    def __duploHash(self, H1, chave, i):
        H2 = self.__chaveDivisao(chave) + 1
        return ((H1 + i*H2) & 0x7FFFFFFF) % self.__TABLE_SIZE
    
    def insereHash_EnderAberto(self,Matricula,Nome,Nota):
        if(self.__qtd == self.__TABLE_SIZE):
            return False

        chave = Matricula
        pos = self.__chaveDivisao(chave)
        
        for i in range(self.__TABLE_SIZE):
            print('mat:',Matricula,')',i)
            newPos = self.__sondagemLinear(pos,i)
            if(self.__itens[newPos] == None):
                self.__itens[newPos] = Aluno(Matricula,Nome,Nota)
                self.__qtd = self.__qtd + 1
                return True            
        
        return False

    def buscaHash_EnderAberto(self,mat):
        pos = self.__chaveDivisao(mat)
        for i in range(self.__TABLE_SIZE):
            print('mat:',mat,')',i)
            newPos = self.__sondagemLinear(pos,i)
            if(self.__itens[newPos] == None):
                return None

            aluno = self.__itens[newPos]
            if(aluno.Matricula == mat):
                return copy.copy(aluno)

        return None

    def print(self):
        print(self.__qtd,' / ',self.__TABLE_SIZE)
        for i in range(self.__TABLE_SIZE):
            print(i,") ",self.__itens[i])

   
# ===================================================

ha = Hash(10)

ha.insereHash_EnderAberto(12,"Andre",9.5)
ha.insereHash_EnderAberto(14,"Ricardo",7.2)
ha.insereHash_EnderAberto(22,"Marcia",8.2)
ha.insereHash_EnderAberto(32,"Ana",5.4)

ha.print()

x = ha.buscaHash_EnderAberto(42)

print('Busca')
print(x)

