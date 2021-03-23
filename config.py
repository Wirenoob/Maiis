import db
import os
# encryption needs here

api_id = int(os.environ['API_ID']) # Api Id
api_hash =  os.environ['API_HASH'] # Api Hash
session_string = os.environ['SESSION'] # session name
custom_command = os.environ['COMMAND_TRIGGER'] # Custom Command Triggerer
my_id = int(os.environ['MASTER_ID']) # User ID
master_id = my_id
total_screen_shot = int(os.environ['TOTAL_PIC']) # total number of photos shot for imdb Search
data_base_url = os.environ['DATABASE_URL']
try:
	data_to_remove = db.get_data()['data_to_remove']
except:
	data_to_remove = []
data_base_data = {'allow' : [],'lock' : 'off','read' : 'on' ,'data_to_remove' : [], 'AI' : {}, 'not_read' : [], 'warnings' : {}, 'sudo' : []}
warn_1 = "Hay, **Did You Know** __Only 10-15 percent of blind people see nothing at all the rest can make out shapes colors and varying degrees of light__.\n** I think You seems like them. Can't you see what am I saying it's your 2nd warning So Wait until You Get Approved**\n\n`Protected by : @MAIIS`"
warn_2 = "Hay, **Did You Know** 80 Percent of vision problems can be avoided or cured with medical care and regular eye.\n**So Go To Hospital Don't Try  To Spam here else if you want to get ban then send more then more then 2 message I bet you will get banned if you did't get approved**\n\n`Protected by : @MAIIS`"
warn_3 = "__OK So you want to risking Your self then Send me another message and I will definitely gonna ban you__\n\n`Protected by : @MAIIS`"
band_message = "__So you did't understand me then you are now liable for your own__. **OK Then never meet again I feel really happy to block you**\n\n`Protected by : @MAIIS`"
not_approved_message = "__You are not__ **Approved** __to message wait until__ **you get Approved** __if you send__ **more then 3 message then you can get banned** __so wait until you get Approved__ \n\n `Protected By - @MAIIS`"
help_command = f"""
**Command List**

**Command** : **Usage**

`{custom_command}help` :  __Use To show help__

`{custom_command}forward` : __To Forward Date From channel__

`{custom_command}ids` : __Show Information About ID__

`{custom_command}imdb` : __Search Movie On IMDB__

`{custom_command}filter` : __Filter Caption (Remove Mentions & link)__

`{custom_command}ubm` : __Sign File As Uploaded By Me__

`{custom_command}lock` : __Enable And Disable LOCK Commands__

`{custom_command}search_tel` : __Search And Upload With Filters__

`{custom_command}add_member` : __Copy Member (Copy other's channel or group member to your)__

`{custom_command}reset_db` : __Reset Database__

`{custom_command}reset` : __Reset Forward message To None__

**Type `{custom_command}help <command>` To Know How To Use**

**Example**

`{custom_command}help forward` OR `{custom_command}help {custom_command}forward`

"""

