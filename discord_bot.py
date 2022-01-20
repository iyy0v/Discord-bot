import discord, os


token = ""
server_name = ""
members = []

# you must enable the "SERVER MEMBERS INTENT" Privileged Gateway Intent under the bot settings in the Discord developer portal
intents = discord.Intents.default() 
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
	for server in client.guilds:
		if server.name == server_name:
			print(
        		f'{client.user} is connected to the following servers:\n'
       			f'{server.name} (id: {server.id})'
    		)
			break

	print("\n Users : ")
	for member in server.members:
		if(member.bot == False):
			print(f"  {member.name}#{member.discriminator} (Nickname: {member.nick})")


	print("\n Bots : ")
	for member in server.members:
		if(member.bot == True):
			print(f"  {member.name}#{member.discriminator} (Nickname: {member.nick})")

client.run(token)
