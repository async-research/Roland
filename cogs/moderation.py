from discord.ext import commands
from discord import Message
import discord
import random
import requests


class Moderation(commands.Cog):  
    """Tools for Moderators and Administrators"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx:commands.Context, amount=25, channel:str="currentChannel"):
        """ Remove messages from channel """
        if channel != 'currentChannel':
            channel = discord.utils.get(ctx.guild.channels, name=channel)
        else:
            channel = ctx.message.channel
        await channel.purge(limit=amount)
        answer = discord.Embed(title="Purge Complete!",
                                       description=f"""`Server` : **{ctx.message.guild.name}**\n`Channel` : **{channel.name}**\n`Messages Removed` : **{amount}**""",
                                       colour=0xff0000) 
        await ctx.message.channel.send(embed=answer, delete_after=20)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def leave(self, ctx:commands.Context):
        """Remove Roland from your server"""
        await ctx.send("Ok, leaving the guild..")
        await self.bot.get_guild(ctx.guild.id).leave()


def setup(bot: commands.Bot):
    bot.add_cog(Moderation(bot))