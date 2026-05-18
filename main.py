from logger import configurar_logger
from coletor import coletar_animes
from excel import gerar_excel
from email_sender import enviar_email

logger = configurar_logger()
animes = coletar_animes()
gerar_excel(animes)
enviar_email()