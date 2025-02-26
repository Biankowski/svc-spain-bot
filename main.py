from src.bot import AppointmentBot
import sys

def main():
    try:
        bot = AppointmentBot()
        result = bot.run()
        
        if result:
            print("Verificação concluída: Há agendamentos disponíveis!")
        else:
            print("Verificação concluída: Não há agendamentos disponíveis.")
        
        return 0
    except Exception as e:
        print(f"Erro na execução do bot: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 