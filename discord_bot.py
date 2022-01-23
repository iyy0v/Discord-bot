import discord, os, random


token = "" 		# <--- put the bot's token here
server_name = ""	# <--- put the server's name here
prefix = '$'		# <--- put the bot's command prefix that you like ('$' by default)

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

	# COMMANDS SECTION
	if(message.content[0] == prefix):
		if(message.content[1:].lower() in greetings):
			greeting = greetings[random.randint(0,len(greetings)-1)].capitalize()
			await message.reply(greeting + " !")
		
		elif(message.content[1:].lower() == 'twerk'):
			await message.channel.send("NO")

		# Return the invite link for the bot
		elif(message.content[1:].lower() == 'invite'):
			await message.channel.send(discord.utils.oauth_url(client_id))

		# Delete message
		elif(message.content[1:8].lower() == 'delete '):
			permission = False
			for role in message.author.roles:
				if role.permissions.manage_messages == True or role.permissions.administrator == True:
					permission = True
			if permission:
				if(message.content[8:].isdigit()):
					await message.channel.purge(limit=int(message.content[8:])+1)
				else:
					await message.channel.send("Invalid number !")

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

		# kick a member 
		elif(message.content[1:6].lower() == 'kick '):
			permission = False
			for role in message.author.roles:
				if role.permissions.ban_members == True or role.permissions.administrator == True:
					permission = True
			if permission:
				member_kicked = discord.utils.get(message.guild.members, name=message.content[6:-5], discriminator=message.content[-4:])
				if(member_kicked == None):
					await message.channel.send(f"Incorrect name: {message.content[6:-5]}#{message.content[-4:]}")
				else:
					await message.channel.send(f"{member_kicked.name}#{member_kicked.discriminator} was KICKED !")
			else:
				await message.channel.send("You don't have the permission to do that.")
		
		# ban a member 
		elif(message.content[1:5].lower() == 'ban '):
			permission = False
			for role in message.author.roles:
				if role.permissions.ban_members == True or role.permissions.administrator == True:
					permission = True
			if permission:
				member_banned = discord.utils.get(message.guild.members, name=message.content[5:-5], discriminator=message.content[-4:])
				if(member_banned == None):
					await message.channel.send(f"Incorrect name: {message.content[5:-5]}#{message.content[-4:]}")
				else:
					await message.channel.send(f"{member_banned.name}#{member_banned.discriminator} was BANNED !")
			else:
				await message.channel.send("You don't have the permission to do that.")
		

		#############################################################
		
		else:
			await message.reply("Unrecognized command !")


	if('send feet' in message.content):
		await message.channel.send("BRUH")

client.run(token)
