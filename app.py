from flask import Flask, request
import telegram

app = Flask(name)

# Токен бота, который ты получила от BotFather
TOKEN = 'YOUR_BOT_TOKEN'  # Заменить на твой токен
bot = telegram.Bot(token=TOKEN)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST'])
def webhook():
    # Получаем данные о сообщении
    data = request.get_json()
    
    # Логика обработки сообщений (например, отправка приветственного сообщения)
    chat_id = data['message']['chat']['id']
    bot.send_message(chat_id=chat_id, text="Привет, я твой бот!")
    
    return 'OK', 200

if name == 'main':
    app.run(host='0.0.0.0', port=3002)
