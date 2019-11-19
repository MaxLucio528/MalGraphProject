# Importando a biblioteca rdflib, mais especificamento o Graph e o Literal
# Também estou importando os namespaces usados dentro do grafo, DC, FOAF, RDF
from rdflib import Graph, Literal
from rdflib.namespace import DC, FOAF, RDF

# Função de consulta no grafo
def graphQuery(g):
    op = 1

    '''
    Aqui há 10 variáveis com comandos de query SPARQL e isso é por conta 
    de que algumas das triplas possuem mais de uma informação em si, portanto 
    em um loop, todas as informações únicas iriam se repetir novamente, logo 
    algumas das consultas estão separadas.
    '''
    q0 = """ SELECT ?tt
            WHERE {
                ?a dc:subject ?subject .
                ?a dc:title ?tt .
                FILTER (?subject = dbpedia:Anime)
            }"""

    q1 = """ SELECT ?tt ?hp ?tr ?ex ?src ?ep ?stt ?cv ?dr ?rt ?ds ?bg ?dt ?br
            WHERE {
                ?a dc:subject ?subject .
                ?a dc:title ?tt .
                ?a foaf:homepage ?hp .
                ?a mal:trailer ?tr .
                ?a mal:exhibition ?ex .
                ?a dc:source ?src .
                ?a mal:episodes ?ep .
                ?a mal:status ?stt .
                ?a dc:coverage ?cv .
                ?a mal:duration ?dr .
                ?a mal:rating ?rt .
                ?a dc:description ?ds .
                ?a mal:background ?bg .
                ?a dc:date ?dt .
                ?a mal:broadcast ?br .
                FILTER (?subject = dbpedia:Anime)
            }"""

    q2 = """ SELECT ?tt ?pd
            WHERE {
                ?a dc:subject ?subject .
                ?a dc:title ?tt .
                ?a dc:publisher ?pd .
                FILTER (?subject = dbpedia:Anime)
            }"""

    q3 = """ SELECT ?tt ?lc
            WHERE {
                ?a dc:subject ?subject .
                ?a dc:title ?tt .
                ?a dc:rights ?lc .
                FILTER (?subject = dbpedia:Anime)
            }"""

    q4 = """ SELECT ?tt ?st
            WHERE {
                ?a dc:subject ?subject .
                ?a dc:title ?tt .
                ?a dc:creator ?st .
                FILTER (?subject = dbpedia:Anime)
            }"""

    q5 = """ SELECT ?tt ?gn
            WHERE {
                ?a dc:subject ?subject .
                ?a dc:title ?tt .
                ?a dc:type ?gn .
                FILTER (?subject = dbpedia:Anime)
            }"""

    q6 = """ SELECT ?tt ?op
            WHERE {
                ?a dc:subject ?subject .
                ?a dc:title ?tt .
                ?a mal:openings ?op .
                FILTER (?subject = dbpedia:Anime)
            }"""

    q7 = """ SELECT ?tt ?ed
            WHERE {
                ?a dc:subject ?subject .
                ?a dc:title ?tt .
                ?a mal:endings ?ed .
                FILTER (?subject = dbpedia:Anime)
            }"""

    q8 = """ SELECT ?tt ?ad
            WHERE {
                ?a dc:subject ?subject .
                ?a dc:title ?tt .
                OPTIONAL{ ?a mal:adaptation ?ad . }
                FILTER (?subject = dbpedia:Anime)
            }"""

    q9 = """ SELECT ?tt ?sq
            WHERE {
                ?a dc:subject ?subject .
                ?a dc:title ?tt .
                OPTIONAL{ ?a mal:sequel ?sq . }
                FILTER (?subject = dbpedia:Anime)
            }"""

    # Laço que repete a consulta quantas vezes o usuário quiser
    while(op != 0):
        # Solicitando que o usuário digite o anime que ele quer procurar
        anime = input("Input the name of the anime you're looking for: ")
        anime = Literal(anime)
        print("\nWe're looking for", "\"" + str(anime) + "\"", "in our database, please wait...")

        # Efetuando os 10 comandos de consulta
        result0 = g.query(q0, initBindings={"tt": anime})
        result1 = g.query(q1, initBindings={"tt": anime})
        result2 = g.query(q2, initBindings={"tt": anime})
        result3 = g.query(q3, initBindings={"tt": anime})
        result4 = g.query(q4, initBindings={"tt": anime})
        result5 = g.query(q5, initBindings={"tt": anime})
        result6 = g.query(q6, initBindings={"tt": anime})
        result7 = g.query(q7, initBindings={"tt": anime})
        result8 = g.query(q8, initBindings={"tt": anime})
        result9 = g.query(q9, initBindings={"tt": anime})

        # Printando todas as informações obtidas se existirem

        print("\nInformations about:", str(anime), "\n")

        print("Title(s): ", end = "")
        for row in result0:
            print(row.tt)

        for row in result1:
            print("\nHomepage:", row.hp)
            print("\nTrailer:", row.tr)
            print("\nExhibition:", row.ex)
            print("\nSource:", row.src)
            print("\nEpisodes:", row.ep)
            print("\nStatus:", row.stt)
            print("\nCoverage:", row.cv)
            print("\nDuration:", row.dr)
            print("\nRating:", row.rt)
            print("\nDescription:", row.ds)
            print("\nBackground:", row.bg)
            print("\nDebut Data:", row.dt)
            print("\nBroadcast:", row.br)

        print("\nAdaptation(s): ", end = "")
        for row in result8:
            if(str(row.ad) == "None"):
                print("Unknown or Nonexistent")
                break
            else:
                print(row.ad)
        print()

        print("Sequel(s): ", end = "")
        for row in result9:
            if(str(row.sq) == "None"):
                print("Unknown or Nonexistent")
                break
            else:
                print(row.sq)
        print()

        print("Publisher(s): ", end = "")
        for row in result2:
            print(row.pd)
        print()

        print("Licensor(s): ", end = "")
        for row in result3:
            print(row.lc)
        print()

        print("Studio(s): ", end = "")
        for row in result4:
            print(row.st)
        print()

        print("Genres: ", end = "")
        for row in result5:
            print(row.gn)
        print()

        print("Opening(s): ", end = "")
        for row in result6:
            print(row.op)
        print()

        print("Ending(s): ", end = "")
        for row in result7:
            print(row.ed)
        print()

        # Dando a opção de se fazer outra consulta ao usuário
        print("Do you want to make another query? (1 - Yes / 0 - No)")
        op = int(input())
        print()

def main():
    print("----------------------------------------------")
    print("             Anime Graph Query v1.1           ")
    print("----------------------------------------------\n")

    '''
    Obtendo o grafo a partir do arquivo turtle, para então efetuar o parse e o
    bind dos namespaces usados dentro do arquivo.
    '''
    filename = "AnimeData.ttl"
    g = Graph()

    print("We're obtaining the database, please wait...\n")
    try:
        g.parse(filename, format="turtle")
        g.bind("mal", "https://myanimelist.net/#")
        g.bind("dbpedia", "http://dbpedia.org/page/")
        g.bind("foaf", FOAF)
        g.bind("dc", DC)

        # Chamando a função de consulta
        graphQuery(g)
    except Exception as e:
        print("\nOops! Something went wrong because of: " + str(e))
main()
