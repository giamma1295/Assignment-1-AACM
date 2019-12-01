# Assignment-1-AACM

First assignment for AACM course, ECS @ University of Messina

![Unime Logo](https://upload.wikimedia.org/wikipedia/it/f/fd/Unime.png)

`Graph.py` contain all the necessary to load a graph from an edge list, supported graph are:

    - Simple graph not weighted
    - Simple graph weighted
    - Directed graph not weighted
    - Direct graph weighted

### Installation

just clone this repo and import module into your project

	   from Graph import Graph

### Usage

First you need to create an istance of Graph

#### Constructor

	Graph(edgeListFile, directed = None, weighted = None)
- edgeListFile -> required, is the path/file that contain the edge list
- directed -> optional because the algorithm will find if a graph is directed or not, but i suggest to specify if the graph is directed or not to avoid any issue.
- weighted -> optional because the algorithm will find if a graph is weighted or not, but i suggest to specify if the graph is weighted or not to avoid any issue.

that's all folks!!!

#### Method

print graph details;

	info()

get vertrex number:

	vertex_count()

get vertrex list
(prop=False -> only vetrex list, prop=True also vertrex properties)

	vertices(prop=False)

get edges number :

	edge_count()

get list of edges (log -> print log);

	edges(log=False)

get edge ;

	get_edge(u, v, log=False)

- u and v -> vetrex of node
- log -> print log

get degree of a vertrex (v)  in a non directed graph;

	degree(v)

get in Degree of a vertrex (v) in a directed graph:

	degree(v, out=False)

get out Degree of a vertrex (v) in a directed graph:

	degree(v, out=True) or degree(v)

....
