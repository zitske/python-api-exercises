#Acessar a API que fornece acesso a imagens da NASA, obtidas por um rover no planeta Marte. Qual o tipo de dado de 
# photos[4]["name"] ? 
# E de 
# photos[4]["img_src"] ?

api_key = "4UfQO88FCYEGoSjoLYa9PFAM5YychbHeUK78A8jH"

import requests
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}
response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos",query_params)
photos = response.json()["photos"]

print(photos[4]["camera"]["name"]) #Resposta: str com o nome do Rover Cameras
print(photos[4]["img_src"]) #Resposta: str com o link da imagem