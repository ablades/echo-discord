import discord
from discord.ext import commands
import asyncio
import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

DISCORD_ID = os.getenv("DISCORD_ID")
DISCORD_SECRET = os.getenv("DISCORD_SECRET")
BOT_TOKEN = os.getenv("BOT_TOKEN")
TWITCH_ID = os.getenv("TWITCH_ID")
TWITCH_SECRET = os.getenv("TWITCH_SECRET")

bot = commands.Bot(command_prefix='$')

async def twitch_fetch():

    headers = {
        'Client-ID': TWITCH_ID,
    }

    params = (
        ('game_id', '33214'),
    )

    response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=params)

    print(response.json())


#fetch arguments from commands
@bot.command()
async def fetch(ctx, arg):
    await ctx.send(arg)
    await twitch_fetch()
    args_list = ctx.args
    print(f"The argument: {args_list} and {arg}")

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to {bot.guilds}")


if __name__ == "__main__":
    bot.run(BOT_TOKEN)
         