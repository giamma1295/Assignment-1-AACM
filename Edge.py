class Edge(object):
    """docstring for Edge."""


    def __init__(self, arg):
        super(Edge, self).__init__()
        self.arg = arg



    def caricaDaFile(self,filename):


        graphFile = open(filename,'r')

        #la edge list contine per ogni riga la tupla nodo1 nodo2 peso
        #carichiamo nella variabile
        graphFile.readlines()

        #apro il file del grafo
        graphFile = open(filename,'r')
        g = [] #will be a list of sets(nodo1 -> int, nodo2 -> int, peso float)
        #la edge list contine per ogni riga la tupla nodo1 nodo2 peso
        #ciclo per le varie righe del file
        for linea in graphFile.readlines():

            edge = linea.split()

            edge = (int(edge[0]),int(edge[1]),float(edge[2]))
            g.append(edge)

        return g
