import requests
import json
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

ws.append(["Título", "Nota", "Episódios", "Status", "Gêneros", "Sinopse"])


params = {
    "limit": 2,
    "filter": "tv"
}


request = requests.get('https://api.jikan.moe/v4/seasons/now', params=params)
request = request.json()
print(json.dumps(request, indent=4, ensure_ascii=False))

for anime in request["data"]:
    genres = ", ".join([g["name"] for g in anime["genres"]])
    title = anime["title_english"] or anime["title"]
    score = anime["score"]
    episodes = anime["episodes"]
    status = anime["status"]
    synopsis = anime["synopsis"]
    ws.append([title, score, episodes, status, genres, synopsis])

wb.save("animes.xlsx")