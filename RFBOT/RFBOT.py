import discord
import json
from discord import Game
from discord.ext.commands import Bot

# Reddit scraper stuff
import requests, urllib
import os, sys, time


# CONFIG
BOT_PREFIX = (">")
TOKEN = 'NDgwMTkzNzY0MzA5MDczOTIy.DlkScg.cdx33F83QtH7rLb9Unnce3WZk1Y'

client = Bot(command_prefix=BOT_PREFIX)



# Helper Functions


# ------------------------------------------------------------------
# https://srikarg.github.io/blog/reddit-image-scraper-with-python/
# def getPosts(subreddit, postLimit):
#     url = 'http://www.reddit.com/r/' + subreddit + '/.json?limit=' + str(postLimit)
#     headers = {
#     'User-Agent': 'Reddit Wallpaper Scraper 1.0'
#     }
#     r = requests.get(url, headers=headers)
#     if r.status_code == requests.codes.ok:
#         data = r.json()
#         print('Sleeping for 3 seconds...\n')
#         time.sleep(3)
#         return data['data']['children']
#     else:
#         text = ('Sorry, but there was an error retrieving the subreddit\'s data!')
#         return text

# def saveImages(posts, scoreLimit, save_dir='reddit_wallpapers'):
#     for post in posts:
#         url = post['data']['url']
#         score = post['data']['score']
#         title = post['data']['title']
#         if 'i.imgur.com' in url and score > scoreLimit:
#             saveImage(url, title, save_dir)

# def saveImage(url, title, save_dir):
#     global counter
#     save_dir = makeSaveDir(save_dir)
#     dot_location = url.rfind('.')
#     filename = (save_dir + title.replace('/', ':') + url[dot_location: dot_location + 4]).encode('utf-8')
#     if not os.path.exists(filename):
#         print('Saving ' + filename + '!\n')
#         counter += 1
#         urllib.urlretrieve(url, filename)

# def makeSaveDir(dir):
#     if not os.path.exists(dir):
#         os.makedirs(dir)
#     return dir + '/'

# def downloadImagesFromReddit(subreddits, postLimit=100, scoreLimit=20):
#     for subreddit in subreddits:
#         posts = getPosts(subreddit, postLimit)
#         # saveImages(posts, scoreLimit, subreddit.lower())
#     return str(posts)

# ------------------------------------------------------------------


# def get_memes():
#         images = downloadImagesFromReddit([
#             'wallpapers'
#         ])

#         return str(images);




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
        # memes = get_memes()
        
        # msg = memes.format(message)
        # msg = 'A MEME YOU SAY?'.format(message)
        print "MEME!!!!!!";
        await client.send_message(message.channel, msg)

#keep
@client.event
async def on_ready():
    print('Logged in as | ' + client.user.name  + ' | ' + client.user.id)
    print('------------------------------------------')

#start client
client.run(TOKEN)
