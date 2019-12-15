'''
Here we import the following libraries:

1 - pandas: To have better organization of the openings and endings songs
of the animes, as well as its authors;
2 - rdflib: To create the graph, and Namespace is to create the necessary namespaces,
Literal is to add data to the graph;
3 - rdflib.namespace: To import predefined namespaces.
'''

import pandas as pd
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import DC, RDF, OWL

# Function that makes the graph or append the data in the graph.
def graphGenerator(animeID, animeData):
    # The file name of the graph.
    filename = "AnimeData.xml"

    # Creating the graph and defining the namespaces.
    g1 = Graph()
    mal = Namespace("https://myanimelist.net/#")
    dbr = Namespace("http://dbpedia.org/resource/")
    dbo = Namespace("http://dbpedia.org/ontology/")
    mo = Namespace("http://purl.org/ontology/mo/")
    schema = Namespace("http://schema.org/")

    # Adding the initial data on the graph.
    g1.add((mal.a + str(animeID), RDF.type, dbo.Anime))
    g1.add((mal.a + str(animeID), DC.title, Literal(animeData["Title"])))
    g1.add((mal.a + str(animeID), OWL.sameAs, Literal(animeData["URL"])))
    g1.add((mal.a + str(animeID), DC.description, Literal(animeData["Synopsis"])))

    # If the anime has a english title, it's added as well.
    if("Title English" in animeData):
        g1.add((mal.a + str(animeID), DC.title, Literal(animeData["Title English"])))

    # If the anime has a trailer, it's added.
    if("Trailer" in animeData):
        g1.add((mal.a + str(animeID), schema.trailer, Literal(animeData["Trailer"])))

    '''
    Adding where the anime was broadcasted, the way it's added
    on the graph depends on where it was broadcasted.
    '''
    if(animeData["Format"] == "TV"):
        g1.add((mal.a + str(animeID), DC["format"], dbo.tvShow))
    elif(animeData["Format"] == "OVA" or animeData["Format"] == "Special"):
        g1.add((mal.a + str(animeID), DC["format"], dbr.OVA))
    elif(animeData["Format"] == "Movie"):
        g1.add((mal.a + str(animeID), DC["format"], dbo.movie))
    elif(animeData["Format"] == "ONA"):
        g1.add((mal.a + str(animeID), DC["format"], dbr.Webseries))
    else:
        g1.add((mal.a + str(animeID), DC["format"], dbr.Musicvideo))

    '''
    Adding the type of material that the anime was based,
    there is five types of material to be based on and what
    goes in the graph depends on this.
    '''
    if(animeData["Source"] == "Manga"):
        g1.add((mal.a + str(animeID), DC.source, dbo.Manga))
    elif(animeData["Source"] == "Light Novel"):
        g1.add((mal.a + str(animeID), DC.source, dbo.LightNovel))
    elif(animeData["Source"] == "Visual Novel" or animeData["Source"] == "Game"):
        g1.add((mal.a + str(animeID), DC.source, dbo.VideoGame))
    elif(animeData["Source"] == "Original"):
        g1.add((mal.a + str(animeID), DC.source, Literal("Original")))

    # Adding other information that doesn't need to be verified.
    g1.add((mal.a + str(animeID), schema.numberOfEpisodes, Literal(animeData["Episodes"])))
    g1.add((mal.a + str(animeID), schema.startDate, Literal(animeData["Start Date"])))
    g1.add((mal.a + str(animeID), schema.endDate, Literal(animeData["End Date"])))
    g1.add((mal.a + str(animeID), schema.contentRating, Literal(animeData["Rating"])))

    # If the broadcast time is available, it's added as well.
    if("Broadcast" in animeData):
        g1.add((mal.a + str(animeID), schema.startTime, Literal(animeData["Broadcast"])))

    '''
    Checking if there is the following information on the dict,
    having the information it's added on the graph by looping on
    the list that contains all the adaptations, sequels, etc.
    '''
    if("Adaptation" in animeData):
        for x in animeData["Adaptation"]:
            g1.add((mal.a + str(animeID), mal.adaptation, Literal(x)))

    if("Prequel" in animeData):
        for x in animeData["Prequel"]:
            g1.add((mal.a + str(animeID), mal.prequel, mal.a + str(x)))

    if("Side Story" in animeData):
        for x in animeData["Side Story"]:
            g1.add((mal.a + str(animeID), mal.spinOff, mal.a + str(x)))
    
    if("Sequel" in animeData):
        for x in animeData["Sequel"]:
            g1.add((mal.a + str(animeID), mal.sequel, mal.a + str(x)))

    if("Producers" in animeData):
        for x in animeData["Producers"]:
            g1.add((mal.a + str(animeID), dbo.producer, Literal(x)))

    if("Licensors" in animeData):
        for x in animeData["Licensors"]:
            g1.add((mal.a + str(animeID), schema.copyrightHolder, Literal(x)))

    if("Studios" in animeData):
        for x in animeData["Studios"]:
            g1.add((mal.a + str(animeID), schema.productionCompany, Literal(x)))

    if("Genres" in animeData):
        for x in animeData["Genres"]:
            g1.add((mal.a + str(animeID), dbo.genre, Literal(x)))

    '''
    The openings and endings are added in a separate URI unique to them,
    with the track name and it's band, after that they are connected to
    the anime URI.
    '''
    if("Openings" in animeData):
        for index, row in animeData["Openings"].iterrows():
            g1.add((mal.op + str(int(index) + 1) + "-" + str(animeID), RDF.type, mo.MusicalWork))
            g1.add((mal.op + str(int(index) + 1) + "-" + str(animeID), mo.Track, Literal(row["Music"])))
            g1.add((mal.op + str(int(index) + 1) + "-" + str(animeID), mo.MusicArtist, Literal(row["Band"])))
            g1.add((mal.a + str(animeID), mal.opening, mal.op + str(int(index) + 1) + "-" + str(animeID)))

    if("Endings" in animeData):
        for index, row in animeData["Endings"].iterrows():
            g1.add((mal.ed + str(int(index) + 1) + "-" + str(animeID), RDF.type, mo.MusicalWork))
            g1.add((mal.ed + str(int(index) + 1) + "-" + str(animeID), mo.Track, Literal(row["Music"])))
            g1.add((mal.ed + str(int(index) + 1) + "-" + str(animeID), mo.MusicArtist, Literal(row["Band"])))
            g1.add((mal.a + str(animeID), mal.ending, mal.ed + str(int(index) + 1) + "-" + str(animeID)))

    # Trying to append the data to a existing graph.
    try:
        # Obtaining a existing graph.
        g2 = Graph()
        g2.parse(filename)

        # Appending the data to be added with the existing file.
        graph = g2 + g1

        # Binding the namespaces.
        graph.bind("mal", mal)
        graph.bind("schema", schema)
        graph.bind("dbr", dbr)
        graph.bind("dbo", dbo)
        graph.bind("mo", mo)
        graph.bind("rdf", RDF)
        graph.bind("dc", DC)
        graph.bind("owl", OWL)

        # Replacing the file with all the data stored in it.
        graph.serialize(filename)
        # Notifying the user about the anime that was added.
        print("Anime", animeID, "added to the graph.\n")
    # If the graph file doesn't exist yet, it's created.
    except:
        # Binding the namespaces.
        g1.bind("mal", mal)
        g1.bind("schema", schema)
        g1.bind("dbr", dbr)
        g1.bind("dbo", dbo)
        g1.bind("mo", mo)
        g1.bind("rdf", RDF)
        g1.bind("dc", DC)
        g1.bind("owl", OWL)

        # Creatng the graph.
        g1.serialize(filename)
        # Notifying the user about the anime that was added.
        print("Anime", animeID, "added to the graph.\n")