# id 500680030322425866
# token NTAwNjgwMDMwMzIyNDI1ODY2.DqOzuw.sv9MJPwO6V2HGP8F5FMnuRgMpYc
# permission 67648

#https://discordapp.com/oauth2/authorize?client_id=500680030322425866&scope=bot&permissions=67648

import discord

client = discord.Client()

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author}: {message.author.name}:{message.content} ")

	if 'hi there' in message.content.lower():
		await client.send_message(message.channel, content = "Hello!")
		print("pass")
		# pass



client.run("NTAwNjgwMDMwMzIyNDI1ODY2.DqOzuw.sv9MJPwO6V2HGP8F5FMnuRgMpYc")