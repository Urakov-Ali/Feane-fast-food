

def telegram_bot_send_message(bot_message):
	bot_token ='5380770058:AAF3i0m-r-3NIuPKoF2mr_lLnQJPsy7knUo'
	bot_chatID ='1344241185'
	send_text ='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode =Markdown&text=' + bot_message 
	response =requests.get(send_text)
	return response.json()

# telegram_bot_send_message('salom')