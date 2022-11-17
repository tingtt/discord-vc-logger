#-*- -*- -*- -*- -*- -*- -*- -*- coding:UTF-8 -*- -*- -*- -*- -*- -*- -*- -*- -
import os
import datetime
import discord
#-*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*
intents = discord.Intents.default()
client = discord.Client(intents=intents)

TOKEN = os.environ['TOKEN']
GUILD_ID = os.environ['GUILD_ID']
CHANNEL_ID = os.environ['CHANNEL_ID']

if TOKEN == '':
  raise ValueError("environment variable 'TOKEN' required")
if GUILD_ID == '':
  raise ValueError("environment variable 'GUILD_ID' required")
if CHANNEL_ID == '':
  raise ValueError("environment variable 'CHANNEL_ID' required")

@client.event
async def on_ready():
  print(client.user.name)
  print(client.user.id)
  print('------')

@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == int(GUILD_ID):
        text_ch = client.get_channel(int(CHANNEL_ID))
        if before.channel is None:
            nowtime = datetime.datetime.utcnow()
            nowtime = nowtime + datetime.timedelta(hours=9)
            nowtime = nowtime.strftime("%Y-%m-%dT%H:%M:%S")
            msg = f'{nowtime} {member.name} joined to <#{after.channel.id}>'
            await text_ch.send(msg)

client.run(TOKEN)