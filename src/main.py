import os
from aiohttp.helpers import TOKEN
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix=["sm ", "sm"], intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"logged in as {bot.user.display_name} (ID: {bot.user.id})")

@bot.command()
async def hello(ctx):
    await ctx.send("hellow")

@bot.command()
async def ping(ctx):
    """replies with pong"""
    await ctx.reply("pong")

bot.run(os.getenv('TOKEN'))
