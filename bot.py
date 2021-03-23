from pyrogram import Client , filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, ForceReply, InputMediaPhoto, InputMediaVideo, InputMediaAudio, ChatPermissions
import requests
import os
from bs4 import BeautifulSoup
import re
import ast
import db
import time
import imdb_p
import save_data_web
from config import *
import _thread
import schedule
import random
import help_maiis
from apscheduler.schedulers.background import BackgroundScheduler

app = Client(
	session_string,
	api_id=api_id,
    api_hash=api_hash)

app.set_parse_mode("markdown")

# global var

forword_start = None
forword_end = None
extra_trash = db.get_data()

# global var end here

if len(extra_trash) < 1:
	# 
	db.update(data_base_data)

# other var

try:
	# 
	lock_kind = db.get_data()['lock']
except KeyError:
	get_data_dic = data_base_data
	db.update(get_data_dic)
	lock_kind = db.get_data()['lock']

list_of_allowed_user = db.get_data()['allow']
message_not_to_read = db.get_data()['not_read']

# other var end here

# Custom Filters 

def test(flt, _, message):
	data_to_return = False
	my_id = my_id
	if message.reply_to_message:
		if message.reply_to_message.from_user.id == my_id:
			if message.reply_to_message.text:
				if flt.data in message.reply_to_message.text:
					data_to_return = True
	return data_to_return

def reply_to_message_check(data):
	return filters.create(
		test,
		data=data
	)

# Custom Filters end here

# Other definition

def forword_data_with_filters(id, text=True, document=True, audio=True, photo=True, video=True):
	number = forword_start.forward_from_message_id
	for x in range(forword_end.forward_from_message_id - forword_start.forward_from_message_id + 1):
		try:
			time.sleep(0.5)
			app.copy_message(id, from_chat_id=forword_start.forward_from_chat.id, message_id=number)
			number = number + 1
		except Exception as e:
			app.send_message(id, f'Error in {e} \n\n**Contect To **@H4CK3R_5M4CK3R')
	return True

def filter_data(name):
	if '💎Uploaded By:' in name:
		name = name.replace('💎Uploaded By:' , '')
	if '\n\n⬆️ Uploaded By ⬆️ \n\n          🇮🇳 ' in name:
		name = name.replace('\n\n⬆️ Uploaded By ⬆️ \n\n' , '')
	if '🇮🇳 \n\n    ✌️ Join now for more And Latest Movies ✌\n\nयहां पर आपको सबसे फ़ास्ट मूवीज मिलेगी तो प्लीज हमें ज्वाइन करें और अपनी मूवी की पूरी डिटेल्स दे जैसे उसका 👇\n\n🔰Name, year, language, quality' in name:
		name = name.replace('🇮🇳 \n\n    ✌️ Join now for more And Latest Movies ✌\n\nयहां पर आपको सबसे फ़ास्ट मूवीज मिलेगी तो प्लीज हमें ज्वाइन करें और अपनी मूवी की पूरी डिटेल्स दे जैसे उसका 👇\n\n🔰Name, year, language, quality' , '')
	if 'uploaded by' in name:
		name = name.replace('uploaded by' , '')
	if 'Uploaded by' in name:
		name = name.replace('Uploaded by' , '')
	if 'Uploaded by' in name:
		name = name.replace('Uploaded by' , '')
	if 'UPLOADED BY' in name:
		name = name.replace('UPLOADED BY' , '')
	
	if '📌' in name:
		name = name.replace('📌' , '')
	if 'upload by' in name:
		name = name.replace('upload by' , '')
	if 'Upload by' in name:
		name = name.replace('Upload by' , '')
	if 'Upload by' in name:
		name = name.replace('Upload by' , '')
	if 'UPLOAD BY' in name:
		name = name.replace('UPLOAD BY' , '')
		
	if 'channel' in name:
		name = name.replace('channel' , '')
	if 'Channel' in name:
		name = name.replace('Channel' , '')
	if 'CHANNEL' in name:
		name = name.replace('CHANNEL' , '')
	if 'Request at' in name:
		name = name.replace('Request at' , '')
	if 'Join Our Official channel' in name:
		name = name.replace('Join Our Official channel' , '')
	for data in data_to_remove:
		if data in name:
			name = name.replace(data, '')
	data_list = []
	list_of_data = name.split()
	n = 0
	while len(list_of_data) > n:
		data = list_of_data[n]
		if '@' in data or 't.me/' in data:
			name = name.replace(data , '')
			n = n + 1
		else:
			n = n + 1
	return name

