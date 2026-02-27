import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot ready")

bot.run(os.getenv("srv-d6gtfdua2pns7386d4e0?key=yZT1qF1wUww"))
