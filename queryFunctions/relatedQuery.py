'''
Here we import the following libraries:

1 - rdflib: To query the graph, transform the data typed by the user
in the Literal format.
'''
from rdflib import Graph, Literal

# Works related to an anime query function.
def relatedQuery(g):
    '''
    There's four variables with query SPARQL commands: 
    
    * The first one is to display all the adaptations the anime has;
    * The second one is to display all the sequels the anime has;
    * The third one is to display all the prequels the anime has;
    * The fourth one is to display all the spin-offs the anime has.
    '''

    q1 = """ SELECT ?tt ?ad
            WHERE {
                ?a rdf:type ?type .
                ?a dc:title ?tt .
                OPTIONAL{ ?a mal:adaptation ?ad . }
                FILTER (?type = dbo:Anime)
            }"""

    q2 = """ SELECT ?tt ?sq
            WHERE {
                ?a rdf:type ?type .
                ?a dc:title ?tt .
                OPTIONAL{ ?a mal:sequel ?sq . }
                FILTER (?type = dbo:Anime)
            }"""

    q3 = """ SELECT ?tt ?pq
            WHERE {
                ?a rdf:type ?type .
                ?a dc:title ?tt .
                OPTIONAL{ ?a mal:prequel ?pq . }
                FILTER (?type = dbo:Anime)
            }"""

    q4 = """ SELECT ?tt ?spf
            WHERE {
                ?a rdf:type ?type .
                ?a dc:title ?tt .
                OPTIONAL{ ?a mal:spinOff ?spf . }
                FILTER (?type = dbo:Anime)
            }"""

    # Requesting the user to type the anime he wants to know related works.
    anime = input("Type the name of the anime you're looking for it's related works: ")
    anime = Literal(anime)
    print("\nWe're looking for anything related to", "\"" + str(anime) + "\"", "in our database, please wait...")

    # Doing the two query commands.
    result1 = g.query(q1, initBindings={"tt": anime})
    result2 = g.query(q2, initBindings={"tt": anime})
    result3 = g.query(q3, initBindings={"tt": anime})
    result4 = g.query(q4, initBindings={"tt": anime})

    # Printing all the data obtained if it exists.
    print("\nWorks related to:", str(anime), "\n")

    # Printing the adaptations.
    print("Adaptation(s):")
    
    for row in result1:
        if(row.ad == None):
            print("-> Unknown or Nonexistent")
        else:
            print("->", row.ad)

    print()

    # Printing the sequels.
    print("Sequel(s):")
    
    for row in result2:
        if(row.sq == None):
            print("-> Unknown or Nonexistent")
        else:
            # Changing from URI to URL
            sq = str(row.sq).split("#a")[1]
            print("-> https://myanimelist.net/anime/" + sq)

    print()

    # Printing the prequels.
    print("Prequel(s):")
    
    for row in result3:
        if(row.pq == None):
            print("-> Unknown or Nonexistent")
        else:
            # Changing from URI to URL
            pq = str(row.pq).split("#a")[1]
            print("-> https://myanimelist.net/anime/" + pq)

    print()

    # Printing the spin-offs.
    print("Spin-off(s):")
    
    for row in result4:
        if(row.spf == None):
            print("-> Unknown or Nonexistent")
        else:
            # Changing from URI to URL
            spf = str(row.spf).split("#a")[1]
            print("-> https://myanimelist.net/anime/" + spf)

    input("\nPress ENTER to continue...")