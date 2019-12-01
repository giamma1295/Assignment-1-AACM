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
        v = []
        ver = {}
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
            #aggiungo l'arco alla lista degli archi
            g.append(edge)
            dictG.update({'('+str(edge[0])+','+str(edge[1])+')' : float(edge[2])})

            #riempio la lista dei nodi
            # --- Open Point, nella descrizione di insert vertrex viene detto
            # must create and return a new vertex with attribute x
            #immagino che ogni verice potrebbe avere delle proprietà, ad esempio associamo ad un vertice un nome
            #per memorizzare la lista dei nodi userò un dizionario {key -> nodo : value -> proprietà}
            if edge[0] not in v:
                v.append(edge[0])
                pass
            if edge[1] not in v:
                v.append(edge[1])
                pass
            pass

            if str(edge[0]) not in ver.keys():
                ver.update({str(edge[0]) : None})
                pass
            if str(edge[1]) not in ver.keys():
                ver.update({str(edge[1]) : None})
                pass
            pass

        #print(dictG)
        #print('richiesto : ' + str(dictG['(131,146)']))
        self.edgesList = g
        self.dictGraph = dictG
        self.verticesList = v
        self.verDict = ver
        pass


    def printGrafo(self):
        print(self.edgesList)
        pass

    def vertex_count(self, log=False):
        n = len(self.verticesList)

        if log:
            print('number of vetrex in given graph -> ' + str(n) )
            pass
        return n

    def vertices(self, prop=False):
        #vertici = []

        #for v in self.edgesList:
        #    if v[0] not in vertici:
        #        vertici.append(v[0])
        #        pass
        #    if v[1] not in vertici:
        #        vertici.append(v[1])
        #        pass
        #    pass

        #if ordered:
        #    vertici.sort()
        #    pass
        if prop:
            print("aaaa")
            #ritorno il dizionario dei nodi con eventuali proprietà dei nodi
            return self.verDict
        else:
            print("bbbbb")
            #ritorno lista di nodi senza eventuali proprietà
            return self.verticesList
            pass

    def edge_count(self, log=False):
        n = len(self.edgesList)
        if log:
            print('number of edge in given graph -> ' + str(n) )
            pass
        return n

    def edges(self, log=False):
        if log:
            print('edges in given graph : ')
            print('\n'.join(map(str, map(lambda x: {'nodo -> ':x[1], 'id -> ':x[0]}, enumerate(self.edgesList)))))
            pass
        return self.edgesList

    def get_edge(self, u, v, log=False):
        selected = None
        for ver in self.edgesList:
            if self.diGraph:
                if (ver[0] == u and ver[1] == v) :
                    selected = ver
                    print("grafo diretto")
                    pass
            else:
                if (ver[0] == u and ver[1] == v) or (ver[1] == u and ver[0] == v) :
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
        deg = 0
        #out è indifferente per grafi non diretti
        #per i grafi non diretti non la inDegree e la outDegree coincidono, per calcolare il degree di un nodo in questo grafo
        #per i grafi diretti invece bisogna tenere conto di out, se è true ci restituirà la outDegree, numero di archi partenti(outgoing)
        #dal nodo specificato
        #se out è false allora calcoliamo la in degree, cioè il numero di archi entranti(ingoing) nel nodo specificato
        #nelle nostre tuple abbiamo : [0]-> nodo da cui parte l'arco, [1] -> nodo su cui atterra l'arco, [2] -> peso

        #grafo diretto
        if self.diGraph:
            #out -> true calcoliamo la outdegree
            if out:
                for x in self.edgesList:
                    if v == x[0]:
                        deg = deg + 1
                        pass
                    pass
                print("node " + str(v) + " outDegree :")
                pass
            #out -> false calcoliamo la indegree
            else:
                for x in self.edgesList:
                    if v == x[1]:
                        deg = deg + 1
                        pass
                    pass
                print("node " + str(v) + " inDegree :")
                pass
            pass
        #grafo non diretto
        else:
            #calcolo il degree
            for x in self.edgesList:
                if v == x[0] or v == x[1]:
                    deg = deg + 1
                    pass
                pass
            print("node " + str(v) + " degree :")
            pass
        print(deg)
        return deg

    def incident_edges(self, v, out=True):
        inc = []
        #stesse premesse per il metodo degree
        #grafo diretto
        if self.diGraph:
            #out -> true calcoliamo la outdegree
            if out:
                for x in self.edgesList:
                    if v == x[0]:
                        inc.append(x)
                        pass
                    pass
                print("list of incident edges outgoing " + str(v) + " :")
                pass
            #out -> false calcoliamo la indegree
            else:
                for x in self.edgesList:
                    if v == x[1]:
                        inc.append(x)
                        pass
                    pass
                print("list of incident edges ingoing " + str(v) + " :")
                pass
            pass
        #grafo non diretto
        else:
            #calcolo il degree
            for x in self.edgesList:
                if v == x[0] or v == x[1]:
                    inc.append(x)
                    pass
                pass
            print("list of incident edges " + str(v) + " :")
            pass
        print(inc)
        return inc

    def insert_vertex(self, x=None):
        pass

    def insert_edge(self, u, v, x=None):
        pass

    def remove_vertex(self, v):
        pass

    def remove_edge(self, e):
        pass
