#classe che conterrà il grafo ed i vari metodi da implementare
class Graph:
    """docstring for Graph."""

#costruttore della classe, richiede il passaggio del nome del file da cui caricare la edge list

    def __init__(self, edgeListFile):
        #super(Graph, self).__init__()
        #apro il file del grafo
        graphFile = open(edgeListFile,'r')
        self.diGraph = False #variabile che indicherà se il grafo è un grafo diretto
        #la edge list contine per ogni riga la tupla nodo1 nodo2 peso
        #carichiamo nella variabile
        g = [] #sarà una lista di tuple(nodo1 -> int, nodo2 -> int, peso float)
        #la edge list contine per ogni riga la tupla nodo1 nodo2 peso
        #ciclo per le varie righe del file
        dictG = {} #dictionary {key -> (u,v) : value -> weight}
        for linea in graphFile.readlines():
            edge = linea.split()
            edge = (int(edge[0]),int(edge[1]),float(edge[2]))
            #in fase di init controllo se il grafo contenuto nel file è un grafo diretto
            #questo è vero se trovo un'arco (u,v) inserendo l'arco (v,u)
            if not (self.diGraph):
                #controllo se è un grafo diretto
                for e in g:
                    if (e[0] == edge[1] and e[1] == edge[0]):
                        self.diGraph = True
                        break
                        pass
                    pass
                pass
            g.append(edge)
            dictG.update({'('+str(edge[0])+','+str(edge[1])+')' : float(edge[2])})
            pass
        #print(dictG)
        #print('richiesto : ' + str(dictG['(131,146)']))
        self.graph = g
        self.dictGraph = dictG
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
            print("Vertrex List  -> \n " + str(vertici))
            #print('\n'.join(map(str, vertici)))
            pass
        return vertici

    def edge_count(self, log=False):
        n = len(self.graph)
        if log:
            print('number of edge in given graph -> ' + str(n) )
            pass
        return n

    def edges(self, log=False):
        if log:
            print('edges in given graph : ')
            print('\n'.join(map(str, map(lambda x: {'nodo -> ':x[1], 'id -> ':x[0]}, enumerate(self.graph)))))
            pass
        return self.graph

    def get_edge(self, u, v, log=False):
        selected = None
        for ver in self.graph:
            if self.diGraph:
                if (ver[0] == u and ver[1] == v)) :
                    selected = ver
                    print("grafo diretto")
                    pass
            else:
                if (ver[0] == u and ver[1] == v) or ((ver[1] == u and ver[0] == v)) :
                    selected = ver
                    print("grafo non diretto")
                    pass
                pass
        if log:
            if selected == None:
                print("requested vertrex not Found ")
            else:
                print("requested vertrex -> " + str(selected))
            pass
        return selected

    def degree(self, v, out=True):
        pass

    def incident_edges(self, v, out=True):
        pass

    def insert_vertex(self, x=None):
        pass

    def insert_edge(self, u, v, x=None):
        pass

    def remove_vertex(self, v):
        pass

    def remove_edge(self, e):
        pass