def get_data():
	data = save_data_web.get_data()
	if len(data) < 1:
		return get_data()
		send_log("ERROR While getting data. data length found " + str(len(data)))
	try:
		data = ast.literal_eval(data)
		return data
	except Exception as e:
		send_log('error : ' + str(e))

def update_data(data):
	save_data_web.update_data(str(data))
	# update data

def send_log(data):
	# send log to log channel
	bot.sendMessage(log_channel , str(data) + " \n - By MAIIS personal")

# other definition end here

#commands start here

# only for owner

# only for owner end here

@app.on_message(filters.text & filters.me & filters.command('reset', prefixes=custom_command))
def reset_forward(_, message):
	global forword_end, forword_start
	message.edit_text('**Forward Message Data Reset Complete**')
	forword_start = None
	forword_end = None

@app.on_message(filters.text & filters.me & filters.command('forward', prefixes=custom_command) & filters.reply)
def forword_command(_, message):
	global forword_start, forword_end
	if forword_start:
		if not message.reply_to_message.forward_from_chat:
			message.edit_text(f'#ERROR_MAIIS** : Forword Message Not Found **')
			return
		if not message.reply_to_message.forward_from_chat.type == 'channel':
			message.edit_text(f'#ERROR_MAIIS** : Only Channel Are Allowd Not **`{message.reply_to_message.forward_from_chat.type}`')
			return
		if not forword_start.forward_from_chat.id == message.reply_to_message.forward_from_chat.id:
			message.edit_text('😒**You Are Trying To Forword Message From Different Channel Really ?**')
			return
		if forword_start.forward_from_message_id > message.reply_to_message.forward_from_message_id:
			message.edit_text('😒**You Are Trying To Forword Data From Down To Up Really ?**')
			return
		message.edit_text(f'**Please Wait Forwording Data From** `{message.reply_to_message.chat.id}` **To** {message.chat.id}')
		forword_end = message.reply_to_message
		if forword_data_with_filters(message.chat.id):
			app.send_message(message.chat.id, '**Done All Data Sent** `Sucess`')
			forword_start = None
			forword_end = None
		else:
			app.send_message(message.chat.id, '**Error While Sending Data** `Error`')
		# forword data here
	else:
		if not message.reply_to_message.forward_from_chat:
			message.edit_text(f'**#ERROR_MAIIS : Forword Message Not Found **')
			return
		if not message.reply_to_message.forward_from_chat.type == 'channel':
			message.edit_text(f'**#ERROR_MAIIS : Only Channel Are Allowd Not **`{message.reply_to_message.forward_from_chat.type}`')
			return
		message.edit_text(f'**Forword Start From Message Selected Now Send End Message**')
		forword_start = message.reply_to_message

@app.on_message(filters.text & filters.me & filters.command('ids', prefixes=custom_command))
def send_ids(_, message):
	if message.reply_to_message:
		message.edit_text(f'**Chat ID :** `{message.chat.id}`\n\n**User ID :** `{message.reply_to_message.from_user.id}`\n\n**My ID :** `{message.from_user.id}`\n\n**Chat Type :** `{message.chat.type}`')
	if message.chat.type == 'private':
		message.edit_text(f'**Chat ID :** `{message.chat.id}`\n\n**My ID :** `{message.from_user.id}`\n\n**Chat Type :** `{message.chat.type}`')
	else:
		message.edit_text(f'**Chat ID :** `{message.chat.id}`\n\n**My ID :** `{message.from_user.id}`\n\n**Chat Type :** `{message.chat.type}`')

