import discord
import CONST

async def react_to_message(message, bot, emoji: str):
    """Reacts to a players message with a specified emoji"""
    get_emoji = discord.utils.get(bot.emojis, name=emoji)
    await message.add_reaction(get_emoji)
