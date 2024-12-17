from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
#from aiogram.enums.parse_mode import ParseMode
from aiogram.utils import markdown as md
from bs4 import BeautifulSoup
import asyncio, logging, urllib.parse, re, requests, json

logging.basicConfig(level=logging.INFO)

API_TOKEN = '7018210376:AAHPQP-RpSouR1sFeB8y5kvv1VM6C7IwDhI'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
chat_id=[1295721493, 426966529]



class CategoryElements:
    def __init__(self, category, quantity, link):
        self.category = category
        self.quantity = quantity
        self.link = link
    def __repr__(self):
        return  f"{self.category}: {self.quantity}"
  
class Item:
    def __init__(self, name, price, link):
        self.name = name
        self.price = price
        self.link = link
    def __repr__(self):
        return  f"{self.name}: {self.price}"
  





@dp.message(Command('start'))
async def send_welcome(message: types.Message):
   await message.reply("Привет, ня!\nЯ бот!\nВведите наименование или номинал компонента и я покажу вам его стоимость в магазине.")

@dp.message()
async def echo(message: types.Message):
    
    search_request = message.text
    
    
    #This is parser..........................................................
    input_name = search_request

    url =f'https://www.chipdip.ru/search?searchtext={input_name}' #define url variable for comfort



    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}   #add a some identifier
    result = requests.get(url, headers=headers) #function that get all code from webpage
    #print(result.content.decode())                 #decode as text
    soup = BeautifulSoup(result.text,"lxml")  #do literally the same thing


    category=[]
    quantity = []
    links = []
    elements=[]




   





    feun1 = price_table(components, prices, url)



    
    #This is parser..........................................................
    
    
    await message.answer(feun1)
#    await bot.send_message(chat_id, str(message.chat.id))


async def alert_users(message:str):
    for id in chat_id:
        try:
            await bot.send_message(id, message)
        except Exception as e:
            logging.error(f'Falied to send message to user {id}: {e}')


'''
async def check_bot_status():
    while True:
        try:
            #check if bot online
            await bot.get_me()
            await alert_users(md.bold("Бот онлайн"))
        except:
            await alert_users(md.bold("Бот офлайн"))
        await asyncio.sleep(60)
'''

@dp.message(F.command == ['shutdown'], F.chat.id == 1295721493)
async def manual_shutdown(message: types.Message):
    await message.reply('Shutting down')
    await bot.close()
    await dp.stop_polling()
    logging.info('Bot has been shut down')



async def on_startup():
    logging.info('startup_func')
    await alert_users(md.bold('Бот онлайн'))

#    if chat_id==1295721493:
#        await bot.send_message(chat_id, "Онлайн")

async def on_shutdown(bot:Bot):
    logging.info('shutdown')
    await alert_users(md.bold('Бот офлайн'))
#        await bot.send_message(chat_id, "Отключаюсь")
#        await dp.stop_polling(bot)



    
async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    
    await dp.start_polling(bot)
    #await alert_users(md.bold('Бот онлайн'))
    

if __name__ == '__main__':
#   executor.start_polling(dp, skip_updates=True)
    asyncio.run(main())