@app.on_message(filters.text & filters.me & filters.command('allow', prefixes=custom_command) & filters.private & ~filters.bot)
def allow_user(_, message):
	global list_of_allowed_user
	get_data_dic = db.get_data()
	if message.chat.id in get_data_dic['allow']:
		message.edit_text('**Already Allowed**')
	else:
		if message.chat.id in get_data_dic['warnings']:
			del get_data_dic['warnings'][message.chat.id]
		get_data_dic['allow'].append(message.chat.id)
		message.edit_text('**You are now allow to send message**')
		list_of_allowed_user = get_data_dic['allow']
		db.update(get_data_dic)

@app.on_message(filters.text & filters.me & filters.command('not allow', prefixes=custom_command) & filters.private & ~filters.bot)
def not_allow_user(_, message):
	global list_of_allowed_user
	get_data_dic = db.get_data()
	if message.chat.id in get_data_dic['allow']:
		message.edit_text('**Done Changes Occur Success**')
		get_data_dic['allow'].remove(message.chat.id)
	else:
		message.edit_text('**No Changes Occur**')
		return
	list_of_allowed_user = get_data_dic['allow']
	db.update(get_data_dic)

@app.on_message(filters.text & filters.me & filters.command('help', prefixes=custom_command))
def show_help_command(_, message):
	if not ' ' in message.text:
		message.edit_text(help_command)
		return
	else:
		message.edit_text(help_maiis.help(message.text.replace(f'{custom_command}help ', '')))
	# help command

@app.on_message(filters.text & filters.me & filters.command('imdb', prefixes=custom_command))
def imdb_search(_, message):
	movie_name = message.text
	movie_name = movie_name.replace(f'{custom_command}imdb', '')
	message.edit_text(f'Searching For : `{movie_name}`')
	if len(movie_name) < 1:
		message.edit_text('**Wrong Format Here is usage** : \n\n`{custom_command}imdb <movie_name>`\n**Example**\n\n`{custom_command}imdb Your Name`')
		return
	movie_data, screen_shots, image = imdb_p.imdb(movie_name)
	if movie_data:
		app.send_photo(message.chat.id, image, caption=movie_data)
		if len(screen_shots) < 1:
			pass
			# app.send_message(message.chat.id, '**Photos Are Not Available Now But may be available soon**')
		else:
			for links in screen_shots:
				time.sleep(2)
				app.send_photo(message.chat.id, links)
		message.delete()
		return
	else:
		message.edit_text(f'**Bruh**, Plox enter **Valid movie name** {movie_name}')

@app.on_message(filters.text & filters.me & filters.command('filter', prefixes=custom_command) & filters.reply)
def filter_caption(_, message):
	if message.reply_to_message.text:
		message.edit_text('#ERROR_MAIIS : **No Media Found**')
		return
	if not message.reply_to_message.caption:
		message.edit_text('#ERROR_MAIIS : **No Caption Found**')
		return
	caption_filtered = filter_data(message.reply_to_message.caption)
	if message.reply_to_message.photo:
		id_of_file = message.reply_to_message.photo.file_id
	elif message.reply_to_message.document:
		id_of_file = message.reply_to_message.document.file_id
	elif message.reply_to_message.video:
		id_of_file = message.reply_to_message.video.file_id
	elif message.reply_to_message.audio:
		id_of_file = message.reply_to_message.audio.file_id
	else:
		message.edit_text('**This Media Is Not Supported Yet **')
		return
	message.delete()
	app.send_cached_media(message.chat.id, file_id=id_of_file, caption=caption_filtered)

