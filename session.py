from pyrogram import Client as c
import os
try:
	API_ID = int(os.environ['API_ID'])
	API_HASH = int(os.environ['API_ID'])
except:
	API_ID = input('Enter API ID : ')
	API_HASH = input('Enter API Hash : ')
i = c(":memory:", api_id=API_ID, api_hash=API_HASH)
with i:
    ss = i.export_session_string()
    print('Here is your session string : \n\n\n')
    print(f"\n{ss}\n")