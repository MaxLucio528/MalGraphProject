# Getting the library rdflib to parse the graph and import the clear screen function.
from rdflib import Graph
from generalFunctions.clearScreen import clear

# Parsing the graph.
g = Graph()
filename = "AnimeData.xml"
g.parse(filename)

clear()

# Reading the graph and informing how many triples it has.
print("\n" + filename, "has", len(g), "triples\n")

input("Press ENTER to continue...")

clear()