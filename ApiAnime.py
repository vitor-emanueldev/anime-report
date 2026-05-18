import requests
import json
import openpyxl
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler("anime_report.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

wb = openpyxl.Workbook()
ws = wb.active

ws.append(["Título", "Nota", "Episódios", "Status", "Gêneros", "Sinopse"])

total = 0
page = 1
ids_vistos = set()

logging.info("Iniciando coleta de dados...")

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
        total += 1

    if not request["pagination"]["has_next_page"]:
        break      
    page += 1

logging.info(f"{page} Páginas coletadas")  
logging.info(f"Total: {total} animes salvos")
wb.save("animes.xlsx")
logging.info("Arquivo animes.xlsx gerado com sucesso")

def enviar_email():
    remetente = "vitoremanuelxd753@gmail.com"
    destinatario = "vitoremanuelxd753@gmail.com"
    senha = "vhdk qmgn eaeg ykzo"

    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = "Anime Report - Temporada Atual"

    msg.attach(MIMEText("Segue em anexo o relatório de animes da temporada atual.", "plain"))

    with open("animes.xlsx", "rb") as f:
        anexo = MIMEBase("application", "octet-stream")
        anexo.set_payload(f.read())
        encoders.encode_base64(anexo)
        anexo.add_header("Content-Disposition", "attachment; filename=animes.xlsx")
        msg.attach(anexo)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
        logging.info("Email enviado com sucesso!")

enviar_email()