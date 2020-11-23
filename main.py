import discord
from messageEventHandler import MessageEventHandler

# Loading DISCORD_TOKEN from .env
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Gets Discord Client (in this case synonymous with Bot)
bot = discord.Client()

# Startup Event Listener
@bot.event
async def on_ready():
	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1

	print("SherlockBot is in " + str(guild_count) + " guilds.")

# New Message Event Listener
@bot.event
async def on_message(message):
	if(message.author.id != 779447264380059680):
		await MessageEventHandler.EvaluateMessage(message)

# Runs Bot with specified token
bot.run(DISCORD_TOKEN)