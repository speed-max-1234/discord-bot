import os
os.environ["DISCORD_NO_VOICE"] = "1"

import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(os.getenv("srv-d6gtfdua2pns7386d4e0?key=yZT1qF1wUww"))
