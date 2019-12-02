#estenzioni per iPython affinchè al cambiamento di un modulo viene ricaricato a runtime
%load_ext autoreload
%autoreload 2
from Graph import Graph


#carico il grafo

grafo = Graph('grafi/pesatoDiretto.txt')

#print del grafo
grafo.info()

#vertex_count
#con log
#grafo.vertex_count(True)

#senza log
grafo.vertex_count()

#vertices
#con proprietà
print("Vertrex list with props")
print("vertices(True) -> " + str(grafo.vertices(True)))
#senza proprietà
print("Vertrex list without props")
print("vertices() -> " + str(grafo.vertices()))

#edge_count
print("Number of edge in the graph")
print("edge_count() -> " + str(grafo.edge_count()))

#edges
print("Edge list")
print("edges() -> " + str(grafo.edges()))

#get_edge(self, u, v, log=False)
print("Search an edge in the graph, u = 118, v = 201")
print("get_edge(u, v, False) ->" + str(grafo.get_edge(118, 201, False)))
#degree
print("Degree")
grafo.degree(201)
#incident_edges
print("Incident edges")
grafo.incident_edges(118, True)

#insert_vertex

grafo.insert_vertex("Pippo")
grafo.insert_vertex("Pluto")
grafo.insert_vertex("Paperino")
grafo.insert_vertex("Minnie")
grafo.insert_vertex("Zio Paperone")

print("Now the Vertrex list with props is")
print("vertices(True) -> " + str(grafo.vertices(True)))

#insert an edge

print("Edge inserted using insert_edge(335, 336) -> " + str(grafo.insert_edge(335, 336)))


print("remove a vertrex using remove_vertex(334) -> " + str(grafo.remove_vertex(334)))
print("if i will try to remove a non existent vertex using remove_vertex(334) -> " + str(grafo.remove_vertex(334)))
print("remove an existent edge using remove_edge((335,336)) -> " + str(grafo.remove_edge((335,336))))
print("remove a non existent edge using remove_edge((335,336)) -> " + str(grafo.remove_edge((335,336))))
