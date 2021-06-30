from discord.ext import commands
from discord import Message
import pandas as pd
import discord

class developer(commands.Cog):  
    """Basic Server Tools"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def clip(self, ctx:commands.Context, limit:int=10, channel:str="currentChannel"):
        """
            Clip Channel History to a .CSV file. 

        """
        if channel != 'currentChannel':
            channel = discord.utils.get(ctx.guild.channels, name=channel)
        else:
            channel = ctx.message.channel
        data = pd.DataFrame(columns=['user','content','roles','time'])
        async for msg in channel.history(limit=limit+1000):
                if msg.author != ctx.bot.user and ctx.bot.command_prefix not in msg.content:     
                    if 'opt-out' not in [str(role) for role in msg.author.roles]:
                        data = data.append({'user':msg.author.name,\
                                            'content':msg.content,\
                                            'roles':[str(role) for role in msg.author.roles],\
                                            'time':msg.created_at}, ignore_index=True)
                    if len(data) == limit:
                        break
        file_location = f"{str(ctx.channel.guild) + '_' + str(channel)}.csv" 
        data.to_csv(file_location)

        answer = discord.Embed(title="Clip Complete!",
                                       description=f"""`Server` : **{ctx.message.guild.name}**\n`Channel` : **{channel.name}**\n`Messages Read` : **{limit}**""",
                                       colour=0xff0000) 
        await ctx.message.channel.send(embed=answer, delete_after=10)

    @commands.command()
    async def source(self, ctx:commands.Context):
        """ Roland's Source Code on GitHub
        """
        await ctx.send("https://github.com/fresh-patches/Roland.git")


def setup(bot: commands.Bot):
    bot.add_cog(developer(bot))





