import discord
from discord.ext import commands
import asyncio
import requests
import os, sys
import json
from dotenv import load_dotenv
load_dotenv()

DISCORD_ID = os.getenv("DISCORD_ID")
DISCORD_SECRET = os.getenv("DISCORD_SECRET")
BOT_TOKEN = os.getenv("BOT_TOKEN")
TWITCH_ID = os.getenv("TWITCH_ID")
TWITCH_SECRET = os.getenv("TWITCH_SECRET")
MIXER_ID = os.getenv("MIXER_ID")
bot = commands.Bot(command_prefix='$')

#fetch results from mixer
async def mixer_fetch(game_name):
    s = requests.Session()
    s.headers.update({'Client-ID': MIXER_ID})

    response = s.get(f'https://mixer.com/api/v1/channels/{game_name}')

    return response.json()

#Fetch results from twitch
async def twitch_fetch(game_name):

    headers = {
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Client-ID': TWITCH_ID,
    }

    params = (
        ('query', game_name),
    )


    response = requests.get('https://api.twitch.tv/kraken/search/streams', headers=headers, params=params)

    return response.json()


#fetch arguments from commands
@bot.command()
async def fetch(ctx, arg):
    await ctx.send("TWITCH RESULTS")
    await ctx.send(await twitch_fetch(arg))
    await ctx.send("MIXERS RESULTS")
    await ctx.send(await mixer_fetch(arg))

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to {bot.guilds}")


if __name__ == "__main__":
    bot.run(BOT_TOKEN)
         