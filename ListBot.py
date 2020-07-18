import os
import time
import IPOScraper as api
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

class ListBot(discord.Client):
    async def on_ready(self):
        await client.change_presence(status=discord.Status.online, activity=discord.Game("the 30/30 rule"))

    async def on_message(self, message: discord.message.Message):
        if message.author.id != client.user.id: # prevent recursive calling
            msg = message.content.split()
            if msg[0] == "!ipocal":
                embed = api.get_ipos_nasdank()
                await message.channel.send(embed=embed)

client = ListBot()
client.run(TOKEN)