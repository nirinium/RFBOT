import discord
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = (">")
TOKEN = ''

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('>hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

#keep
@client.event
async def on_ready():
    print('Logged in as | ' + client.user.name  + ' | ' + client.user.id)
    print('------------------------------------------')

#start client
client.run(TOKEN)
