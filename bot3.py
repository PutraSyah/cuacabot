import time
import telepot
from twx.botapi import TelegramBot, ReplyKeyboardMarkup #Telegram BotAPI
from time import sleep
import sys
from pyowm import OWM
import traceback
TOKEN = "739704639:AAFdgUEbsd2vI4MdjmknLrufNTqJvecV1EQ"
bot = TelegramBot(TOKEN) 
bot.update_bot_info().wait()  #wait for a message
print bot.username 
last_update_id = 0 
OWMKEY ='93e430eaf5690c0ec4ae89e4f84a7d7d'
def process_message(bot, u):	
 #Use a custom keyboard 
   
    if u.message.sender and u.message.text and u.message.chat: #if it is a text message then get it 
		chat_id = u.message.chat.id 
		user = u.message.sender.username
		message = u.message.text 
		print chat_id 
		print message 
		if message == 'Cuaca uro nyo?': #if the user is asking for the weather then we ask the location 
			bot.send_message(chat_id, 'Ka kirim lokasi kah keuno!') 
		if message == 'Assalamualaikum': #if the user is asking for the weather then we ask the location 
			bot.send_message(chat_id, 'Walaikumsalam')
		if message =='/start':
			bot.send_message(chat_id,'Selamat Katroh bak Dedek Bot')
		if message =='Pu na haba?':
			bot.send_message(chat_id,'Haba get')
		if message =='Pu haba?':
			bot.send_message(chat_id,'Haba get')
		if message =='Pat jino tinggai?':
			bot.send_message(chat_id,'Lam internet. Katem tinggai sajan lon?')
		if message =='Han':
			bot.send_message(chat_id,'Kakeuhlah')
		if message =='Pat tinggai?':
			bot.send_message(chat_id,'Lam internet. Katem tinggai sajan lon?')
		if message =='Peu na haba?':
			bot.send_message(chat_id,'Haba get') 
		if message =='Hana':
			bot.send_message(chat_id,'Oo kakeuh lah')	
		if message =='So peuget kah?':
			bot.send_message(chat_id,'Si Youtuber Putra Gamer')
		if message =='So ureung yang peuget kah?':
			bot.send_message(chat_id,'Si Youtuber Putra Gamer')
		if message =='Pubut kah nyo?':
			bot.send_message(chat_id,'Peugah haba ngon kah hehe ^_^')
		if message =='Pubut kah jino nyo?':
			bot.send_message(chat_id,'Peugah haba ngon kah hehe ^_^')
		if message =='Pubut kah nyo jino?':
			bot.send_message(chat_id,'Peugah haba ngon kah hehe ^_^')
		if message =='Pu na haba uro nyo?':
			bot.send_message(chat_id,'Haba get')	
		if message=='Hahaha':
			bot.send_message(chat_id,'Hahaha Hihihi Huhuhu')
		if message =='Kah ka ejek lon nyeh?':
			bot.send_message(chat_id,'Hana hai cuma meen - meen')
		if message =='Pubut kah jino?':
			bot.send_message(chat_id,'Peugah haba ngon kah hehe ^_^')
		if message =='Kah na ngon keuh?':
			bot.send_message(chat_id,'Hana lom, kah katem meungen ngon lon?')
		if message=='Jeut':
			bot.send_message(chat_id,'Makasih Beuh')
		if message =='Tem':
			bot.send_message(chat_id,'Makasih Beuh')
		if message=='Ok':
			bot.send_message(chat_id,'Makasih Beuh')
		
		
 
    elif u.message.location: #if the message contains a location then get the weather on that latitude/longitude 
        print u.message.location 
        chat_id = u.message.chat.id 
        owm = OWM(OWMKEY) #initialize the Weather API 
        obs = owm.weather_at_coords(u.message.location.latitude, u.message.location.longitude) #Create a weather observation 
        w = obs.get_weather() #create the object Weather as w 
        print(w) # <Weather - reference time=2013-12-18 09:20, status=Clouds> 
        l = obs.get_location() #create a location related to our already created weather object And send the parameters 
        status = str(w.get_detailed_status()) 
        placename = str(l.get_name()) 
        wtime = str(w.get_reference_time(timeformat='iso')) 
        temperature = str(w.get_temperature('celsius').get('temp'))
        bot.send_message(chat_id, 'Status cuaca uro nyo: ' +status +' Bak '+placename+' ' +wtime+' Suhu jih: '+ temperature+ 'C') #send the anwser
		
	
	
while True: #a loop to wait for messages
    updates = bot.get_updates(offset = last_update_id).wait() #we wait for a message
    try: 
        for update in updates: #get the messages
            if int(update.update_id) > int(last_update_id): #if it is a new message then get it
                last_update_id = update.update_id 
                process_message(bot, update) #send it to the function 
                continue 
        continue 
    except Exception: 
        ex = None 
        print traceback.format_exc() 
        continue
		
# Token of bot account

bot = telepot.Bot(TOKEN)
bot.message_loop(process_message)
print ('Loading . . .')

# Keep bot running
while 1:
	time.sleep(10)