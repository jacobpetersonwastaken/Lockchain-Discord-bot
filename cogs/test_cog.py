from discord.ext import commands
from dotenv import load_dotenv
import CONST
from helper_code import react_to_message

load_dotenv()



class CogExample(commands.Cog):
    """A simple example of a discord bot cog."""
    def __init__(self, bot):
        """Class takes the bot as a param and initializes it."""
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """@commands.Cog.listener() decorator listens for things like messages but returns if it sees its own message, as to not reply to itself."""
        if message.author.bot:
            return

        if message.author.id == CONST.kitty_id:
            """Here we get the message and respond if it sees a specific user id."""
            await message.channel.send("Hey, I'm a bot responding because I saw that you are the chosen one")
            return

    @commands.command()
    async def hello(self, ctx):
        """To listen for commands within a commands.Cog in discord.py, you'll primarily use the @commands.command() decorator.
        The method that follows this decorator will be treated as a command. Check the command prefix in Main_Start_Here,this will listen for that prefix.
        Currently, its set to !"""
        await ctx.send("Hello, world!")

async def setup(bot):
    await bot.add_cog(CogExample(bot))
