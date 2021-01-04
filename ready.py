import discord

from discord.ext import commands

class ready(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="Your Xp"))
        
        
def setup(client):
    client.add_cog(ready(client))
