import discord
import pymongo

from discord.ext import commands
from pymongo import MongoClient

import exp
import token

cogs = [exp]

client = commands.Bot(command_prefix="?", intents=discord.Intents.all())
client.remove_command("help")


for i in range(len(cogs)):
    cogs[i].setup(client)


client.run(token.txt)
