'''
Here we import the following libraries:

1 - rdflib: To query the graph, transform the data typed by the user
in the Literal format.
'''
from rdflib import Graph, Literal

# Track query function.
def trackQuery(g):
    '''
    There's two variables with SPARQL commands, the first one is to display 
    all the openings the anime has.
    
    The second query displays all the endings the anime has.
    '''

    q1 = """ SELECT ?tt ?tk ?at
            WHERE {
                ?a rdf:type ?type .
                ?a dc:title ?tt .
                ?a mal:opening ?op .
                ?op mo:Track ?tk .
                ?op mo:MusicArtist ?at .
                FILTER (?type = dbo:Anime)
            }"""

    q2 = """ SELECT ?tt ?tk ?at
            WHERE {
                ?a rdf:type ?type .
                ?a dc:title ?tt .
                ?a mal:ending ?ed .
                ?ed mo:Track ?tk .
                ?ed mo:MusicArtist ?at .
                FILTER (?type = dbo:Anime)
            }"""

    # Requesting the user to type the anime he wants to know the tracks.
    anime = input("Type the name of the anime you're looking for the tracks: ")
    anime = Literal(anime)
    print("\nWe're looking for tracks of", "\"" + str(anime) + "\"", "in our database, please wait...")

    # Doing the two query commands.
    result1 = g.query(q1, initBindings={"tt": anime})
    result2 = g.query(q2, initBindings={"tt": anime})

    # Printing all the data obtained if it exists.
    print("\nTracks of:", str(anime), "\n")

    # Printing the openings.
    print("Openings:")
    
    for row in result1:
        if(row.tk == None):
            print("-> Unknown or Nonexistent")
        else:
            print("->", row.tk, "-", row.at)

    print()
    
    # Printing the endings.
    print("Endings:")
    
    for row in result2:
        if(row.tk == None):
            print("-> Unknown or Nonexistent")
        else:
            print("->", row.tk, "-", row.at)

    input("\nPress ENTER to continue...")