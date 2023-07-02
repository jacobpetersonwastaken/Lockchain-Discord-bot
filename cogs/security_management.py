from discord.ext import commands
from dotenv import load_dotenv
import os
import CONST
from helper_code import react_to_message

load_dotenv()
file_not_allowed_template = """{} no compressed/ compiled files. Post the github link.\n 
{}"""

class SecurityManagement(commands.Cog):
    """A cog for managing the Golden Sage Minecraft server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        await self.handle_file_types(message)

    async def handle_file_types(self, message):
        """Removes forbidden file types"""
        for attachment in message.attachments:
            _, ext = os.path.splitext(attachment.filename)
            if ext.lower() in CONST.FORBIDDEN_FILE_TYPES:
                await message.delete()
                await message.channel.send(file_not_allowed_template.format(message.author.mention, CONST.IM_IN_DANGER))
                return  # Stop processing this message

        await self.bot.process_commands(message)  # Continue processing other commands


async def setup(bot):
    await bot.add_cog(SecurityManagement(bot))
