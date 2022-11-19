import discord
from discord.ext import commands, tasks
import token2



# Importation des cogs
import Sw
import cairos


bot = commands.Bot(
    command_prefix='!',
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



bot.remove_command("help") #Retire la commande help basique







bot.add_cog(cairos.cairos(bot))
bot.add_cog(Sw.Sw(bot))

bot.run(token2.token)