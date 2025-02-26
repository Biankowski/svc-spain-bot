import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

EMBASSY_URL = "https://www.exteriores.gob.es/Embajadas/brasilia/pt/Embajada/Paginas/Cita-previa.aspx"
NO_APPOINTMENTS_TEXT = "No hay horas disponibles" 