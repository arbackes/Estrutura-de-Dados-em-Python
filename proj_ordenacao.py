def bubbleSort(V):
    N = len(V)
    continua = True
    while(continua):
        continua = False
        for i in range(N-1):
            if(V[i] > V[i+1]):
                aux = V[i]
                V[i] = V[i+1]
                V[i+1] = aux
                continua = True
        N = N - 1

# ===================================================

def insertionSort(V):
    N = len(V)
    for i in range(1,N):
        aux = V[i]
        j = i
        while(j > 0 and aux < V[j - 1]):
            V[j] = V[j - 1]
            j = j - 1
        V[j] = aux
        
# ===================================================

def selectionSort(V):
    N = len(V)
    for i in range(N-1):
        menor = i
        for j in range(i+1,N):
            if(V[j] < V[menor]):
                menor = j

        if(i != menor):
            troca = V[i]
            V[i] = V[menor]
            V[menor] = troca
        
# ===================================================

def merge(V, inicio, meio, fim):    
    tamanho = fim-inicio+1
    p1 = inicio
    p2 = meio+1
    fim1 = False
    fim2 = False
    
    temp = [0 for i in range(tamanho)]

    for i in range(tamanho):
        if(not fim1 and not fim2):
            if(V[p1] < V[p2]):
                temp[i] = V[p1]
                p1 = p1 + 1                
            else:
                temp[i] = V[p2]
                p2 = p2 + 1

            if(p1 > meio):
                fim1 = True

            if(p2 > fim):
                fim2 = True
        else:
            if(not fim1):
                temp[i] = V[p1]
                p1 = p1 + 1
            else:
                temp[i] = V[p2]
                p2 = p2 + 1
            
    k = inicio
    for j in range(tamanho):
        V[k] = temp[j]
        k = k + 1

def mergeSort(V, inicio, fim):
    if(inicio < fim):
        meio = int((inicio+fim)/2)
        mergeSort(V,inicio,meio)
        mergeSort(V,meio+1,fim)
        merge(V,inicio,meio,fim)

# ===================================================

def particiona(V, inicio, final):
    esq = inicio
    dir = final
    pivo = V[inicio]
    while(esq < dir):
        while(esq <= final and V[esq] <= pivo):
            esq = esq + 1

        while(dir >= 0 and V[dir] > pivo):
            dir = dir - 1

        if(esq < dir):
            aux = V[esq]
            V[esq] = V[dir]
            V[dir] = aux
            
    V[inicio] = V[dir]
    V[dir] = pivo
    return dir

def quickSort(V, inicio, fim):
    if(fim > inicio):
        pivo = particiona(V, inicio, fim)
        quickSort(V, inicio, pivo-1)
        quickSort(V, pivo+1, fim)
    
# ===================================================

def criaHeap(V, pai, fim):
    aux = V[pai]
    filho = 2 * pai + 1
    while(filho <= fim):
        if(filho < fim):
            if(V[filho] < V[filho + 1]):
                filho = filho + 1
                
        if(aux < V[filho]):
            V[pai] = V[filho]
            pai = filho
            filho = 2 * pai + 1
        else:
            filho = fim + 1
            
    V[pai] = aux
    

def heapSort(V):
    N = len(V)    
    for i in range(int((N - 1)/2),-1,-1):
        criaHeap(V, i, N-1)

    for i in range(N - 1,0,-1):
        aux = V[0]
        V[0] = V[i]
        V[i] = aux
        criaHeap(V, 0, i - 1)        

def countingSort(V):
    N = len(V) 
    MAX = max(V) + 1
    
    baldes = [0 for i in range(MAX)];
    
    for i in range(N):
        baldes[V[i]] = baldes[V[i]] + 1;

    print(baldes)
    i = 0
    for j in range(MAX):
        k = baldes[j]
        while(k > 0):
            V[i] = j
            i = i + 1
            k = k - 1
    
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

    def insertionSortMatricula(self):
        for i in range(1,self.N):
            auxMatricula = self.Matricula[i]
            auxNome = self.Nome[i]
            j = i
            while(j > 0 and auxMatricula < self.Matricula[j - 1]):
                self.Matricula[j] = self.Matricula[j - 1]
                self.Nome[j] = self.Nome[j - 1]
                j = j - 1
                
            self.Nome[j] = auxNome
            self.Matricula[j] = auxMatricula
    
# ===================================================
"""
vet = [8,2,1,7,4,6,5]
#vet = [23,4,67,-8,90,54,21]

print(vet)

#bubbleSort(vet)
#insertionSort(vet)
selectionSort(vet)
#mergeSort(vet,0,len(vet)-1)
#quickSort(vet,0,len(vet)-1)
#heapSort(vet)


print(vet)

"""

# ===================================================


vet = [8,2,1,7,4,6,5,8,1,5,8]
print(vet)
countingSort(vet)
print(vet)


# ===================================================

"""
li = Lista();
li.add(2,"Andre")
li.add(4,"Ricardo")
li.add(1,"Marcia")
li.add(3,"Ana")

li.print()

li.insertionSortMatricula()
print('--------------');

li.print()
"""

    

