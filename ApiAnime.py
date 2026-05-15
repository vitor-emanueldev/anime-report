import requests
import json
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

ws.append(["Título", "Nota", "Episódios", "Status", "Gêneros", "Sinopse"])

page = 1
ids_vistos = set()

while True:
    params = {
        "filter": "tv",
        "page": page
    }


    request = requests.get('https://api.jikan.moe/v4/seasons/now', params=params)
    request = request.json()
    print(json.dumps(request, indent=4, ensure_ascii=False))

    for anime in request["data"]:
        mal_id = anime["mal_id"]

        if mal_id in ids_vistos:
            continue

        ids_vistos.add(mal_id)
        
        genres = ", ".join([g["name"] for g in anime["genres"]])
        title = anime["title_english"] or anime["title"]
        score = anime["score"] or "N/A"
        episodes = anime["episodes"] or "N/A"
        status = anime["status"]
        synopsis = anime["synopsis"]
        ws.append([title, score, episodes, status, genres, synopsis])

    if not request["pagination"]["has_next_page"]:
        break
            
    page += 1
    
wb.save("animes.xlsx")
