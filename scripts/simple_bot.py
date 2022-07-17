import os

from dotenv import load_dotenv

import disnake
from disnake.ext import commands

load_dotenv()

intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot("!", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.command()
async def play(ctx, url: str):
    await ctx.send(f"Playing {url} 🎵")


bot.run(os.environ['TOKEN'])