@app.on_message(filters.text & filters.me & filters.command('ubm', prefixes=custom_command) & filters.reply)
def uploaded_by_me_setting(_, message):
	if message.reply_to_message.text:
		message.edit_text('#ERROR_MAIIS : **No Media Found**')
		return
	if message.reply_to_message.caption:
		caption_filtered = message.reply_to_message.caption
	else:
		caption_filtered = None
	if message.reply_to_message.photo:
		id_of_file = message.reply_to_message.photo.file_id
	elif message.reply_to_message.document:
		id_of_file = message.reply_to_message.document.file_id
	elif message.reply_to_message.video:
		id_of_file = message.reply_to_message.video.file_id
	elif message.reply_to_message.audio:
		id_of_file = message.reply_to_message.audio.file_id
	else:
		message.edit_text('**This Media Is Not Supported Yet **')
		return
	message.delete()
	if caption_filtered:
		app.send_cached_media(message.chat.id, file_id=id_of_file, caption=caption_filtered)
	else:
		app.send_cached_media(message.chat.id, file_id=id_of_file)

@app.on_message(filters.text & filters.me & filters.command('lock', prefixes=custom_command))
def enable_disable_lock(_, message):
	global lock_kind
	all_ow = ''
	get_data_dic = db.get_data()
	if get_data_dic['lock'] == 'off':
		message.edit_text('**Private Lock** : `Enable`')
		all_ow = 'on'
	elif get_data_dic['lock'] == 'on':
		message.edit_text('**Private Lock** : `Disable`')
		all_ow = 'on'
	else:
		message.edit_text('#ERROR_MAIIS : **Contact** @H4CK3R_5M4CK3R')
	get_data_dic['lock'] = all_ow
	lock_kind = all_ow
	db.update(get_data_dic)

@app.on_message(filters.text & filters.me & filters.command("search_tel", prefixes=custom_command))
def search_for_files(_, message):
	checking_data = message.text
	try:
		checking_data = checking_data.split(' ')
	except:
		message.edit_text('**Usage :** \n\n`{custom_command}search_tel <name> | <type>-<number>\n**Example : **\n\n`{custom_command}search_tel your name | document-3`')
		return
	if len(checking_data) > 0:
		if '|' in message.text:
			if f'{custom_command}search_tel' in message.text:
				data_to_search = message.text
				data_to_search = data_to_search.replace(f'{custom_command}search_tel ' , '')
				message.edit_text(f'Searching For {data_to_search}')
				try:
					if ' | ' in data_to_search and '-' in data_to_search:
						data_to_search = data_to_search.split(' | ')
						number = data_to_search[1]
						data_to_search = data_to_search[0]
						if 'document' in number:
							file = 'document'
							number = number.replace('document-' , '')
							number = int(number)
						elif 'video' in number:
							file = 'video'
							number = number.replace('video-' , '')
							number = int(number)
						elif 'photo' in number:
							file = 'photo'
							number = number.replace('photo-' , '')
							number = int(number)
						elif 'text' in number:
							file = 'text'
							number = number.replace('text-' , '')
							number = int(number)
					else:
						file = 'text'
						number = 5
				except:
					app.send_message(message.chat.id , 'Error While Getting result please use this format `.search the your name | video-5` \n\n This is just a example you can use any other things to search and note that only document , video , text , photo are search able other data will changed to text and default is text')
					return
				total = 0
				if number > 25:
					app.send_message(message.chat.id , 'Searching limit is 25 you can not get more then 25 data per search')
					return
				else:
					for data in app.search_global(data_to_search, limit=400):
						if data.caption:
							caption = data.caption
							if len(caption) > 0:
								caption = filter_data(caption)
							else:
								caption = ''
						else:
							caption = ''
						caption = caption + ' By @MAIIS'
						if file == 'text':
							if data.text:
								if total < number:
									app.send_message(message.chat.id, data.text)
								else:
									break
								total = total + 1
						elif file == 'video':
							if data.video:
								file_id = data.video.file_id
								if total < number:
									app.send_video(message.chat.id, file_id, caption=caption)
								else:
									break
								total = total + 1
						elif file == 'document':
							if data.document:
								file_id = data.document.file_id
								if total < number:
									app.send_document(message.chat.id, file_id, caption=caption)
								else:
									break
								total = total + 1
						elif file == 'photo':
							if data.photo:
								file_id = data.photo.file_id
								if total < number:
									app.send_photo(message.chat.id, file_id, caption=caption)
								else:
									break
								total = total + 1
						else:
							pass
					message.delete()
					app.send_message(message.chat.id, '**Done Data Sent**')
			else:
				message.edit_text('**Usage :** \n\n`.search_tel <name> | <type>-<number>\n**Example : **\n\n`.search_tel your name | document-3`')
		else:
			message.edit_text('**Usage :** \n\n`.search_tel <name> | <type>-<number>\n**Example : **\n\n`.search_tel your name | document-3`')
	else:
		message.edit_text('**Usage :** \n\n`.search_tel <name> | <type>-<number>\n**Example : **\n\n`.search_tel your name | document-3`')

