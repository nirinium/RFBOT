import discord
import json
from discord import Game
from discord.ext.commands import Bot

from imgurpython import ImgurClient
from random import randint
from time import sleep


# CONFIG
BOT_PREFIX = (">")
TOKEN = 'NDgwMTkzNzY0MzA5MDczOTIy.DlkScg.cdx33F83QtH7rLb9Unnce3WZk1Y'

client = Bot(command_prefix=BOT_PREFIX)

# From IMGUR
client_id = 'bdb67f6e22d322a'
client_secret = 'a01653158047ca1013a49a17a6a6cc9b26faa787'





# getMemes Function()
# Hits IMGUR API and returns imgur link
# By- Nick Conn
def get_meme():

    
    subreddits = [
        'holdmybeer',
        'funny',
        'whitepeopletwitter',
        'holdmyfries',
        'MemeEconomy',
        'wholesomememes',
        'dankmemes',
        'Whatcouldgowrong',
        'RedneckGifs',
        'gifs'
    ]
    # Get Length of list
    subRedditLength = len(subreddits)
    subRedditKey = randint(0, subRedditLength-1)

    # Plug this into api for a random subreddit
    subReddit = subreddits[subRedditKey]
    
    # Connect to Client
    client = ImgurClient(client_id, client_secret)


    # https://github.com/Imgur/imgurpython
    items = client.subreddit_gallery(subReddit, sort='top', window='day', page=0)


    # Grab the length of the dictionary returned from IMGUR
    imgurLength = len(items)

    if imgurLength != 0:
        # Get random element
        key = randint(0, imgurLength)

        # Grab random meme link
        link = items[key].link

        return link
    else:
        return 'Please try again!'


    

# ------------------------------- Main -------------------------------

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('>hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    # Lets make a meme feature!
    if message.content.startswith('>meme'):
        
        meme = get_meme()
        # msg = memes.format(message)
        msg = meme.format(message)
        await client.send_message(message.channel, msg)

        # IMGUR API nonsense
        sleep(2)

#keep
@client.event
async def on_ready():
    print('Logged in as | ' + client.user.name  + ' | ' + client.user.id)
    print('------------------------------------------')

#start client
client.run(TOKEN)


# ------------------------------- Main -------------------------------
