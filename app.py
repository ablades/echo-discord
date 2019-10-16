import discord
import asyncio
import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

API_ENDPOINT = 'https://discordapp.com/api/v6'
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

client = discord.Client()

def get_token():
  data = {
    'grant_type': 'client_credentials',
    'scope': 'identify connections'
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
  r.raise_for_status()
  print(r.json())
  return r.json()

@client.event
async def login_user():
    pass

@client.event
async def on_ready(self):
    print(self.user.name)

    print(client.servers)

if __name__ == "__main__":
    get_token()
         