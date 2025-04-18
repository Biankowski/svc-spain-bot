from playwright.sync_api import sync_playwright
import time
import os
from datetime import datetime
from .config import NO_APPOINTMENTS_TEXT
from .telegram_service import TelegramService

class AppointmentBot:
    def __init__(self, browser_type="firefox"):
        self.embassy_url = "https://www.exteriores.gob.es/Embajadas/brasilia/pt/Embajada/Paginas/Cita-previa.aspx"
        self.telegram_service = TelegramService()
        self.screenshot_path = "appointment_status.png"
        self.browser_type = browser_type.lower()
    
    def run(self):
        print("Iniciando verificação de agendamentos...")
        
        with sync_playwright() as p:

            browser_launcher = getattr(p, self.browser_type)
            browser = browser_launcher.launch(headless=False)
            context = browser.new_context()
            
            # Configurar contexto para não usar cache
            context = browser.new_context(
                bypass_csp=True,  # Ignora política de segurança de conteúdo
                java_script_enabled=True,
                ignore_https_errors=True,
                service_workers="block",  # Bloqueia service workers que podem armazenar cache
                viewport={"width": 1920, "height": 1080},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
            )
            
            # Configurar cabeçalhos para evitar cache
            page = context.new_page()
            page.set_extra_http_headers({
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0"
            })
            
            try:
                # Limpar cookies antes de iniciar
                context.clear_cookies()
                
                page.goto(self.embassy_url, wait_until="networkidle")
                print("Acessando o site da embaixada...")
                
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
                
                print("Procurando o botão 'Nacionalidad Española'...")
                nationality_selector = '.clsBktServiceName.clsHP a:has-text("Nacionalidad Española")'
                page.wait_for_selector(nationality_selector, state="visible")
                page.click(nationality_selector)
                print("Clicando no botão 'Nacionalidad Española'...")
                time.sleep(10)
                
                page.wait_for_load_state("networkidle")
                print("Página de nacionalidade carregada")
                
                print("Tirando screenshot da página...")
                page.screenshot(path=self.screenshot_path, full_page=True)
                
                page_content = page.content()
                has_appointments = NO_APPOINTMENTS_TEXT not in page_content
                
                if has_appointments:
                    print("Há agendamentos disponíveis!")
                else:
                    print("Não há agendamentos disponíveis.")
                
                self.telegram_service.send_screenshot(self.screenshot_path, has_appointments)
                
                if os.path.exists(self.screenshot_path):
                    os.remove(self.screenshot_path)
                
                return has_appointments
                
            except Exception as e:
                print(f"Erro durante a verificação: {str(e)}")
                try:
                    page.screenshot(path=self.screenshot_path)
                    self.telegram_service.send_screenshot(self.screenshot_path, False, f"Erro: {str(e)}")
                    if os.path.exists(self.screenshot_path):
                        os.remove(self.screenshot_path)
                except:
                    self.telegram_service.send_notification(False, f"Erro ao verificar agendamentos: {str(e)}")
                return False
            
            finally:
                # Limpeza final
                try:
                    context.clear_cookies()
                    browser.close()
                except:
                    pass 