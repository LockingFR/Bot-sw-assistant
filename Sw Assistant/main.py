import discord
from discord.ext import commands, tasks
import token2



# Importation des cogs
from Sw import Sw


bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('!'),
    description=
    f"-",
    intents = discord.Intents.all(),
    case_insensitive=True)



@bot.event
async def on_ready():
    print("Le bot est lancé")



@bot.command
async def hello(ctx):
  await ctx.respond("Hello")







bot.add_cog(Sw(bot))

bot.run(token2.token)