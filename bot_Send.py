import telegram
#python-telegram-bot
from crawl import crawl_wf

def send_alert(sentence=None):
    my_token = 'SECRET KEY'

    bot = telegram.Bot(token=my_token)
    updates = bot.getUpdates()

    chat_id = bot.getUpdates()[-1].message.chat.id

    # print(chat_id)

    #bot.send_message(chat_id=roharon, text='훕포메이션 학점알림이 - 텔레그램\n' + sentence)
    bot.send_message(chat_id=roharon, text='월프공지\n' + sentence)
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