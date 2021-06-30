from discord.ext import commands
from discord import Message
import discord
import random
import requests


class tools(commands.Cog):  
    """Basic Server Tools"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Get latency"""
        await ctx.send(f':ping_pong: Pong {round(self.bot.latency*1000)}ms')

    @commands.command()
    async def joined(self, ctx:commands.Context, member: discord.Member):
        """Get date and time  when a member joined."""
        await ctx.send(f':passport_control: {member.name} joined in {member.joined_at}')

    @commands.command(pass_context=True)
    async def setRole(self, ctx:commands.Context, role:discord.Role):
        """
            Allows users to assign their roles.
            If user already has role it will be unassigned.

        """
        if role in ctx.message.author.roles:
            await ctx.author.remove_roles(role)
            await ctx.send(f"{ctx.author.name} has removed their role of {role.name}.")
        else:

            await ctx.author.add_roles(role)
            await ctx.send(f"{ctx.author.name} has been given the role of {role.name}.")

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
    bot.add_cog(tools(bot))