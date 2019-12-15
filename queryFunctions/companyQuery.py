'''
Here we import the following libraries:

1 - rdflib: To query the graph, transform the data typed by the user
in the Literal format.
'''
from rdflib import Graph, Literal

# Producer, Licensor and Studio query function.
def companyQuery(g):
    '''
    There's two variables with SPARQL commands, the first one is to display 
    all the producers the anime has.
    
    The second query displays all the licensors the anime has.

    The third query displays all the studios the anime has.
    '''

    q1 = """ SELECT ?tt ?pd
            WHERE {
                ?a rdf:type ?type .
                ?a dc:title ?tt .
                ?a dbo:producer ?pd .
                FILTER (?type = dbo:Anime)
            }"""

    q2 = """ SELECT ?tt ?lc
            WHERE {
                ?a rdf:type ?type .
                ?a dc:title ?tt .
                ?a schema:copyrightHolder ?lc .
                FILTER (?type = dbo:Anime)
            }"""

    q3 = """ SELECT ?tt ?st
            WHERE {
                ?a rdf:type ?type .
                ?a dc:title ?tt .
                ?a schema:productionCompany ?st .
                FILTER (?type = dbo:Anime)
            }"""

    # Requesting the user to type the anime he wants to know the producers and licensors.
    anime = input("Type the name of the anime you're looking for the producers, licensors and studios: ")
    anime = Literal(anime)
    print("\nWe're looking for producers, licensors and studios of", "\"" + str(anime) + "\"", "in our database, please wait...")

    # Doing the two query commands.
    result1 = g.query(q1, initBindings={"tt": anime})
    result2 = g.query(q2, initBindings={"tt": anime})
    result3 = g.query(q3, initBindings={"tt": anime})

    # Printing all the data obtained if it exists.
    print("\nProducers, Licensors and Studios of:", str(anime), "\n")

    # Printing the producers.
    print("Producers:")
    
    for row in result1:
        if(row.pd == None):
            print("-> Unknown")
        else:
            print("->", row.pd)

    print()

    # Printing the licensors.
    print("Licensors:")
    
    for row in result2:
        if(row.lc == None):
            print("-> Unknown of Nonexistent")
        else:
            print("->", row.lc)

    print()

    # Printing the licensors.
    print("Studios:")
    
    for row in result3:
        if(row.st == None):
            print("-> Unknown or Nonexistent")
        else:
            print("->", row.st)

    input("\nPress ENTER to continue...")