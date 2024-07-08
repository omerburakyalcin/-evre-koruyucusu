import discord
from discord.ext import commands
import random
import os
from bot_token import token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
cevre_bilinci_listesi = ["Yerlere çöp atan insanları uyarmalıyız" ,
                         "toplu taşıma kullanımını arttırmalıyız",
                         "daha çok ağaç dikmeliyiz, bu sayade karbondioksit azalır ve oksijen artar" 
                        ]
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptik')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.commnad()
async def cevre_bilinci(ctx):
    await ctx.send(random.choice(cevre_bilinci_listesi))


@bot.commnad()
async def bilresim(ctx):
    bilinc_list = os.listdir("proje1/images")
    bil = random.choice(bilinc_list)
    with open(f"proje1/images/{bil}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
     
    
bot.run(token)