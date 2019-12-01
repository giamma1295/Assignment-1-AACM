#%load_ext autoreload
#%autoreload 2
from Graph import Graph


#carico il grafo

grafo = Graph('grafi/USAir97.net')

#print del grafo
grafo.printGrafo()

grafo.diGraph
grafo.verDict

#vertex_count
#con log
#grafo.vertex_count(True)

#senza log
grafo.vertex_count(True)

#vertices
#con log
grafo.vertices(True)

#senza log
#grafo.vertices()


#edge_count
grafo.edge_count(True)

#edges

grafo.edges()

#get_edge(self, u, v, log=False)
grafo.get_edge(201, 118, True)
