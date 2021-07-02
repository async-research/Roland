from discord.ext import commands
from discord import Message
import random
import requests


class Random(commands.Cog):  
    """Everything random."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.vids = []
        self.cookies = [cookie.strip() for cookie in open('./src/fortune_cookies.txt','r').readlines()]
        self.dadJokes = [joke.strip().split("<>") for joke in open('./src/dadJokes.txt','r').readlines()]   


    @commands.command()
    async def rng(self, ctx: commands.Context, upto:int=6):
        """
            Generate a random number.

        """
        await ctx.send(":game_die: Rolled a " + str(random.randint(0, upto)))

    @commands.command()
    async def fortuneCookie(self, ctx: commands.Context):
        """
            Get a fortune cookie.
            Source: https://github.com/ianli/fortune-cookies-galore/blob/master/fortunes.txt
        """
        await ctx.send(":fortune_cookie: \"" + random.choice(self.cookies) + "\"")

    @commands.command()
    async def dadJoke(self, ctx:commands.Context):
        """
            Get a Dad Joke.
            Source: https://github.com/yesinteractive/dadjokes/blob/master/controllers/jokes.txt
        """
        await ctx.send(" \n".join(random.choice(self.dadJokes)))

    @commands.command()
    async def randomVideo(self, ctx: commands.Context):
        """
            Get a random video.

        """
       
        url = "https://rngtube.com/controller.php?state=rolling&filter=Mix"
        if self.vids == []:
            result = requests.get(url, verify=False)
            self.vids = result.json()['arr']
            record = self.vids.pop()
            videoID = record['videoID']
            word = record['rngQuery']
        else:
            record= self.vids.pop()
            videoID = record['videoID']
            word = record['rngQuery']
        await ctx.send("**Catch Phrase:** __" + word + '__\nhttps://www.youtube.com/watch?v=' + videoID)

    @randomVideo.error
    async def rngtube_error(self, ctx:commands.Context, error):
        await ctx.send("RNGTube Not Availiable. BARNEY ERROR 404 ")
        #print(":construction: This feature is undercontruction. :construction: ")
        
    



def setup(bot: commands.Bot):
    bot.add_cog(Random(bot))