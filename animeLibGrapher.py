'''
Aqui são importadas as seguintes bibliotecas:

1 - requests: Para obter as informações da rede;
2 - json: Devido as informações obtidas serem em JSON, usa-se esta
biblioteca;
3 - time: Para que ocorra uma espera de um segundo entre os requests,
evitando limitação de acesso pela API;
4 - rdflib: importando Graph para criar o grafo, Namespace para criar os
namespaces necessários, literal para inserir os dados no grafo, além de
importar alguns namespaces pré-definidos.
'''
import requests
import json
import time
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import DC, FOAF, RDF

# Função que obtém a definição de anime
def getAnime():
    try:
        # Link para se fazer o request
        baseSource = "http://dbpedia.org/data/Anime.json"
        # Obtendo os dados em json
        data = requests.get(baseSource)
        jsonData = json.loads(data.content)

        # Salvando os dados obtidos
        title = "Anime"
        temp = jsonData["http://dbpedia.org/resource/Anime"]["http://dbpedia.org/ontology/abstract"]
        for x in temp:
            if(x["lang"] == "en"):
                desc = x["value"]
        url = baseSource

        # Colocando os dados obtidos em uma lista
        baseData = []
        baseData.append(title)
        baseData.append(desc)
        baseData.append(url)

        return baseData

    except Exception as e:
        print("Erro! Algo deu errado por conta de: " + str(e))

# Função que obtém todos os animes
def getAnimeData():
    try:
        # Link para se fazer o request
        source = "https://api.jikan.moe/v3/anime/"

        # Lista que guarda os dictionaries dos animes
        animesData = []

        '''
        Este loop obtém todos os dados de animes cadastrados na 
        fonte em que se pega os dados.
        '''
        for x in range(1, 40730):
            data = requests.get(source + str(x))
            jsonData = json.loads(data.content)

            '''
            A frequência para requisição de dados é de 2 requests
            por segundo, por isso quando se chega em qualquer número
            em que o resto de divisão por três é zero, aguarda-se um
            segundo para obter mais dados.
            '''
            if ((x % 3) == 0):
                time.sleep(1)
            
            '''
            Alguns IDs não existem na base de dados que a API consulta,
            por isso no JSON há o nome do código da resposta, porém isso 
            apenas aparece quando algo da errado, por isso sempre que algo 
            der errado, a consulta do número em questão é pulada.
            '''
            if(jsonData["type"] == "BadResponseException"):
                continue
            else:
                # Salvando dados únicos dos animes disponíveis na base de dados
                animeData = {
                    "ID": jsonData["mal_id"],
                    "URL": jsonData["url"],
                    "Trailer": jsonData["trailer_url"],
                    "Title": jsonData["title"],
                    "Title_English": jsonData["title_english"],
                    "Exhibition": jsonData["type"],
                    "Source": jsonData["source"],
                    "Episodes": jsonData["episodes"],
                    "Status": jsonData["status"],
                    "Date": jsonData["aired"]["string"],
                    "Duration": jsonData["duration"],
                    "Rating": jsonData["rating"],
                    "Synopsis": jsonData["synopsis"],
                    "Background": jsonData["background"],
                    "Debut_Date": jsonData["premiered"],
                    "Broadcast": jsonData["broadcast"]
                }

                '''
                Animes podem ser adaptações de outras obras, e em alguns casos
                raros, de mais de uma obra, logo este loop verifica se o anime
                é uma adaptação, se for ele salva todas as disponíveis.
                '''
                if ("Adaptation" in jsonData["related"]):
                    adapt = []
                    for links in jsonData["related"]["Adaptation"]:
                        temp = str(links)
                        temp = temp.split("'url': '")[1]
                        temp = temp.split("'")[0]
                        adapt.append(temp)
                    animeData["Adaptation"] = adapt

                '''
                Animes podem ter continuações, e em alguns casos raros, múltiplas
                continuações paralelas, logo este loop verifica se o anime tem
                continuações, se tiver ele salva todas as disponíveis.
                '''
                if ("Sequel" in jsonData["related"]):
                    temp = str(jsonData["related"]["Sequel"])
                    temp = temp.split("'url': '")[1]
                    temp = temp.split("'")[0]
                    animeData["Sequel"] = temp

                '''
                Animes possuem um ou mais produtores, se houver informações sobre
                os produtores, o programa salva as informações disponíveis.
                '''
                if (jsonData["producers"] != []):
                    prod = []
                    for links in jsonData["producers"]:
                        temp = str(links)
                        temp = temp.split("'url': '")[1]
                        temp = temp.split("'")[0]
                        prod.append(temp)
                    animeData["Producers"] = prod

                '''
                Animes possuem um ou mais licenciadores, se houver informações sobre
                os licenciadores, o programa salva as informações disponíveis.
                '''
                if (jsonData["licensors"] != []):
                    licensors = []
                    for links in jsonData["licensors"]:
                        temp = str(links)
                        temp = temp.split("'url': '")[1]
                        temp = temp.split("'")[0]
                        licensors.append(temp)
                    animeData["Licensors"] = licensors

                '''
                Animes possuem um ou mais estúdios que o animaram, se houver informações
                sobre os estúdios, o programa salva as informações disponíveis.
                '''
                if (jsonData["studios"] != []):
                    studios = []
                    for links in jsonData["studios"]:
                        temp = str(links)
                        temp = temp.split("'url': '")[1]
                        temp = temp.split("'")[0]
                        studios.append(temp)
                    animeData["Studios"] = studios

                '''
                Animes possuem um ou mais gêneros, se houver informações sobre
                os gêneros, o programa salva as informações disponíveis.
                '''
                if (jsonData["genres"] != []):
                    genres = []
                    for links in jsonData["genres"]:
                        temp = str(links)
                        temp = temp.split("'url': '")[1]
                        temp = temp.split("'")[0]
                        genres.append(temp)
                    animeData["Genres"] = genres

                '''
                Animes possuem nenhuma ou pelo menos uma abertura, se houver informações
                sobre as aberturas, o programa salva as informações disponíveis.
                '''
                if (jsonData["opening_themes"] != []):
                    op = []
                    for music in jsonData["opening_themes"]:
                        temp = str(music)
                        op.append(temp)
                    animeData["Openings"] = op

                '''
                Animes possuem nenhum ou pelo menos um encerramento, se houver informações
                sobre os encerramentos, o programa salva as informações disponíveis.
                '''
                if (jsonData["ending_themes"] != []):
                    end = []
                    for music in jsonData["ending_themes"]:
                        temp = str(music)
                        end.append(temp)
                    animeData["Endings"] = end

                '''
                Loop de tratamento de informações não existentes, caso haja alguma situação 
                dessas, é definido um texto padrão para tratar da ausência destas informações.
                '''
                for key, data in animeData.items():
                    if ((data == None) or (data == "Unknown")):
                        if(key == "Title_English"):
                            animeData["Title_English"] = "No English title"
                        else:
                            animeData[key] = "Unknown or Nonexistent"

                # Salvando dados em uma lista
                animesData.append(animeData)
                print("Anime", x, "obtained.")

        return animesData
    except Exception as e:
        print("\nOops! Something went wrong because of: " + str(e))

