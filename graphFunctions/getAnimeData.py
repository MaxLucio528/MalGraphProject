'''
Here we import the following libraries:

1 - requests: To get the information from the source;
2 - pandas: To have better organization of the openings and endings songs
of the animes, as well as its authors;
3 - graphGenerator: Function that generates the graph.
'''

import requests
import pandas as pd
from .graphGenerator import graphGenerator

# Function responsible for getting the anime data requested.
def getAnimeData(animeID):
    # Trying to obtain the data.
    try:
        # Simple message to inform the user about what's happening.
        print("Obtaining anime " + str(animeID) + "...\n")

        # Source from where the program requests the data.
        source = "https://api.jikan.moe/v3/anime/" + str(animeID)
        # Getting the data from the source above.
        data = requests.get(source)
        # Dictionary with the data parsed in JSON.
        jsonData = data.json()

        '''
        Chain of conditions to check if anything went wrong with
        the request, all the possible errors that aren't in the
        user end (like internet connection) are treated here.
        '''
        if("status" in jsonData and jsonData["status"] == 400):
            raise Exception("Error 400: Bad Request\n")
        elif("status" in jsonData and jsonData["status"] == 404):
            raise Exception("Error 404: Anime Not Found\n")
        elif("status" in jsonData and jsonData["status"] == 405):
            raise Exception("Error 405: Method Not Allowed\n")
        elif("status" in jsonData and jsonData["status"] == 429):
            raise Exception("Error 429: Too Many Requests\n")
        elif("status" in jsonData and jsonData["status"] == 500):
            raise Exception("Error 500: Internal Server Error\n")
        # Without any errors, the program proceed to get the data.
        else:
            # The dictionary that will store all the information.
            animeData = {
                "Title": jsonData["title"],
                "Synopsis": jsonData["synopsis"],
                "URL": jsonData["url"],
                "Format": jsonData["type"],
                "Source": jsonData["source"],
                "Episodes": jsonData["episodes"],
                "Rating": jsonData["rating"]
            }

            '''
            Those conditions that check if a value on the jsonData 
            dict differ from None are from values that may be not 
            available depending on the anime, if they aren't None
            the data is stored in the dict.
            '''
            if(jsonData["aired"]["from"] != None):
                animeData["Start Date"] = jsonData["aired"]["from"].split("T")[0]
            else:
                animeData["Start Date"] = "Start date not available."

            if(jsonData["aired"]["to"] != None):
                animeData["End Date"] = jsonData["aired"]["to"].split("T")[0]
            else:
                animeData["End Date"] = "End date not available."

            if(jsonData["trailer_url"] != None):
                animeData["Trailer"] = jsonData["trailer_url"]

            if(jsonData["title_english"] != None):
                animeData["Title English"] = jsonData["title_english"]

            if(jsonData["broadcast"] != None):
                animeData["Broadcast"] = jsonData["broadcast"]

            '''
            The following data may not even be on the data obtained, 
            so it's checked if they exist, if they exist the program
            checks if the list isn't empty, then the data is obtained
            and stored on the dict.
            '''

            if ("Adaptation" in jsonData["related"] and len(jsonData["related"]["Adaptation"]) != 0):
                adapt = []
                for links in jsonData["related"]["Adaptation"]:
                    temp = str(links["url"])
                    adapt.append(temp)
                animeData["Adaptation"] = adapt

            if ("Prequel" in jsonData["related"] and len(jsonData["related"]["Prequel"]) != 0):
                prequel = []
                for links in jsonData["related"]["Prequel"]:
                    temp = str(links["mal_id"])
                    prequel.append(temp)
                animeData["Prequel"] = prequel

            if ("Side story" in jsonData["related"] and len(jsonData["related"]["Side story"]) != 0):
                sideStory = []
                for links in jsonData["related"]["Side story"]:
                    temp = str(links["mal_id"])
                    sideStory.append(temp)
                animeData["Side Story"] = sideStory

            if ("Sequel" in jsonData["related"] and len(jsonData["related"]["Sequel"]) != 0):
                sequel = []
                for links in jsonData["related"]["Sequel"]:
                    temp = str(links["mal_id"])
                    sequel.append(temp)
                animeData["Sequel"] = sequel

            if ("producers" in jsonData and len(jsonData["producers"]) != 0):
                prod = []
                for links in jsonData["producers"]:
                    temp = str(links["name"])
                    prod.append(temp)
                animeData["Producers"] = prod

            if ("licensors" in jsonData and len(jsonData["licensors"]) != 0):
                linc = []
                for links in jsonData["licensors"]:
                    temp = str(links["name"])
                    linc.append(temp)
                animeData["Licensors"] = linc

            if ("studios" in jsonData and len(jsonData["studios"]) != 0):
                studio = []
                for links in jsonData["studios"]:
                    temp = str(links["name"])
                    studio.append(temp)
                animeData["Studios"] = studio
            
            if ("genres" in jsonData and len(jsonData["genres"]) != 0):
                genres = []
                for links in jsonData["genres"]:
                    temp = str(links["name"])
                    genres.append(temp)
                animeData["Genres"] = genres
            
            '''
            A special attention is needed on the last two pieces
            of data to be obtained, because it's a string with a
            music name and the author, the program splits the music
            name and the author in two separate lists and removes
            any japanese character as well in the process.
            '''

            if ("opening_themes" in jsonData and len(jsonData["opening_themes"]) != 0):
                op = []
                bands = []
                for music in jsonData["opening_themes"]:
                    temp = str(music)
                    temp = temp.split(", by")[0]
                    temp = temp.split(" by")[0]
                    temp = temp.split(" (")[0]
                    temp = temp.replace("\"", "")
                    temp = temp.replace("<", "(")
                    temp = temp.replace(">", ")")
                    op.append(temp)
                    temp = str(music)
                    if(")\"" in temp):
                        temp = temp.split(")\" by ")[1]
                    else:
                        temp = temp.split(" by ")[1]
                    temp = temp.split(" (")[0]
                    bands.append(temp)
                opDF = pd.DataFrame(data={"Music": op, "Band": bands})
                animeData["Openings"] = opDF
            
            if ("ending_themes" in jsonData and len(jsonData["ending_themes"]) != 0):
                ed = []
                bands = []
                for music in jsonData["ending_themes"]:
                    temp = str(music)
                    temp = temp.split(", by")[0]
                    temp = temp.split(" by")[0]
                    temp = temp.split(" (")[0]
                    temp = temp.replace("\"", "")
                    temp = temp.replace("<", "(")
                    temp = temp.replace(">", ")")
                    ed.append(temp)
                    temp = str(music)
                    if(")\"" in temp):
                        temp = temp.split(")\" by ")[1]
                    else:
                        temp = temp.split(" by ")[1]
                    temp = temp.split(" (")[0]
                    bands.append(temp)
                edDF = pd.DataFrame(data={"Music": ed, "Band": bands})
                animeData["Endings"] = edDF
            '''
            Calling the function to save the data in the graph,
            we pass the animeID to create a URI unique to the anime
            on the graph, as well as the data.
            '''
            graphGenerator(animeID, animeData)
    # If anything goes wrong the program is redirected here.
    except Exception as e:
        print(e)