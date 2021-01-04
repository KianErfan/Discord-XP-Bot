import discord
import pymongo

from discord.ext import commands
from pymongo import MongoClient

import exp

cogs = [exp]

client = commands.Bot(command_prefix="?", intents=discord.Intents.all())


for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("Nzc2OTQxOTMyNjU1MjgwMTc4.X68Njw.87i6JBhR8edUAOGa6RcOa-Rce28")