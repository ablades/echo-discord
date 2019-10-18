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

    if response.status_code == '404':
        print("Query not found")

    twitch_streams = json.loads(response.content)['streams']

    return twitch_streams
"""
 'streams':[ 
      { 
         '_id':35997734672,
         'game':'Diablo III: Reaper of Souls',
         'broadcast_platform':'live',
         'community_id':'',
         'community_ids':[  ],
         'viewers':961,
         'video_height':1080,
         'average_fps':30,
         'delay':0,
         'created_at':'2019-10-17T20:54:55Z',
         'is_playlist':False,
         'stream_type':'live',
         'preview':{  },
         'channel':{  }
      },

"""


#fetch arguments from commands
@bot.command()
async def fetch(ctx, arg):
    await ctx.send("TWITCH RESULTS")
    twitch_streams = await twitch_fetch(arg)
    await ctx.send("MIXERS RESULTS")
    mixer_json = await mixer_fetch(arg)

    print(twitch_streams[0]['game'])
    
    for stream in twitch_streams:
        await ctx.send(stream['channel']['url'])

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to {bot.guilds}")


if __name__ == "__main__":
    bot.run(BOT_TOKEN)
         