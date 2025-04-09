import requests
from datetime import datetime
import os
from .config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

class TelegramService:
    def __init__(self):
        self.token = TELEGRAM_BOT_TOKEN
        self.chat_id = TELEGRAM_CHAT_ID
        self.api_url = f"https://api.telegram.org/bot{self.token}"
    
    def send_notification(self, has_appointments, custom_message=None):        
        if custom_message:
            message = custom_message
        elif has_appointments:
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
            
            response = requests.post(f"{self.api_url}/sendMessage", params=params)
            
            if response.status_code == 200:
                print(f"Mensagem enviada com sucesso para o chat ID {self.chat_id}")
                return True
            else:
                print(f"Erro ao enviar mensagem: {response.text}")
                return False
                
        except Exception as e:
            print(f"Erro ao enviar mensagem: {str(e)}")
            return False
    
    def send_screenshot(self, screenshot_path, has_appointments, custom_message=None):
        """Envia screenshot da página de agendamentos via Telegram"""
        
        if not os.path.exists(screenshot_path):
            print(f"Arquivo de screenshot não encontrado: {screenshot_path}")
            return self.send_notification(has_appointments, "Erro: Não foi possível capturar screenshot")
        
        if custom_message:
            caption = custom_message
        elif has_appointments:
            caption = "🟢 ALERTA: Há agendamentos disponíveis no site do consulado espanhol. Acesse o site para agendar."
        else:
            caption = "🔴 Não há agendamentos disponíveis no momento. Uma nova verificação será realizada posteriormente."
        
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        caption += f"\n\nVerificação realizada em: {timestamp}"
        
        try:
            with open(screenshot_path, 'rb') as photo:
                files = {'photo': photo}
                data = {
                    'chat_id': self.chat_id,
                    'caption': caption,
                    'parse_mode': 'HTML'
                }
                
                response = requests.post(f"{self.api_url}/sendPhoto", data=data, files=files)
                
                if response.status_code == 200:
                    print(f"Screenshot enviado com sucesso para o chat ID {self.chat_id}")
                    return True
                else:
                    print(f"Erro ao enviar screenshot: {response.text}")
                    return self.send_notification(has_appointments, 
                                                 f"Erro ao enviar screenshot: {response.text}. {caption}")
        
        except Exception as e:
            print(f"Erro ao enviar screenshot: {str(e)}")
            return self.send_notification(has_appointments, 
                                         f"Erro ao enviar screenshot: {str(e)}. {caption}") 