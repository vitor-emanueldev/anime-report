import openpyxl
import logging

logger = logging.getLogger(__name__)

def gerar_excel(animes):
    wb = openpyxl.Workbook()
    ws = wb.active

    ws.append(["Título", "Nota", "Episódios", "Status", "Gêneros", "Sinopse"])

    for anime in animes:
        genres = ", ".join([g["name"] for g in anime["genres"]])
        title = anime["title_english"] or anime["title"]
        score = anime["score"] or "N/A"
        episodes = anime["episodes"] or "N/A"
        status = anime["status"]
        synopsis = anime["synopsis"]
        ws.append([title, score, episodes, status, genres, synopsis])

    wb.save("animes.xlsx")
    logger.info("Arquivo animes.xlsx gerado com sucesso!")