def buscaLinear(V, elem):
    N = len(V)
    for i in range(N):
        if(elem == V[i]):
            return i; #elemento encontrado
    
    return -1;#elemento não encontrado

# ===================================================

def buscaOrdenada(V, elem):
    N = len(V)
    for i in range(N):
        if(elem == V[i]):
            return i; #elemento encontrado
        else:
            if(elem < V[i]):
                return -1# para a busca
    
    return -1;#elemento não encontrado

# ===================================================

def buscaBinaria(V, elem):    
    inicio = 0;
    final = len(V)-1;
    while(inicio <= final):
        meio = int((inicio + final)/2);
        print("meio = ",meio);
        if(elem < V[meio]):
            final = meio-1;#busca na metade da esquerda
        else:
            if(elem > V[meio]):
                inicio = meio+1;#busca na metade da direita
            else:
                return meio;
    
    return -1;#elemento não encontrado

# ===================================================
class Lista:
    def __init__(self):
        self.Nome = []
        self.Matricula = []
        self.N = 0
        
    def add(self,matricula,nome):
        self.Nome.append(nome);
        self.Matricula.append(matricula);
        self.N = self.N + 1

    def print(self):
        for i in range(self.N):
            print(self.Matricula[i],') ',self.Nome[i])

    def buscaLinearMatricula(self,mat):
        for i in range(self.N):
            if(mat == self.Matricula[i]):
                return i; #elemento encontrado
        
        return -1;#elemento não encontrado

    def buscaLinearNome(self,nome):
        for i in range(self.N):
            if(nome == self.Nome[i]):
                return i; #elemento encontrado
        
        return -1;#elemento não encontrado    
# ===================================================
"""
vet = [-8,-5,1,4,14,21,23,54,67,90];
if(buscaBinaria(vet,90) != -1):
    print("OK")
else:
    print("ERRO");

"""
li = Lista();
li.add(2,"Andre")
li.add(4,"Ricardo")
li.add(1,"Marcia")
li.add(3,"Ana")

li.print()

if(li.buscaLinearNome("Ana") != -1):
    print("OK")
else:
    print("ERRO");
