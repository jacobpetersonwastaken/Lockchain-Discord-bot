from discord.ext import commands
from dotenv import load_dotenv
import CONST
from helper_code import react_to_message

load_dotenv()

class LeadershipUserManagement(commands.Cog):
    """A cog for managing the Golden Sage Minecraft server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        await self.handle_admin_emoji(message)
        await self.handle_mod_emoji(message)

    async def handle_admin_emoji(self, message):
        """Gets the admin users and reacts to them with their emoji"""
        author_roles = [role.id for role in message.author.roles]
        if CONST.ROLE_ID_admin in author_roles:
            await react_to_message(message, self.bot, CONST.EMOJI_ADMIN)

    async def handle_mod_emoji(self, message):
        """Gets the mod users and reacts to them with their emoji"""
        author_roles = [role.id for role in message.author.roles]
        if CONST.ROLE_ID_mod in author_roles:
            await react_to_message(message, self.bot, CONST.EMOJI_MOD)



async def setup(bot):
    await bot.add_cog(LeadershipUserManagement(bot))
