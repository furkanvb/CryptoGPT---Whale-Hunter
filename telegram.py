import telebot
import random


def sendtelegramplus(percent,message):
	if (percent < 1):
		return
	tel = telebot.TeleBot("TOKENPLUS",parse_mode='html')
	tel.send_message("PLUSCHANNELID",text=message)


def set_critical(percent):
	critical = ""
	if (percent >= 3):
		critical = "🔥🔥🔥"
	elif (percent >= 2):
		critical = "🔥🔥"
	elif (percent >= 1):
		critical = "🔥"
	return (critical)

def set_message(coinname, lastvol, percent, price, t_vol, count, signaltype, critical):
	if (signaltype == 'long'):
		message = f"""
	🟢 CryptoGPT - LONG 🟢
	💎 Coin: #{coinname} {critical}
	💰 Volume: {lastvol}$ (%{percent})
	💲 Price: {price}$
	💵 T-Long: {t_vol}$ 
	🎚 Count: {count}. Long
	"""
	elif (signaltype == 'short'):
			message = f"""
	🔴 CryptoGPT - SHORT 🔴
	💎 Coin: #{coinname} {critical}
	💰 Volume: {lastvol}$ (%{percent})
	💲 Price: {price}$
	💵 T-Short: {t_vol}$ 
	🎚 Count: {count}. Short
	"""
	return (message)

def sendtelegram(coinname, lastvol, percent, price, t_vol, count, signaltype):
	i = random.randint(1,5)

	if (i == 1):
		token = "BOT1TOKEN"
	elif (i == 2):
		token = "BOT2TOKEN"
	elif (i == 3):
		token = "BOT3TOKEN"
	elif (i == 4):
		token = "BOT4TOKEN"
	elif (i == 5):
		token = "BOT5TOKEN"

	critical = set_critical(percent)
	message = set_message(coinname, lastvol, percent, price, t_vol, count, signaltype, critical)
	tel = telebot.TeleBot(token,parse_mode='html')
	tel.send_message("chatid",message)
	sendtelegramplus(percent,message)