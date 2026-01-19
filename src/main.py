import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class Shimi(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=["sm ", "sm"],
            intents=discord.Intents.all(),
            status=discord.Status.idle,
            activity=discord.CustomActivity(name="prefix: sm")
        )

    async def setup_hook(self):
        await self.load_extension("cogs.music")
        print("Music Cog Loaded!")

bot = Shimi()

@bot.event
async def on_ready():
    assert bot.user is not None
    print(f"Logged in as {bot.user.display_name} (ID: {bot.user.id})")

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    await bot.process_commands(message)

@bot.command()
async def ping(ctx: commands.Context):
    """Get the bot's latency"""
    await ctx.reply(f"pong {bot.latency * 1000:.2f}ms")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx: commands.Context, amount: int = 1):
    """Deletes messages."""
    if isinstance(ctx.channel, discord.TextChannel):
        await ctx.channel.purge(limit=amount + 1)
    else:
        await ctx.send("failed", delete_after=3)
        return
    await ctx.send(f"Cleared {amount} messages.", delete_after=3)

@bot.command()
async def userinfo(ctx: commands.Context, target: discord.Member | None = None):
    """Shows user information."""
    user = target or ctx.author
    
    embed = discord.Embed(title=f"User Info - {user.name}", color=discord.Color.blue())
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.add_field(name="ID", value=user.id)
    embed.add_field(name="Joined Discord", value=user.created_at.strftime("%Y-%m-%d"))
    
    await ctx.send(embed=embed)

token = os.getenv('TOKEN')
if not token:
    raise ValueError("TOKEN not found in .env file")

bot.run(token)
