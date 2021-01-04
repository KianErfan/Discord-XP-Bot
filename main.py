import discord
import pymongo

from discord.ext import commands
from pymongo import MongoClient

import exp

token = open("token.txt","r").read()

cogs = [exp]

client = commands.Bot(command_prefix="?", intents=discord.Intents.all())
client.remove_command("help")

def on_ready()
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Your Xp"))

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run(token)
