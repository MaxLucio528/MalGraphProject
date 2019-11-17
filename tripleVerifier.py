# Obtendo a biblioteca rdflib e importando especificamento o Graph
from rdflib import Graph

# Criando o grafo e importando o arquivo turtle para leitura
g = Graph()
filename = 'AnimeData.ttl'
g.parse(filename, format='turtle')

# Lendo o grafo e informando a quantidade de triplas que constam nele
print(filename, 'tem', len(g), 'triplas')