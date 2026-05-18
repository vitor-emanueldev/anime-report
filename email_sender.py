import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

logger = logging.getLogger(__name__)

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
        logger.info("Email enviado com sucesso!")