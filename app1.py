from telegram.ext import Updater, MessageHandler,Filters
from Adafruit_IO import Client
import os
aio = Client('Rokhini',os.getenv('Rokhini'))
def turn_on_light(bot,update):
  #aio = Client('Rokhini', 'aio_TyyC17mIBfY3IbbRuUJGZ8XMwoLJ')
  aio.send('bedroom-light', 1)
  data = aio.receive('bedroom-light')
  print(f'Received value: {data.value}')
  chat_id=bot.message.chat_id
  path='https://www.excelelectricsouthflorida.com/images/blog/bigstock-Light-bulb-16977008.jpg'
  bot.message.reply_text('light is turned on')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_off_light(bot,update):
  #aio = Client('Rokhini', 'aio_TyyC17mIBfY3IbbRuUJGZ8XMwoLJ')
  aio.send('bedroom-light',0)
  data = aio.receive('bedroom-light')
  print(f'Received value: {data.value}')
  chat_id=bot.message.chat_id
  bot.message.reply_text('light is turned off')
  path='https://thumbs.dreamstime.com/z/light-bulb-watt-off-white-background-34641378.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_on_fan(bot,update):
  #aio = Client('Rokhini', 'aio_TyyC17mIBfY3IbbRuUJGZ8XMwoLJ')
  aio.send('bedroom-fan',1)
  data = aio.receive('bedroom-fan')
  print(f'Received value: {data.value}')
  chat_id=bot.message.chat_id
  path='https://ak8.picdn.net/shutterstock/videos/2862997/thumb/1.jpg'
  bot.message.reply_text('fan is turned on')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_off_fan(bot,update):
  #aio = Client('Rokhini', 'aio_TyyC17mIBfY3IbbRuUJGZ8XMwoLJ')
  aio.send('bedroom-fan',0)
  data = aio.receive('bedroom-fan')
  print(f'Received value: {data.value}')
  chat_id=bot.message.chat_id
  bot.message.reply_text('fan is turned off')
  path='https://i5.walmartimages.com/asr/fef3c062-8076-44a4-8db5-119188eef039_1.06c32d0a1181c1722c474a9f3f129afe.jpeg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def main(bot,update):
  a = bot.message.text
  print(a)

  if a=="turn on light":
    turn_on_light(bot,update)
  elif a=="turn off light" or a=="light off":
    turn_off_light(bot,update)
  elif a=="turn on fan":
    turn_on_fan(bot,update)
  elif a=="turn off fan" or a=="fan off":
    turn_off_fan(bot,update)
  else:
    bot.message.reply_text('invalid')

BOT_TOKEN = os.getenv('BOT_TOKEN')
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
