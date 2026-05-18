import requests
import logging

logger = logging.getLogger(__name__)

def coletar_animes():
    animes = []
    ids_vistos = set()
    page = 1

    while True:
        params = {
            "filter": "tv",
            "page": page
        }


        request = requests.get('https://api.jikan.moe/v4/seasons/now', params=params)
        request = request.json()

        for anime in request["data"]:
            mal_id = anime["mal_id"]

            if mal_id in ids_vistos:
                continue

            ids_vistos.add(mal_id)
            animes.append(anime)
            
        logger.info(f"Página {page} coletada - {len(request['data'])} animes")

        if not request["pagination"]["has_next_page"]:
            break      
        page += 1

    logging.info(f"{page} Páginas coletadas")  
    logging.info(f"Total: {len(animes)} animes salvos")
    return animes