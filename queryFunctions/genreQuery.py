'''
Here we import the following libraries:

1 - rdflib: To query the graph, transform the data typed by the user
in the Literal format.
'''
from rdflib import Graph, Literal

# Genre query function.
def genreQuery(g):
    '''
    This is a variable with SPARQL commands, it's goal is to find all
    the genres an anime has.
    '''

    q1 = """ SELECT ?tt ?gn
            WHERE {
                ?a rdf:type ?type .
                ?a dc:title ?tt .
                ?a dbo:genre ?gn .
                FILTER (?type = dbo:Anime)
            }"""

    # Requesting the user to type the anime he wants to know the genres.
    anime = input("Type the name of the anime you're looking for the genres: ")
    anime = Literal(anime)
    print("\nWe're looking for genres of", "\"" + str(anime) + "\"", "in our database, please wait...")

    # Doing the two query commands.
    result1 = g.query(q1, initBindings={"tt": anime})

    # Printing all the data obtained if it exists.
    print("\nGenres of:", str(anime), "\n")
    
    for row in result1:
        if(row.gn == None):
            print("-> Unknown or Nonexistent")
        else:
            print("->", row.gn)

    input("\nPress ENTER to continue...")