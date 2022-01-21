import discord, os, random


token = "" 		# <--- put the bot's token here
server_name = ""	# <--- put the server's name here
members = []


greetings = ['hello','hi','yo','salute','whats up','wassup','hey','greetings']

logged_messages = []
logging = False
# you must enable the "SERVER MEMBERS INTENT" Privileged Gateway Intent under the bot settings in the Discord developer portal
intents = discord.Intents.default() 
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
	server = discord.utils.get(client.guilds, name=server_name)

@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'EYOOOO {member.name} ! WELCOME TO TECH DUNGEON x)'
		)

@client.event
async def on_message(message):
	global logging,logged_messages
	
	if(logging): 
		logged_messages.append(f'#{message.channel.name}/{message.author.name}#{message.author.discriminator}: {message.content}')


	if(message.content[0] == '$'):
		if(message.content[1:].lower() in greetings):
			greeting = greetings[random.randint(0,len(greetings)-1)].capitalize()
			await message.reply(greeting + " !")
		
		elif(message.content[1:].lower() == 'twerk'):
			await message.channel.send("NO")

		# Messages logging commands
		elif(message.content[1:].lower() == 'log start'):
			if(logging):
				await message.channel.send("Messages logging is already started.")
			else:
				logging = True
				await message.channel.send("Messages logging started.")

		elif(message.content[1:].lower() == 'log stop'):
			logging = False
			await message.channel.send("Messages logging Ended.")

		elif(message.content[1:].lower() == 'log show'):
			if(logging == False):
				for msg in logged_messages:
					await message.channel.send(msg)
			else:
				await message.channel.send("Stop the logging first !")
		
		elif(message.content[1:].lower() == 'log delete'):
			logged_messages = []
			await message.channel.send("Messages logs were deleted.")
		#############################################################

		else:
			await message.reply("Unrecognized command !")


	if('send feet' in message.content):
		await message.channel.send("BRUH")

client.run(token)
