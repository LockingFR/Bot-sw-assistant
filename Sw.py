import discord
from discord.ext import commands, tasks
import asyncio



class Sw(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  #Partie Commandes

  @discord.slash_command(name="aide", description='La liste des commandes')
  async def help(self, ctx):
    
    embed_help = discord.Embed(title=f'Voici la liste des commandes', description="Tu verras toute les commandes que tu peux éxécuter ci-dessous, n'histe pas à tout observer ! Si tu veux voir cette liste dans tes messages privés, clique sur la réaction en bas.", color=0xeb571c )
    embed_help.add_field(name="Les commandes pour le donjon de cairos :", value="/gb12 pour afficher des teams ainsi que des aides pour gb12 facilement\n/db12 pour afficher des teams ainsi que des aides pour db12 facilement")
    #embed_help.add_field(name="\u200b", value="/db12 pour afficher des teams ainsi que des aides pour db12 facilement")


    try :
      await ctx.author.send(embed=embed_help)
    except discord.errors.Forbidden:
      await ctx.respond("Tes MP sont fermés, je ne peux pas t'envoyer l'aide en privé !", ephemeral=True)


    await ctx.respond(embed=embed_help,ephemeral=True)


  @discord.slash_command(name="hello",description="-")
  async def hello(self , ctx):
    await ctx.respond("Bonjour !")



  @discord.slash_command(name="start", description='Tous ce que tu as besoin de savoir sur le bot !')
  async def start(self, ctx):
    
    embed_start = discord.Embed(title=f'Qui suis-je ?', description="Je suis un robot développé par LockingFR, expérimental qui vous permet de visualiser des aides pour Summoners War !", color=0xeb571c)


    await ctx.respond(embed=embed_start) #L'argument embed= defini un embed ; Embed_start c le nom du tien / Si tu veut un bouton dans une commande différente, il faudra recreer une classe 
    #tu peux check la doc des boutons la : https://guide.pycord.dev/interactions/ui-components/buttons/

