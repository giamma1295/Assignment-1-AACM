#classe che conterrà il grafo ed i vari metodi da implementare
class Graph:
    """docstring for Graph."""

#costruttore della classe, richiede il passaggio del nome del file da cui caricare la edge list

    def __init__(self, edgeListFile):
        #super(Graph, self).__init__()
        #apro il file del grafo
        graphFile = open(edgeListFile,'r')
        #la edge list contine per ogni riga la tupla nodo1 nodo2 peso
        #carichiamo nella variabile
        g = [] #will be a list of sets(nodo1 -> int, nodo2 -> int, peso float)
        #la edge list contine per ogni riga la tupla nodo1 nodo2 peso
        #ciclo per le varie righe del file
        for linea in graphFile.readlines():
            edge = linea.split()
            edge = (int(edge[0]),int(edge[1]),float(edge[2]))
            g.append(edge)
        self.graph = g
        pass


    def printGrafo(self):
        print(self.graph)
        pass

    def vertex_count(self, log=False):
        n = len(self.vertices())

        if log:
            print('number of vetrex in given graph -> ' + str(n) )
            pass
        return n

    def vertices(self, log=False, ordered=False):
        vertici = []

        for v in self.graph:
            if v[0] not in vertici:
                vertici.append(v[0])
                pass
            if v[1] not in vertici:
                vertici.append(v[1])
                pass
            pass
        if ordered:
            vertici.sort()
            pass
        if log:
            print("Vertrex List -> \n " + str(vertici))
            pass
        return vertici

    def edge_count(self, log=False):
        n = len(self.graph)

        if log:
            print('number of edge in given graph -> ' + str(n) )
            pass
        return n
