import discord
from discord.ext import commands
from discord.commands import slash_command,permissions
from dotenv import load_dotenv
import os

import utils

load_dotenv()

TOKEN = os.getenv("OTUwMDQzMTUyODc2NzExOTk5.YiTKog.rsGLU2QWttkdJ-t8oxDN_1Bg8n0")
PREFIX = os.getenv("$")
GUILD_IDS = [963801997407047690]

# Intents
intents = discord.Intents.all()

bot = commands.Bot(PREFIX, intents = intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"https://discord.gg/fngeKk3cG7"))
    print(discord.__version__)
    guild = bot.get_guild(949056400359821362)
    # print(guild.roles)

# <Role id=963805295610564608 name='SwishBot tillgång'>

@bot.slash_command(
    name = "sw1shb0t" , 
    usage="/swish" , 
    description = "Command for making payment" ,
    guild_ids=GUILD_IDS ,
    default_permission = False
)
@permissions.has_role("SwishBot tillgång")
async def swish(ctx:discord.ApplicationContext , namn: str, nummer: str , belopp: str):
    interaction = await ctx.respond(f"Skapar betalning från {ctx.author.mention} Till {namn}. Belopp: {belopp} .....")
    msg = await interaction.original_message()
    payment = utils.Payment(namn,nummer,belopp,msg.created_at,msg.id)

    await msg.channel.send(file = discord.File(fp=payment.mp4))

    payment.close()



if __name__ == "__main__":
    bot.run(TOKEN)

