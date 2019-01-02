import telegram
#python-telegram-bot
from crawl import crawl_wf
import json

def send_alert(sentence=None):
    my_token = ''

    with open('./token.json', 'r') as f:
        my_token = json.loads(f.read())["TOKEN"]
    print(my_token)
    bot = telegram.Bot(token=my_token)
    updates = bot.getUpdates()

    try:
        chat_id = bot.getUpdates()[-1].message.chat.id
    except:
        chat_id = 11

    # print(chat_id)

    bot.send_message(chat_id=chat_id, text='월프공지\n' + sentence.replace('\n', ' ').replace('*',''))
    #bot.send_message(chat_id=chat_id,text='월프공지')

def send_telegram():
    result = crawl_wf()
    if result[0] ==1:
        send_alert(result[1])
    else:
        pass

send_telegram()



"""
pip install python-telegram-bot --upgrade
pip install selenium

"""
