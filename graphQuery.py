'''
Here we import the following libraries:

1 - rdflib: To parse the graph in the XML file;
2 - rdflib.namespace: To bind the default namespaces used in the graph;
3 - queryFunctions.animeQuery: To use the animeQuery() function;
4 - queryFunctions.relatedQuery: To use the relatedQuery() function;
5 - queryFunctions.dateQuery: To use the dateQuery() function;
6 - queryFunctions.companyQuery: To use the companyQuery() function;
7 - queryFunctions.trackQuery: To use the trackQuery() function;
8 - queryFunctions.genreQuery: To use the genreQuery() function;
9 - generalFunctions.clearScreen: To use the clear() function.
'''
from rdflib import Graph
from rdflib.namespace import DC, RDF, OWL
from queryFunctions.animeQuery import animeQuery
from queryFunctions.relatedQuery import relatedQuery
from queryFunctions.dateQuery import dateQuery
from queryFunctions.companyQuery import companyQuery
from queryFunctions.trackQuery import trackQuery
from queryFunctions.genreQuery import genreQuery
from generalFunctions.clearScreen import clear

def main():
    clear()

    '''
    Obtaining the graph from the XML file, so the program can parse it and bind
    the namespaces used inside the file.
    '''
    filename = "AnimeData.xml"
    g = Graph()

    print("We're obtaining the database, please wait...\n")

    clear()

    try:
        # Parsing the XML file and binding the namespaces.
        g.parse(filename)
        g.bind("mal", "https://myanimelist.net/#")
        g.bind("schema", "http://schema.org/")
        g.bind("dbr", "http://dbpedia.org/resource/")
        g.bind("dbo", "http://dbpedia.org/ontology/")
        g.bind("mo", "http://purl.org/ontology/mo/")
        g.bind("rdf", RDF)
        g.bind("dc", DC)
        g.bind("owl", OWL)

        '''
        This is the option variable that determines what the program gonna do
        or if the program will continue running or not. 
        '''
        op = -1

        # Loop that runs the program while the user wants.
        while(op != 0):
            # Printing the Main Menu.
            print("----------------------------------------------")
            print("             Anime Graph Query v2.0           ")
            print("----------------------------------------------\n")
            print("1 - Query General Information")
            print("2 - Query Related Works")
            print("3 - Query Anime Dates")
            print("4 - Query Anime Producers, Licensors and Studios")
            print("5 - Query Anime Tracks")
            print("6 - Query Anime Genres")
            print("0 - Exit")
            
            # Getting the option the user selected.
            op = int(input("\nPlease select a option: "))
            print()

            # General Infomation about an anime.
            if(op == 1):
                clear()
                animeQuery(g)
                clear()

            # Works related to an anime.
            elif(op == 2):
                clear()
                relatedQuery(g)
                clear()

            # Dates of an anime.
            elif(op == 3):
                clear()
                dateQuery(g)
                clear()

            # Producers, Licensors and Studios of an anime.
            elif(op == 4):
                clear()
                companyQuery(g)
                clear()

            # Tracks of an anime.
            elif(op == 5):
                clear()
                trackQuery(g)
                clear()

            # Genres of an anime.
            elif(op == 6):
                clear()
                genreQuery(g)
                clear()

            # Exiting the program.
            elif(op == 0):
                clear()
                print("Program terminated...\n")
                exit()

            # Invalid number.
            else:
               print("Invalid number! Please try again...\n")
               input("Press ENTER to continue...")
               clear()
    
    # If anything goes wrong with thoses processes the program is redirected here.
    except Exception as e:
        print("\n", e)

# Starting the program.
main()