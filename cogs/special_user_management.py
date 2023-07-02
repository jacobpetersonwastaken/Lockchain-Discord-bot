from discord.ext import commands
from dotenv import load_dotenv
import CONST
from helper_code import react_to_message

load_dotenv()

class SpecialUserManagement(commands.Cog):
    """A cog for managing the Golden Sage Minecraft server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        await self.handle_special_user_reactions(message)

    async def handle_special_user_reactions(self, message):
        """Gets the special user and reacts to them with their emoji"""
        special_user_role = message.author.id
        if special_user_role in CONST.SPECIAL_USERS:
            await react_to_message(message, self.bot, CONST.SPECIAL_USERS[special_user_role]["emoji"])



async def setup(bot):
    await bot.add_cog(SpecialUserManagement(bot))