# Função que monta o grafo
def graphGenerator(anime, animeData):
    # Criando o grafo e definido dois namespaces customizados
    g = Graph()
    mal = Namespace("https://myanimelist.net/#")
    dbpedia = Namespace("http://dbpedia.org/page/")

    # Salvando definições de anime no grafo
    g.add((mal.Anime, RDF.type, FOAF.Project))
    g.add((mal.Anime, DC.title, Literal(anime[0])))
    g.add((mal.Anime, DC.description, Literal(anime[1])))
    g.add((mal.Anime, DC.homepage, Literal(anime[2])))

    # Salvando as informações dos animes no grafo
    for x in animeData:
        g.add((mal.a + str(x["ID"]), RDF.type, mal.Anime))
        g.add((mal.a + str(x["ID"]), DC.subject, dbpedia.Anime))
        g.add((mal.a + str(x["ID"]), FOAF.homepage, Literal(x["URL"])))
        g.add((mal.a + str(x["ID"]), mal.trailer, Literal(x["Trailer"])))
        g.add((mal.a + str(x["ID"]), DC.title, Literal(x["Title"])))
        g.add((mal.a + str(x["ID"]), DC.title, Literal(x["Title_English"])))
        g.add((mal.a + str(x["ID"]), mal.exhibition, Literal(x["Exhibition"])))
        g.add((mal.a + str(x["ID"]), DC.source, Literal(x["Source"])))
        g.add((mal.a + str(x["ID"]), mal.episodes, Literal(x["Episodes"])))
        g.add((mal.a + str(x["ID"]), mal.status, Literal(x["Status"])))
        g.add((mal.a + str(x["ID"]), DC.coverage, Literal(x["Date"])))
        g.add((mal.a + str(x["ID"]), mal.duration, Literal(x["Duration"])))
        g.add((mal.a + str(x["ID"]), mal.rating, Literal(x["Rating"])))
        g.add((mal.a + str(x["ID"]), DC.description, Literal(x["Synopsis"])))
        g.add((mal.a + str(x["ID"]), mal.background, Literal(x["Background"])))
        g.add((mal.a + str(x["ID"]), DC.date, Literal(x["Debut_Date"])))
        g.add((mal.a + str(x["ID"]), mal.broadcast, Literal(x["Broadcast"])))
        '''
        Animes podem ou não ser adatações de outras obras, prevenindo erros caso
        não este não seja o caso por meio deste if.
        '''
        if("Adaptation" in x):
            for info in x["Adaptation"]:
                g.add((mal.a + str(x["ID"]), mal.adaptation, Literal(info)))
        else:
            g.add((mal.a + str(x["ID"]), mal.adaptation, Literal("Unknown or Nonexistent")))
        '''
        Animes podem ou não ter continuações, prevenindo erros caso não este não 
        seja o caso por meio deste if.
        '''
        if("Sequel" in x):
            g.add((mal.a + str(x["ID"]), mal.sequel, Literal(x["Sequel"])))
        else:
            g.add((mal.a + str(x["ID"]), mal.sequel, Literal("Unknown or Nonexistent")))
        # Evitando erros, caso esta informação não exista
        if("Producers" in x):
            for info in x["Producers"]:
                g.add((mal.a + str(x["ID"]), DC.publisher, Literal(info)))
        else:
            g.add((mal.a + str(x["ID"]), DC.publisher, Literal("Unknown or Nonexistent")))
        '''
        Animes podem ou não ter licenciadores, prevenindo erros caso não este não 
        seja o caso por meio deste if.
        '''
        if("Licensors" in x):    
            for info in x["Licensors"]:    
                g.add((mal.a + str(x["ID"]), DC.rights, Literal(info)))
        else:
            g.add((mal.a + str(x["ID"]), DC.rights, Literal("Unknown or Nonexistent")))
        # Evitando erros, caso as informações abaixo não existam
        if("Studios" in x):
            for info in x["Studios"]:
                g.add((mal.a + str(x["ID"]), DC.creator, Literal(info)))
        else:
            g.add((mal.a + str(x["ID"]), DC.creator, Literal("Unknown or Nonexistent")))
        if("Genres" in x):
            for info in x["Genres"]:
                g.add((mal.a + str(x["ID"]), DC.type, Literal(info)))
        else:
            g.add((mal.a + str(x["ID"]), DC.type, Literal("Unknown or Nonexistent")))
        if("Openings" in x):
            for info in x["Openings"]:
                g.add((mal.a + str(x["ID"]), mal.openings, Literal(info)))
        else:
            g.add((mal.a + str(x["ID"]), mal.openings, Literal("Unknown or Nonexistent")))
        if("Endings" in x):
            for info in x["Endings"]:
                g.add((mal.a + str(x["ID"]), mal.endings, Literal(info)))
        else:
            g.add((mal.a + str(x["ID"]), mal.endings, Literal("Unknown or Nonexistent")))

    # Bind dos namespaces customizados e renomeando dois namespaces padrões
    g.bind("dbpedia", dbpedia)
    g.bind("mal", mal)
    g.bind("foaf", FOAF)
    g.bind("dc", DC)

    # Tentando salvar o grafo em formato turtle
    try:
        g.serialize(destination=f"AnimeData.ttl", format="turtle")
        print("\nGraph created successfully!")
    # Caso algo de errado, toda a operação é cancelada
    except Exception as e:
        print("\nOops! Couldn't create the graph because of: " + str(e))

'''       
Função main que controla todas as outras funções e mostra situação do programa
para o usuário. 
'''
def main():
    print("----------------------------------------------")
    print("          Anime Graph Generator v1.0          ")
    print("----------------------------------------------\n")
    try:
        # Chamando funções de obtenção de dados
        print("We're collecting the data, please wait...\n")
        print("Obtaining animes...")
        anime = getAnime()
        animeData = getAnimeData()

        # Chamando função geradora do grafo
        print("\nGenerating the graph, please wait...")
        graphGenerator(anime, animeData)
    except Exception as e:
        print("\nOops! Something went wrong because of: " + str(e))

# Iniciando o programa
main()