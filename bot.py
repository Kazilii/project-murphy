import discord
import os
import json

PATH = "data"
CREDS = PATH + "/botcreds.json"

class Murphy(discord.Client):

	async def on_ready(self):
		print('Logged on as {0}'.format(self.user))
		print('Hi there! I\'m {0}, you can invite me to a server using this link: https://discordapp.com/oauth2/authorize?client_id={1}&scope=bot&permissions=67488768'.format(self.user.name, self.user.id))

	async def on_message(self, message):
		if message.author == self.user:
			return

def check_folders():
	if not os.path.exists(PATH):
		print("No data folder detected, generating data folder...")
		os.makedirs(PATH)
		print("Done.\n")

def check_files():
	if not os.path.isfile(CREDS):
		with open(CREDS, 'w') as outfile:
			json.dump({}, outfile)

check_folders()
check_files()

def updatecreds(dict):
	with open(CREDS, 'w') as outfile:
		json.dump(dict, outfile)

def setup():

	settings = {
		"token" : None,
		"owner" : None,
		"nickname" : None
	}

	with open(CREDS, 'w') as outfile:
		json.dump(settings, outfile)

	token = input("Please enter your bot Token: ")

	settings["token"] = token

	owner = input("Please enter the ID of the bot owner: ")

	settings["owner"] = owner

	nickname = input("Please enter a nickname for the bot: ")

	settings["nickname"] = nickname

	updatecreds(settings)

with open(CREDS, 'r') as f:
	settings = json.load(f)
	if settings.get("token") is None or settings.get("owner") is None or settings.get("nickname") is None:
		setup()

client = Murphy()
client.run(settings.get("token"))