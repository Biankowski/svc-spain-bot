import requests
from datetime import datetime
from .config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

class TelegramService:
    def __init__(self):
        self.token = TELEGRAM_BOT_TOKEN
        self.chat_id = TELEGRAM_CHAT_ID
        self.api_url = f"https://api.telegram.org/bot{self.token}/sendMessage"
    
    def send_notification(self, has_appointments):        
        if has_appointments:
            message = "🟢 ALERTA: Há agendamentos disponíveis no site do consulado espanhol. Acesse o site para agendar."
        else:
            message = "🔴 Não há agendamentos disponíveis no momento. Uma nova verificação será realizada posteriormente."
        
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        message += f"\n\nVerificação realizada em: {timestamp}"
        
        try:
            params = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            
            response = requests.post(self.api_url, params=params)
            
            if response.status_code == 200:
                print(f"Mensagem enviada com sucesso para o chat ID {self.chat_id}")
                return True
            else:
                print(f"Erro ao enviar mensagem: {response.text}")
                return False
                
        except Exception as e:
            print(f"Erro ao enviar mensagem: {str(e)}")
            return False 