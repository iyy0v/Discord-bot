import discord, os


token = ""
server_name = ""

client = discord.Client()

@client.event
async def on_ready():
	for server in client.guilds:
		if server.name == server_name:
			print(
        		f'{client.user} is connected to the following servers:\n'
       			f'{server.name} (id: {server.id})'
    		)
    		break


client.run(token)
