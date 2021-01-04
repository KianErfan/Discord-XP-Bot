import discord
from discord.ext import commands
from pymongo import MongoClient

bot_channel = 794587190817718272
talk_channel = [767826793415180339, 705194793520857138, 794332497151524964, 794332373265022987, 794332619809620038, 794256875134124053, 794329957987647508, ]

level = ["Level 5+" , "Level 10+", "Level 15+"]
levelnum = [5,10,15]

cluster = MongoClient("mongodb+srv://KianErfan:36272002kian@discordbot.jr8ty.mongodb.net/DiscordBot?retryWrites=true&w=majority")

levelling = cluster["XP"]["Levels"]

class exp(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready To Collect XP")
    

    @commands.Cog.listener()
    async def on_message(self, message):
      print(message.author)
      print(message)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_channel:
            stats = levelling.find_one({"id" : message.author.id})
            if not message.author.bot:
                if stats is None:
                    newsuser = {"id" : message.author.id, "xp" : 20}
                    levelling.insert_one(newsuser)
                else:
                    xp = stats["xp"] + 5
                    levelling.update_one({"id":message.author.id}, {"$set":{"xp":xp}})
                    lvl = 0 
                    while True:
                        if xp < ((50*(lvl**2)+(50*(lvl)))):
                            break
                        lvl += 1
                    xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                    if xp == 0:
                        await message.channel.send(f"<:pog:795449196034916382> {message.author.mention}! You leveled up to level {lvl}.")
                        for i in range(len(level)):
                            if lvl == levelnum[i]:
                                await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
                                embed = discord.Embed(description=f"{message.author.mention} you have achieved the role **{level[i]}**! Congrats")
                                embed.set_thumbnail(url=message.avatar.url)
                                await message.channel.send(embed=embed)

    @commands.command()
    async def rank(self, ctx):
        if ctx.channel.id == bot_channel:
            stats = levelling.find_one({"id": ctx.author.id})
            if stats is None:
                embed = discord.Embed(description= "You need to send a message first to earn some rank")
                await ctx.channel.send(embed= embed)
            else:
                xp = stats["xp"]
                lvl = 0 
                rank = 0
                while True:
                        if xp < ((50*(lvl**2)+(50*(lvl)))):
                            break
                        lvl += 1
                xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                boxes = int((xp/(200*((1/2) * lvl)))*10)
                ranking = levelling.find().sort("xp", -1)
                for x in ranking:
                    rank += 1
                    if stats["id"] == x["id"]:
                        break
                
                embed = discord.Embed(title = "{}'s level stats".format(ctx.author.name), color=0x00FF00)
                embed.add_field(name = "Name" , value = ctx.author.mention, inline = True)
                embed.add_field(name = "Xp" , value=f"{xp}/{int(200*((0.5)*lvl))}", inline = True)
                embed.add_field(name = "Rank" ,value=f"{rank}/{ctx.guild.member_count}", inline = True)
                embed.add_field(name = "Progress Bar" , value = boxes * "<:dead:795447837537599509>" + (10-boxes) * '<:alive:795447837109387295>' , inline = True)
                embed.set_thumbnail(url = ctx.author.avatar_url)
                await ctx.channel.send(embed = embed)

    @commands.command()
    async def leaderboard(self, ctx):
        if ctx.channel.id == bot_channel:
            ranking = levelling.find().sort("xp", -1)
            i = 1
            embed = discord.Embed(title = "Rankings:")
            for x in ranking:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["xp"]
                    embed.add_field(name=f"{i}: {temp.name}", value=f"Total XP: {tempxp}", inline=False)
                    i += 1
                except:
                    pass
                if i == 11:
                    break
            await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(exp(client))
