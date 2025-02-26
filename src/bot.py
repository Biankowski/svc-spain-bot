from playwright.sync_api import sync_playwright
import time
from .config import NO_APPOINTMENTS_TEXT, EMBASSY_URL
from .telegram_service import TelegramService

class AppointmentBot:
    def __init__(self):
        self.embassy_url = EMBASSY_URL
        self.telegram_service = TelegramService()
    
    def run(self):
        print("Iniciando verificação de agendamentos...")
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            
            try:
                page.goto(self.embassy_url)
                print("Acessando o site da embaixada...")
                
                page.wait_for_load_state("networkidle")
                
                print("Procurando o link de agendamento pelo XPath...")
                xpath_selector = '//*[@id="main-container"]/main/div[2]/div[1]/section/div/div[2]/div/p[4]/a'
                
                page.wait_for_selector(xpath_selector, state="visible")
                
                page.click(xpath_selector)
                print("Clicando no link de agendamento...")
                
                page.wait_for_load_state("networkidle")
                print("Página de agendamento carregada")
                
                page.on("dialog", lambda dialog: dialog.accept())
                
                page.wait_for_selector('text="Continue / Continuar"')
                page.click('text="Continue / Continuar"')
                print("Navegando para a página de agendamentos...")
                
                page.wait_for_load_state("networkidle")
                
                page_content = page.content()
                has_appointments = NO_APPOINTMENTS_TEXT not in page_content
                
                if has_appointments:
                    print("Há agendamentos disponíveis!")
                else:
                    print("Não há agendamentos disponíveis.")
                
                self.telegram_service.send_notification(has_appointments)
                
                return has_appointments
                
            except Exception as e:
                print(f"Erro durante a verificação: {str(e)}")
                self.telegram_service.send_notification(False)
                return False
            
            finally:
                time.sleep(10)
                browser.close() 