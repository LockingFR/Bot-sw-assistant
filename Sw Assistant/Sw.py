import discord
from discord.ext import commands, tasks
import asyncio



class Sw(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @discord.slash_command(name="hello",description="-")
  async def hello(self , ctx):
    await ctx.respond("Bonjour !")


  @discord.slash_command(name="gb12",description='-')
  async def gb12(self, ctx):  
  
    embed = discord.Embed(title=f"TITRE",description="DESC", color=0xeb571c)
    embed.add_field(name="Nom ligne",value="Valeur ligne")
    embed.set_thumbnail(url=f"{ctx.author.avatar.url}")
    embed.set_image(url=f"{ctx.author.avatar.url}")
    embed.set_footer(text="Footer")


    class MyButton(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View


        def __init__(self):
          super().__init__(timeout=None)
          
          videogb12 = discord.ui.Button(label='Video', emoji="<:ytb:1043234935005253742>",style=discord.ButtonStyle.gray, url='https://www.youtube.com/watch?v=nlevmj8xc9E')
          self.add_item(videogb12)



        async def on_timeout(selfBUTTON):
            await selfBUTTON.message.edit(view=None) #Retire les boutons du message a la fin du temps ! (view=None donc pas de bouton)





    await ctx.respond(embed=embed,view=MyButton())