import discord
import pymongo

from discord.ext import commands
from pymongo import MongoClient

import exp

token = open("token.txt","r").read()

cogs = [exp, ready]

client = commands.Bot(command_prefix="?", intents=discord.Intents.all())
client.remove_command("help")


for i in range(len(cogs)):
    cogs[i].setup(client)


client.run(token)
