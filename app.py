import discord
from discord.ext import commands
import asyncio
import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

API_ENDPOINT = 'https://discordapp.com/api/v6'
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix='$')


#fetch arguments from commands
@bot.command()
async def fetch(ctx, arg):
    await ctx.send(arg)
    args_list = ctx.args
    print(f"The argument: {args_list} and {arg}")

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to {bot.guilds}")


if __name__ == "__main__":
    bot.run(BOT_TOKEN)
         