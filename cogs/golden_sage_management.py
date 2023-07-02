from discord.ext import commands
from dotenv import load_dotenv
import CONST
from helper_code import react_to_message

load_dotenv()


joining_whitelist_message_template = """# Welcome to the Senzu 👑Golden Sage Minecraft Server! \n### Our server mods have been notified and you will be *added* to the whitelist *shortly* with the username: **`{}`** \n### Server Info
- Vanilla minecraft server 1.20
- Survival
- Hard
- Server address `51.81.167.237:25770`"""


class GoldenSageManagement(commands.Cog):
    """A cog for managing the Golden Sage Minecraft server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        await self.handle_paid_roles(message)
        await self.handle_onboarding(message)

    async def handle_paid_roles(self, message):
        author_roles = [role.id for role in message.author.roles]
        if any(role in author_roles for role in CONST.PAID_ROLE):
            await react_to_message(message, self.bot, CONST.EMOJI_GOLDEN_SAGE)

    async def handle_onboarding(self, message):
        if message.channel.id == CONST.CHANNEL_join_golden_sage:
            if message.content.startswith("Username:"):
                username = message.content.split("Username:")[1].strip()
                await self.add_user_to_whitelist(username, message)
            else:
                await message.delete()

    async def add_user_to_whitelist(self, username, message):
        mod_whitelist_alert_message = f"<@{CONST.USER_ID_lockchain}>\n<@&{CONST.ROLE_ID_minecraft_mod}>\nPlease add *{username}* to the whitelist \n\nCommand: `~whitelist add {username}`"
        mod_channel = self.bot.get_channel(CONST.CHANNEL_minecraft_mod)
        await mod_channel.send(mod_whitelist_alert_message)
        await message.author.send(joining_whitelist_message_template.format(username))
        await message.delete()


async def setup(bot):
    await bot.add_cog(GoldenSageManagement(bot))
