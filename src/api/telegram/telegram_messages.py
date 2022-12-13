import telegram
from requests import request
from api.telegram.telegram_credentials import bot_token, bot_user_name, URL

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

def war_status(war_stats):    
    bot.sendMessage(chat_id='-1001707021945', text=war_stats)