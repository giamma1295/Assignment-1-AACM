%load_ext autoreload
%autoreload 2
from Graph import Graph


#carico il grafo

grafo = Graph('grafi/USAir97.net')

#print del grafo
grafo.printGrafo()

#vertex_count
#con log
grafo.vertex_count(True)

#senza log
grafo.vertex_count()

#vertices
#con log
grafo.vertices(True,True)

#senza log
grafo.vertices()


#edge_count
grafo.edge_count()
