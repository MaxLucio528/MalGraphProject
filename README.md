# MalGraphProject

Made by: Max Lucio Martins de Assis

This project has the goal of generate a RDF graph from data that appear in the database of the social media MyAnimeList, also known as MAL. In the graph will appear data like title, description, episodes, exhibition date, etc. about the animes in the database.

The source of data used in theory are two, but in reality the first is a way to access the data in of the second source of data. There's a third source of data to get the definition to some things inside the graph as well:

## JikanAPI

-> Link: https://jikan.moe/

-> This is a non-official API of the social media MyAnimeList, that has diverse data of the social media available in JSON format to the user, the program pulls all the data from this API.

## MyAnimeList

-> Link: https://myanimelist.net/

-> The social media in question tha has 14000+ of animes registered, this is the database from where the API gets the data, meaning that, indirectly the program gets the data from this site as well.

## DBPedia

-> Link: http://dbpedia.org/

-> DBPedia has Linked Open Data and has a immensurable amount of information, but on this program it's used to get the definition of some ontologies and other resources.

## Process to make the RDF

After studying the data the API brings to the user in the JSON file, the conclusion that was made is that it would be best to keep only the general information, so someone that doesn't watch anime can understand the information as well, the data obtained are:

-> ID: The anime ID, only to create all the URIRefs.

-> URL: From where all the data are pulled.

-> Trailer: A trailer for the anime if it's available.

-> Title: The original anime title.

-> English Title: If available, the english title is obtained as well.

-> Exhibition: Where the anime was broadcasted (TV, DVD, BluRay, etc.).

-> Source: Where the anime was based, it it's the case.

-> Episódios: Number of episodes the anime has.

-> Status: Current situation of the anime.

-> Start Date: When the anime started.

-> End Data: When the anime ended.

-> Rating: The recommended age to watch it.

-> Description: A brief synopsis of the anime.

-> Broadcast: Time of the anime broadcast.

-> Adaptation: Name of the work the anime is based on, it it's the case.

-> Prequel: Previous history of the anime, if it's the case.

-> Sequel: Next history of the anime, if it's the case.

-> Spin-off: Alternative history of the anime, if it's the case.

-> Producers: The anime producers.

-> Licensors: Responsible for the anime licensing, if it's the case.

-> Studio: Who animated the anime.

-> Genres: The anime genres.

-> Openings: The anime openings.

-> Endings: The anime endings.

There were some other data available like score to the anime in the social media, ranking, popularity and who watched an certain anime, but like it was said before, only general information are available to the public in this program so it can be more accessible.

From the standard vocabularies, it was used the RDF to use the RDF:type only, DC (Dublin Core) for descriptions, titles and other things and OWL to indicate equality between triples.

The local vocabularies are "mal", with was used to define what were openings, endings, adaptations, etc., "schema" to define things like dates and rating, "dbo" to use some ontologies like tvShow, "dbr" to get some definitions in situations where there wasn't a ontology, and "mo" to define the openings and endings.

## Things to Know

There is three python files that the user should execute:

-> animeGrapher.py: Can create a graph with a anime and append a existing graph with new animes, the user has the option to add only one anime or set a range so the program can get all the animes in that defined range, in after the process is finished, a XML file is generated, this is where all the data is saved.

-> graphQuery.py: Can make six different types of query as long as the user gives the anime name to the program, this program can get the general information about an anime, it's related works, it's dates, it's producers, licensors and studios, it's tracks and it's genres. It's up to the user choose one of those.

-> tripleVerifier.py: Verifies the number of triples the XML file has.

-> AnimeData.xml: Has only 1 anime (My Hero Academia) to be used as example in the programs.

## Execution

-> To generate a graph, type the following:

~~~
python animeGrapher.py
~~~

-> To query in an existing graph, type the following:

~~~
python graphQuery.py
~~~

-> To check the number of triples in an existing graph, type the following:

~~~
python tripleVerifier.py
~~~

## Changelog

**Version 2.0 (15/12/2019) [FORMAT (DD/MM/YY)]**

-> Complete revamp of the program, removal of the following datas: background, coverage and season of broadcast.

-> Coverage splited in start date and end date.

-> Genres, Producers, Licensors and Studios aren't links in the graph anymore, only having it's names now.

-> Sequels now aren't links, being the URI to the anime in the graph if it is already there.

-> Prequels and Spin-Offs added.

-> Vocabularies changed for some things, ontologies attributed to things like source, producers, studios, etc.

-> Openings and Endings are separe from the animes now, having it's own vocabulary now.

-> Different query options to the user.

-> Option to add one anime or bulk add by a user-determined range.

-> And much more.

**Version 1.1 (19/11/2019) [FORMAT (DD/MM/YY)]**

-> Changes in animeQuery.py, making the version 1.1 provide a better query experience to the user; little change in a string in animeLibGrapher.py

**Version 1.0 (17/11/2019) [FORMAT (DD/MM/YY)]**

-> Program creation, it's already capable of generating a graph with all the data in turtle format, as well as auxiliary programs to make queries and a triple verifier. Made in brazilian portuguese.