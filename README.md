# MalGraphProject

Feito por: Max Lucio Martins de Assis

Este projeto tem como objetivo gerar um grafo RDF a partir das informações que constam na base de dados da rede social MyAnimeList, conhecida também como Mal. No grafo constarão informações como título, descrição, episódios, época de exibição, etc. sobre os animes que estão presentes na base de dados.

As fontes de dados utilizadas na teoria são duas, mas na realidade a primeira é um meio para acessar as informações da segunda fonte de dados:

## JikanAPI

-> Link: https://jikan.moe/

-> Esta é uma API não-oficial da rede social MyAnimeList, que disponibiliza informações diversas contidas na rede social em formato .json para o usuário, o programa puxa todos os dados a partir da API.

## MyAnimeList

-> Link: https://myanimelist.net/

-> A rede social em si que possui mais de 14000 animes registrados, esta é a base de dados de onde a API pega as informações, ou seja, indiretamente o programa pega as informações deste site também.

## DBPedia

-> Link: http://dbpedia.org/

-> Base de dados de inúmeras coisas, usei o DBPedia para obter a definição geral de anime, que está no centro de tudo no grafo e todos os outros animes são ligados a tal tripla com estas informações.

## Processo de erredeificação

Eu estudei as informações que a API trás para o usuário no arquivo .json e cheguei a conclusão de que as informações que eu desejava que fossem armazenadas e disponibilizadas para o usuário fossem:

-> ID: O ID do anime na rede social.

-> URL: A URL de onde foram tiradas as informações.

-> Trailer: O Trailer do anime se este estiver disponível.

-> Título: O Título original do anime.

-> Título em inglês: Se houver, o título em inglês do anime.

-> Exibição: Onde o anime foi exibido (TV, DVD, BluRay, etc.).

-> Fonte: Tipo de obra que o anime se baseou, se for o caso.

-> Episódios: Número de episódios do anime.

-> Status: Situação atual do anime.

-> Datas: Período de início do anime e fim do anime se for o caso.

-> Classificação Indicativa: Idades para qual o anime é recomendado.

-> Sinopse: Descrição da história do anime.

-> Cenário: O que levou à criação do anime, se for o caso.

-> Temporada: Em que temporada de animes (Estações do ano), ocorreu a estréia.

-> Transmissão: Horário de exibição do anime.

-> Adaptação: Nome da obra em que o anime se baseou, sendo este o caso.

-> Continuação: Continuação do anime, se houver.

-> Produtores: Produtores do anime.

-> Licenciadores: Responsáveis pelo licenciamento do anime, se for o caso.

-> Estúdio: Estúdio que animou o anime.

-> Gêneros: Gêneros que o anime possui.

-> Abertura: Aberturas que o anime possui.

-> Encerramento: Encerramentos que o anime possui.

Haviam mais algumas informações disponíveis como notas para o anime naquela rede social, ranking, popularidade e pessoas que assistiram esse anime, que estão presentes na rede social, mas o meu objetivo foi trazer informações mais gerais para as pessoas e não coisas específicas da rede social.

Fora isso há uma tripla específica que é sobre a definição de anime, em que todos os animes são ligados também, tendo o título, descrição sobre o que é anime e a URL também.

Os vocabulários usados são o RDF, para definir o RDF.type de cada um dos animes e da definição geral, FOAF apenas para as URLs e para o tipo da definição geral, que é do tipo FOAF.Project. Além disso o outro vocabulários usado é o Dublin Core, que é usado para títulos, descrições, gêneros, fontes, tempo de exibição, data de estréia, produtores, licenciadores, estúdios e assunto.

Por fim dois vocabulários locais, sendo eles o mal e o dbpedia, onde mal guarda o restante das informações sobre os animes e o dbpedia é para que o assunto (Salvo como DC.subject) de cada um dos animes sejam referenciados à página sobre animes no DBPedia.

## Outras informações

Há três arquivos .py presentes para o usuário: 

-> animeLibGrapher.py: O responsável pela criação do grafo, onde o próprio usuário define os animes que quer salvar no grafo a partir de seus IDs ao editar o código, no fim é gerado um arquivo .ttl onde todas as informações são salvas.

-> animeQuery.py: Que permite que o usuário digite o nome de um anime e então o programa efetua uma consulta SPARQL dentro do arquivo .ttl gerado pelo arquivo .py anterior a este.

-> tripleVerifier.py: O próprio nome diz o que ele faz, ele simplesmente tem a função de verificar quantas triplas o grafo no arquivo .ttl possui.

## Changelog

**Versão 1.0 (17/11/2019)**

-> Criação do programa, sendo ele capaz de gerar o grafo com todas as informações, além de programas auxiliares para consulta e verificação de triplas.