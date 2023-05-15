import copy
import math

class Grafo:
    def __init__(self,nro_vertices):
        self.__nro_vertices = nro_vertices
        self.__arestas = [[] for i in range(nro_vertices)]
        self.__pesos = [[] for i in range(nro_vertices)]

    def insereAresta(self, orig, dest, eh_digrafo, peso = 1):
        if(orig < 0 or orig >= self.__nro_vertices):
            return False

        if(dest < 0 or dest >= self.__nro_vertices):
            return False

        self.__arestas[orig].append(dest)
        self.__pesos[orig].append(peso)
        
        if(eh_digrafo == False):
            self.insereAresta(dest,orig,True,peso)

        return True

    def __buscaProfundidade_Rec(self, ini, visitado, cont):
        visitado[ini] = cont
        grau = len(self.__arestas[ini])
        for i in range(grau):
            if(visitado[self.__arestas[ini][i]] == 0):
                self.__buscaProfundidade_Rec(self.__arestas[ini][i],visitado,cont+1)
                
                
    def buscaProfundidade(self, ini):
        cont = 1
        visitado = [0 for i in range(self.__nro_vertices)]

        self.__buscaProfundidade_Rec(ini,visitado,cont)

        return visitado

    def buscaLargura(self, ini):
        cont = 1
        IF = 0
        FF = 0
        visitado = [0 for i in range(self.__nro_vertices)]
        fila = [0 for i in range(self.__nro_vertices)]

        FF = FF + 1
        fila[FF] = ini
        visitado[ini] = cont

        while(IF != FF):
            IF = (IF + 1) % self.__nro_vertices
            vert = fila[IF]
            cont = cont + 1
            grau = len(self.__arestas[vert])
            for i in range(grau):
                if(visitado[gr.__arestas[vert][i]] == 0):
                    FF = (FF + 1) % self.__nro_vertices
                    fila[FF] = gr.__arestas[vert][i]
                    visitado[gr.__arestas[vert][i]] = cont

        return visitado

    def __procuraMenorDistancia(self,dist, visitado):
        menor = -1
        menorDist = math.inf
        for i in range(len(dist)):
            if(dist[i] < menorDist and visitado[i] == False):
                menor = i
                menorDist = dist[i]
                
        return menor;
        
    def menorCaminho(self, ini):
        cont = self.__nro_vertices

        visitado = [False for i in range(self.__nro_vertices)]
        ant = [-1 for i in range(self.__nro_vertices)]
        dist = [math.inf for i in range(self.__nro_vertices)]
        dist[ini] = 0
        
        while(cont > 0):
            vert = self.__procuraMenorDistancia(dist, visitado)
            if(vert == -1):
                break

            visitado[vert] = True
            cont = cont - 1
            grau = len(self.__arestas[vert])
            for i in range(grau):                
                ind = gr.__arestas[vert][i]
                if(dist[ind] > dist[vert] + self.__pesos[vert][i]):
                    dist[ind] = dist[vert] + self.__pesos[vert][i]
                    ant[ind] = vert

        return dist,ant

    def arvoreGeradoraMinima_PRIM(self, orig):
        
        pai = [-1 for i in range(self.__nro_vertices)]
        pai[orig] = orig
        
        while(True):
            menorPeso = math.inf
            for i in range(self.__nro_vertices):
                if(pai[i] != -1):# achou vértices já visitado
                    grau = len(self.__arestas[i])
                    for j in range(grau):# percorre os vizinhos do vértice visitado
                        if(pai[self.__arestas[i][j]] == -1):# achou vértice vizinho não visitado
                            if(menorPeso > self.__pesos[i][j]):
                                menorPeso = self.__pesos[i][j]
                                orig = i
                                dest = self.__arestas[i][j]
            if(menorPeso == math.inf):
                break

            pai[dest] = orig
        return pai


    def arvoreGeradoraMinima_Kruskal(self, orig):
        arv = [i for i in range(self.__nro_vertices)]
        pai = [-1 for i in range(self.__nro_vertices)]
        
        pai[orig] = orig
        
        while(True):
            menorPeso = math.inf
            for i in range(self.__nro_vertices):# percorre todos os vértices
                grau = len(self.__arestas[i])
                for j in range(grau):# percorre os vizinhos do vértice visitado
                    if(arv[i] != arv[self.__arestas[i][j]]):
                        if(menorPeso > self.__pesos[i][j]):
                            menorPeso = self.__pesos[i][j]
                            orig = i
                            dest = self.__arestas[i][j]
                            
            if(menorPeso == math.inf):
                break

            if(pai[orig] == -1):
                pai[orig] = dest
            else:
                pai[dest] = orig

            v_dest = arv[dest]
            for i in range(self.__nro_vertices):
                if(arv[i] == v_dest):
                    arv[i] = arv[orig]


        return pai

    def print(self):
        for i in range(self.__nro_vertices):
            texto = '%d) ' % (i)
            grau = len(self.__arestas[i])
            for j in range(grau):
                texto = '%s %d (%.2f), ' % (texto,self.__arestas[i][j],self.__pesos[i][j])
            print(texto)
            

gr = Grafo(5)
eh_digrafo = True
gr.insereAresta(0, 1, eh_digrafo)
gr.insereAresta(1, 3, eh_digrafo)
gr.insereAresta(1, 2, eh_digrafo)
gr.insereAresta(2, 4, eh_digrafo)
gr.insereAresta(3, 0, eh_digrafo)
gr.insereAresta(3, 4, eh_digrafo)
gr.insereAresta(4, 1, eh_digrafo)

gr.print()

#visitado = gr.buscaProfundidade(0)
#visitado = gr.buscaLargura(0)
#print(visitado)

dist,ant = gr.menorCaminho(0)
print(dist)
print(ant)

"""

gr = Grafo(6)
eh_digrafo = False
gr.insereAresta(0, 1, eh_digrafo, 6)
gr.insereAresta(0, 2, eh_digrafo, 1)
gr.insereAresta(0, 3, eh_digrafo, 5)
gr.insereAresta(1, 2, eh_digrafo, 2)
gr.insereAresta(1, 4, eh_digrafo, 5)
gr.insereAresta(2, 3, eh_digrafo, 2)
gr.insereAresta(2, 4, eh_digrafo, 6)
gr.insereAresta(2, 5, eh_digrafo, 4)
gr.insereAresta(3, 5, eh_digrafo, 4)
gr.insereAresta(4, 5, eh_digrafo, 3)

gr.print()

#pai = gr.arvoreGeradoraMinima_PRIM(0)
pai = gr.arvoreGeradoraMinima_Kruskal(0)
print(pai)

"""
