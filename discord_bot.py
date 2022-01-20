import discord, os, random


token = ""
server_name = ""
members = []


greetings = ['hello','hi','yo','salute','whats up','wassup','hey']
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
	print(
		f'#{message.channel.name}/{message.author.name}#{message.author.discriminator}: {message.content}'
	)
	if(message.content[0] == '$'):
		if(message.content[1:].lower() in greetings):
			greeting = greetings[random.randint(0,len(greetings)-1)].capitalize()
			await message.reply(greeting + " !")



'''
	print("\n Users : ")
	for member in server.members:
		if(member.bot == False):
			print(f"  {member.name}#{member.discriminator} (Nickname: {member.nick})")


	print("\n Bots : ")
	for member in server.members:
		if(member.bot == True):
			print(f"  {member.name}#{member.discriminator} (Nickname: {member.nick})")
'''


client.run(token)
