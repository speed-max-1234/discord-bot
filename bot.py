import os
os.environ["DISCORD_NO_VOICE"] = "1"

import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(os.getenv("MTQ3Njk3MzQzNjIzMTM1NjQ3Nw.GAjJ_y.yh8IXuTspSFAyb1MOvpxhC-ZSQ5JO6wixRqD2o"))
