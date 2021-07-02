from discord.ext import commands
from discord import Message
from dotenv import load_dotenv
from os import getenv
import discord
art = '''
   ___       __             __
  / _ \___  / /__ ____  ___/ /
 / , _/ _ \/ / _ `/ _ \/ _  / 
/_/|_|\___/_/\_,_/_//_/\_,_/                                                                    
'''
description = art+'''Simple Bot to scrape text from channel histories.
It also can interface with RNGTube database for random videos.'''
intents = discord.Intents.default()
intents.members = True
extensions = ['cogs.randomStuff',
                'cogs.tools',
                'cogs.developer',
                'cogs.moderation']

load_dotenv()


bot = commands.Bot(command_prefix='?', description=description, intents=intents)
if __name__ == "__main__":
    for extension in extensions:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    print(art,end="")
    print("INFO".center(40,"="))
    print("Discord Version: ",discord.__version__)
    print('Logged in as ',end='')
    print(bot.user.name + ": " + str(bot.user.id))
    print("="*40)
    print("Connected to..")
    servers = list(bot.guilds)
    cnt = len(servers)
    for i in range(cnt):
        print(str(i) + " " + str(servers[i]) + " : " + str(servers[i].id))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='?help'))


#.env file must be in the same directory as this file
#must have a .env file with your dev token.
bot.run(getenv("TOKEN"), bot=True, reconnect=True)