@app.on_message(filters.text & filters.me & filters.command('reset_db', prefixes=custom_command))
def reset_db(_, message):
	get_data_dic = data_base_data
	message.edit_text('**Data Reset Complete Every Thing Is Erased**')
	db.update(get_data_dic)

@app.on_message(filters.private & filters.text & filters.regex('&') & ~filters.me)
def sudo_command_startner(_, message):
	get_data_dic = db.get_data()
	if message.chat.id in get_data_dic['sudo']:
		if message.text == '$gclear':
			app.send_message(-1001177299931, '.gclear')
			time.sleep(2)
			app.send_message(-1001177299931, '.gsetup')
			return
		try:
			message_id = message.reply_to_message.message_id
		except:
			message_id = message.message_id
		if message.from_user.id in get_data_dic['sudo']:
			command = message.text
			command = command.replace('$' , '.')
			app.send_message(message.chat.id , command , reply_to_message_id=message_id)
		else:
			app.send_message(message.chat.id , '- You are not allow to use this feature-')
		app.read_history(message.chat.id)

@app.on_message(filters.private & ~filters.me & ~filters.bot)
def check_message_data(_, message):
	global lock_kind, list_of_allowed_user
	get_data_dic = db.get_data()
	if lock_kind == 'on':
		if message.chat.id in list_of_allowed_user:
			return
		else:
			if message.chat.id in get_data_dic['warnings']:
				total_warn = get_data_dic['warnings'][message.chat.id]
				if total_warn == 1:
					app.send_message(message.chat.id, warn_1)
					get_data_dic['warnings'][message.chat.id] = 2
				elif total_warn == 2:
					message.reply_text(warn_2)
					get_data_dic['warnings'][message.chat.id] = 3
				elif total_warn == 3:
					message.reply_text(warn_3)
					get_data_dic['warnings'][message.chat.id] = 4
				elif total_warn > 3:
					message.reply_text(band_message)
					del get_data_dic['warnings'][message.chat.id]
					app.block_user(message.chat.id)
			else:
				app.send_message(message.chat.id, not_approved_message)
				get_data_dic['warnings'][message.chat.id] = 1
			db.update(get_data_dic)
			# bot.send_message()

# commands end here

# only for owner of bot

@app.on_message(filters.text & filters.me & filters.command('sudo allow', prefixes=custom_command))
def sudo_allow(_, message):
	get_data_dic = db.get_data()
	get_data_dic['sudo'].append(message.chat.id)
	message.edit_text('**Done User Allowed To Use Sudo**')
	db.update(get_data_dic)

@app.on_message(filters.text & filters.me & filters.command('sudo not allow', prefixes=custom_command))
def sudo_not_allow(_, message):
	get_data_dic = db.get_data()
	get_data_dic['sudo'].remove(message.chat.id)
	message.edit_text('**Sudo Removed**')
	db.update(get_data_dic)

# only for owner of bot

app.run()
