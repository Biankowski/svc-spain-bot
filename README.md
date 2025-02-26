# Bot de Verificação de Agendamentos Consulares

Este bot automatiza a verificação de disponibilidade de agendamentos no site da Embaixada da Espanha em Brasília e envia notificações via Telegram quando encontra vagas disponíveis.

## Funcionalidades

- Acessa automaticamente o site da Embaixada da Espanha
- Navega até o sistema de agendamentos
- Verifica se há horários disponíveis
- Envia notificações via Telegram sobre a disponibilidade
- Exibe o navegador durante o processo para acompanhamento visual

## Requisitos

- Python 3.7+
- Playwright
- Conta no Telegram
- Bot do Telegram (criado via BotFather)

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/Biankowski/svc-spain-bot.git
cd bot-verificacao-agendamentos
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Instale os navegadores necessários para o Playwright:

```bash
playwright install
```

## Configuração

### 1. Configuração do Bot do Telegram

1. Abra o Telegram e procure por `@BotFather`
2. Inicie uma conversa e envie o comando `/newbot`
3. Siga as instruções para criar um novo bot
4. Guarde o token fornecido pelo BotFather

### 2. Obtendo o Chat ID

1. Inicie uma conversa com seu bot recém-criado
2. Envie qualquer mensagem para o bot
3. Acesse a URL: `https://api.telegram.org/bot{SEU_TOKEN}/getUpdates` (substitua `{SEU_TOKEN}` pelo token do seu bot)
4. Procure pelo valor `"chat":{"id":` na resposta JSON - este é o seu Chat ID

### 3. Configuração do arquivo .env

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
TELEGRAM_CHAT_ID=seu_chat_id_aqui
```

Substitua `seu_chat_id_aqui` pelo ID numérico obtido no passo anterior.

### 4. Configuração do arquivo config.py

O arquivo `src/config.py` já contém as configurações básicas, mas você pode precisar ajustar:

```python
# Token do seu bot do Telegram
TELEGRAM_BOT_TOKEN = "seu_token_aqui"

# ID do chat para enviar as notificações
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
```

## Uso

Para executar o bot uma única vez:

```bash
python main.py
```

## Estrutura do Projeto

```
projeto/
├── src/
│   ├── __init__.py
│   ├── bot.py           # Classe principal do bot
│   ├── telegram_service.py  # Serviço de notificação via Telegram
│   └── config.py        # Configurações do bot
├── main.py              # Script principal
├── .env                 # Variáveis de ambiente
└── requirements.txt     # Dependências
```

## Solução de Problemas

### O bot não consegue enviar mensagens pelo Telegram

- Verifique se o token do bot está correto
- Certifique-se de que você iniciou uma conversa com o bot
- Confirme se o Chat ID está correto

### O bot não consegue acessar o site da embaixada

- Verifique sua conexão com a internet
- O site pode estar temporariamente indisponível
- O layout do site pode ter mudado, necessitando atualização do código

### Erro ao instalar o Playwright

- Tente executar `playwright install` novamente
- Verifique se você tem permissões de administrador

**Nota**: Este bot foi criado apenas para fins educacionais e de conveniência pessoal. Use-o de forma responsável e respeite os termos de serviço do site da embaixada.
