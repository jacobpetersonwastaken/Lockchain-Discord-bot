import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  
BOT_TOKEN = os.getenv("BOT_TOKEN")
cogs_dir = os.path.join(os.path.dirname(__file__), 'cogs')

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='~', intents=intents)

# Here you load your cog
@bot.event
async def on_ready():
    print('Bot is ready.')
    try:
        for f in os.listdir(cogs_dir):
            if f.endswith(".py"):
                await bot.load_extension("cogs."+f[:-3])
    except Exception as e:
        print(e)

bot.run(BOT_TOKEN)
