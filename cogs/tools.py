from discord.ext import commands
from discord import Message
import discord
import random
import requests


class Tools(commands.Cog):  
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
    async def flag(self, ctx:commands.Context, message_id:int):
        """Remove something that Roland has sent"""
        msg = await ctx.fetch_message(message_id)
        if msg.author == ctx.bot.user:
            await ctx.channel.delete_messages([msg])
            await ctx.send(f'Deleted Message with message_id:{message_id}', delete_after=10)
        else:
            await ctx.send("Error Message ID does not belong to Roland!")


    
def setup(bot: commands.Bot):
    bot.add_cog(Tools(bot))