import discord
from discord.ext import commands, tasks
import asyncio


class cairos(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @discord.slash_command(name="gb12",description='Tu trouveras des aides pour le Géant')
  async def gb12(self, ctx):  
  
    embed = discord.Embed(title=f"Besoin d'aide pour le Géant ? Tu es au bon endroit !",description="DESC", color=0xeb571c)
    embed.add_field(name="Nom ligne",value="Valeur ligne")
    embed.set_thumbnail(url=f"{ctx.author.avatar.url}")
    embed.set_image(url=f"{ctx.author.avatar.url}")
    embed.set_footer(text="Footer")

    class MyButton(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View


        def __init__(self):
          super().__init__(timeout=None)
          
          videogb12 = discord.ui.Button(label='Vidéo', emoji="<:ytb:1043234935005253742>",style=discord.ButtonStyle.gray, url='https://www.youtube.com/watch?v=nlevmj8xc9E')
          self.add_item(videogb12)



        async def on_timeout(selfBUTTON):
            await selfBUTTON.message.edit(view=None) #Retire les boutons du message a la fin du temps ! (view=None donc pas de bouton)
    
    await ctx.respond(embed=embed,view=MyButton())
  
  
  
  @discord.slash_command(name="db12", description='Tu trouveras des aides pour le Dragon')
  async def db12(self, ctx):
    
    db12 = discord.Embed(title=f"Besoin d'aide pour db12 ? Tu es au bon endroit", description="Tout ce que tu as besoin pour speedrun db12 se trouve ici ! ", color=0xeb571c )
    db12.set_footer(text="Footer")

    class MyButton2(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View


        def __init__(self):
          super().__init__(timeout=None)
          
          videodb12 = discord.ui.Button(label='Vidéo', emoji="<:ytb:1043234935005253742>",style=discord.ButtonStyle.gray, url='https://www.youtube.com/watch?v=-QZohMlBPw0')
          self.add_item(videodb12)



        async def on_timeout(selfBUTTON):
            await selfBUTTON.message.edit(view=None) #Retire les boutons du message a la fin du temps ! (view=None donc pas de bouton)
    
    
    
    await ctx.respond(embed=db12, view=MyButton2())