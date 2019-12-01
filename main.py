%load_ext autoreload
%autoreload 2
from Graph import Graph


#carico il grafo

grafo = Graph('grafi/USAir97.net')

#print del grafo
grafo.info()

grafo.diGraph
grafo.gWeigted
grafo.verDict

#vertex_count
#con log
#grafo.vertex_count(True)

#senza log
grafo.vertex_count()

#vertices
#con log
grafo.vertices(True)

#senza log
grafo.vertices()


#edge_count
grafo.edge_count(True)

#edges

grafo.edges()

#get_edge(self, u, v, log=False)
grafo.get_edge(118, 201, True)

grafo.degree(201, False)

grafo.incident_edges(118, True)

grafo.insert_vertex()

grafo.insert_edge(335, 335)


grafo.remove_vertex(335)
grafo.remove_edge((335,335))
