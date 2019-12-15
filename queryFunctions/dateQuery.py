'''
Here we import the following libraries:

1 - rdflib: To query the graph, transform the data typed by the user
in the Literal format.
'''
from rdflib import Graph, Literal

# Date query function.
def dateQuery(g):
    '''
    This variable is SPARQL command that looks for the Start Date, End Date
    and the broadcast time of an anime the user gives the name.
    '''

    q1 = """ SELECT ?stD ?eD ?br
            WHERE {
                ?a rdf:type ?type .
                ?a dc:title ?tt .
                ?a schema:startDate ?stD .
                ?a schema:endDate ?eD .
                ?a schema:startTime ?br .
                FILTER (?type = dbo:Anime)
            }"""

    # Requesting the user to type the anime he wants to know the dates.
    anime = input("Type the name of the anime you're looking for the dates: ")
    anime = Literal(anime)
    print("\nWe're looking for dates of", "\"" + str(anime) + "\"", "in our database, please wait...")

    # Doing the query command.
    result1 = g.query(q1, initBindings={"tt": anime})

    # Printing all the data obtained if it exists.
    print("\nDates of:", str(anime), "\n")

    # Printing start and end dates, and well as the broadcast time.
    for row in result1:
        print("Started airing at:", row.stD)
        print("Finished airing at:", row.eD)
        print("Broadcast:", row.br)

    input("\nPress ENTER to continue...")