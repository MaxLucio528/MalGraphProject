'''
Here we import the following libraries:

1 - rdflib: To query the graph, transform the data typed by the user
in the Literal format and to define two Namespaces for a condition below.
'''
from rdflib import Graph, Literal, Namespace

# Anime query function.
def animeQuery(g):
    # Defining those namespaces to use below.
    dbr = Namespace("http://dbpedia.org/resource/")
    dbo = Namespace("http://dbpedia.org/ontology/")

    '''
    There's two variables with SPARQL commands, the first one is to display 
    all the titles the anime has, since it can be more than one it needs to 
    have a separate query.
    
    The second query displays general informations like trailer, source,
    number of episodes, start date, end date, rating, description, where it
    was broadcasted and the broadcast time.
    '''

    q1 = """ SELECT ?tt ?title
            WHERE {
                ?a rdf:type ?type .
                ?a dc:title ?tt .
                ?a dc:title ?title .
                FILTER (?type = dbo:Anime)
            }"""

    q2 = """ SELECT ?hp ?tr ?src ?ep ?stD ?eD ?rt ?ds ?fm ?br
            WHERE {
                ?a rdf:type ?type .
                ?a dc:title ?tt .
                ?a owl:sameAs ?hp .
                ?a schema:trailer ?tr .
                ?a dc:source ?src .
                ?a schema:numberOfEpisodes ?ep .
                ?a schema:contentRating ?rt .
                ?a dc:description ?ds .
                ?a dc:format ?fm .
                FILTER (?type = dbo:Anime)
            }"""

    # Requesting the user to type the anime he wants to query.
    anime = input("Type the name of the anime you're looking for: ")
    anime = Literal(anime)
    print("\nWe're looking for", "\"" + str(anime) + "\"", "in our database, please wait...")

    # Doing the two query commands.
    result1 = g.query(q1, initBindings={"tt": anime})
    result2 = g.query(q2, initBindings={"tt": anime})

    # Printing all the data obtained if it exists.
    print("\nInformations about:", str(anime), "\n")

    # Printing the titles.
    print("Title(s):")

    for row in result1:
        print("->", row.title)

    print()

    # Printing the rest of the information.
    for row in result2:
        print("Homepage:", row.hp)
        print("\nTrailer:", row.tr)
        print("\nDescription:", row.ds)

        """
        What's inside row.src is a namespace, so it's needed to be compared with
        the predefined namespaces defined above.
        """
        if(row.src == dbo.Manga):
            print("\nSource: Manga")
        elif(row.src == dbr.LightNovel):
            print("\nSource: Light Novel")
        elif(row.src == dbo.VideoGame):
            print("\nSource: Video Game")
        else:
            print("\nSource: Original")

        print("\nEpisodes:", row.ep)
        print("\nRating:", row.rt)

        """
        What's inside row.fm is a namespace, so it's needed to be compared with
        the predefined namespaces defined above.
        """
        if(row.fm == dbo.tvShow):
            print("\nFormat: TV")
        elif(row.fm == dbr.OVA):
            print("\nFormat: OVA")
        elif(row.fm == dbo.movie):
            print("\nFormat: Movie")
        elif(row.fm == dbr.Webseries):
            print("\nFormat: ONA")
        else:
            print("\nFormat: Music Video")

    input("\nPress ENTER to continue...")