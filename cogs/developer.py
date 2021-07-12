from discord.ext import commands
from discord import Message
import pandas as pd
import discord

class Developer(commands.Cog):  
    """Developer Tools"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def recallBot(self, ctx:commands.Context, serverID:int):
        """Remove Roland from a server."""
        await ctx.send("Ok, leaving the guild..", delete_after=10)
        await self.bot.get_guild(serverID).leave()

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
                    try:

                        if (ctx.guild.get_member(msg.author.id) is not None
                             and 'opt-out' not in [str(role) for role in msg.author.roles] 
                             and not msg.attachments):
                            data = data.append({'user':msg.author.name,\
                                                'content':msg.content,\
                                                'roles':[str(role) for role in msg.author.roles],\
                                                'time':msg.created_at}, ignore_index=True)
                    except Exception as e:
                        print(e, msg.author.name)

              

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

    @commands.command()
    @commands.is_owner()
    async def purgeBot(self, ctx:commands.Context, amount=25, channel:str="currentChannel"):
        """ Remove bot messages from a channel """
        msgs=[]
        if channel != 'currentChannel':
            channel = discord.utils.get(ctx.guild.channels, name=channel)
        else:
            channel = ctx.message.channel

        async for msg in ctx.channel.history():
            if len(msgs) == amount:
                break
            if msg.author == ctx.bot.user:
                msgs.append(msg)
        await ctx.channel.delete_messages(msgs)
        answer = discord.Embed(title="Self Purge Complete!",
                                   description=f"""`Server` : **{ctx.message.guild.name}**\n`Channel` : **{channel.name}**\n`Messages Removed` : **{amount}**""",
                                   colour=0xff0000) 
        await ctx.message.channel.send(embed=answer, delete_after=20)

def setup(bot: commands.Bot):
    bot.add_cog(Developer(bot))





