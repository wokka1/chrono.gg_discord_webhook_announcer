#!/usr/bin/python3

# chrono.gg announcement webhook 1.0
# simple setup to announce chrono.gg url into your discord channel (yes, you could use the same setup for any URL)
# as an admin of a discord channel, click the gear on the channel and add a webhook, grab the URL from there and replace the one below in the variables, execute the script to push the url to the discord channel.  there is no scheduler, i use a crontab entry on linux for that

# written by wokka - 14 Nov 2018
# changelog :
#
# no warranty or support comes with this, use it as you want
# licensed under GPLv3
# change the variables accordingly

import sys
import requests
import json

# variables
webhookurl = 'https://discordapp.com/api/webhooks/---------replace-this-URL-with-your-own-----H5bWACL_UE_LvIk'

# Code

header = {'Content-Type': 'application/json'}

response = requests.post(webhookurl, data="{\"content\": \"https://www.chrono.gg/\"}", headers=header)

