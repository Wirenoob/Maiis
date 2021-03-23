from config import custom_command

def help(which):
	which = which.lower()
	if custom_command in which:
		which = which.replace(custom_command, '')
	if which == 'help' or which == f'{custom_command}help':
		message = f"""
**Description**

__This command is use to Show Help Command__

**Usage**

`{custom_command}help`
		"""
	elif which == 'forward' or which == f"{custom_command}forward":
		message = f"""
**Description**

__This command is use to forward media, text and other document from channel to specific chat (private, group, channel)__

**Usage**

__First you need to select start message forward message to chat where you want to send data and reply to that message with command__

`{custom_command}forward`

__After That select another message which is end message and forward to same chat with command__

`{custom_command}forward`

__After That You Will get your text or media__

**NOTE** : __Select Message from up to down format Not down to up__

		"""
	elif which == 'ids':
		message = f"""
**Description**

__This command is use to extract IDS like chat id user id etc (You can also reply to message to know user chat id)__

**Usage**

`{custom_command}ids`
		"""
	elif which == 'filter':
		message = f"""
**Description**

__This command is use to filter (remove links and username) caption from media (You need to reply to that media and use command)__

**Usage**

__By reply to media message__

`{custom_command}filter`
		"""
	elif which == 'ubm':
		message = f"""
**Description**

__It means__ **Uploaded By Me** __It is use to remove forward sign from file (sign only for user not telegram)__

**Usage**

__By reply to media message__

`{custom_command}ubm`
		"""
	elif which == 'lock':
		message = f"""
**Description**

__This command is use to enable / disable new message lock (It will give 3 warning to user and after that user will get temporary blocked)__

**Usage**

`{custom_command}lock`

**Use** `{custom_command}allow` **To allow user to send message**
**Or Use** `{custom_command}not allow` **To Not to allow user to send message any more**
		"""
	elif which == 'search_tel':
		message = f"""
**Description**

__This command is use to search Photo / Video / Document in your telegram chat's__

**Usage**

`{custom_command}search_tel <name> | <type>-<number>`

**Here** `<name>` __Referred as file name and__ `<type>` __As file type and__ `<number>` __as how much files you need__

**Types Which Are Available**

`document` - __A Document File which could be movie, apk, uncompressed photo, other__
`video` - __A Video File__
`photo` - __Compressed Photo__
`text` - __Simple text__

**NOTE** : __Default value is text and try to use Types in small letter and also try to give much less information as less you can while searching for file__
		"""
	elif which == 'add_member':
		message = "Not Available Now Soon will be Join @MAIIS To Know latest Updates"
		messages = f"""
**Description**

__This command is use to extract member's from another group to yours__

**Usage**

`{custom_command}add_member <from User-name / Chat ID>|<to user-name / Chat ID>|<total>`

__You can get chat id from__ `{custom_command}ids` __command__

**NOTE** : __Max Number is 200 You can not add more then 200 member from per group and also use at your own risk__
		"""
	elif which == 'reset_db':
		message = f"""
**Description**

__This command is use to reset database To start everything again__

**Usage**

`{custom_command}reset_db`
		"""
	elif which == 'reset':
		message = f"""
**Description**

__This command is use to reset forward message ( forward command data )__

**Usage**

`{custom_command}reset`
		"""
	else:
		message = f"""
**Wrong Format OR Wrong Command Type **`{custom_command}help` **To Know Usage And all command**
		"""
	return message
