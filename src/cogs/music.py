import discord
from discord.ext import commands
import yt_dlp

class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx: commands.Context):
        """Joins the user's voice channel"""
        if isinstance(ctx.author, discord.Member) and ctx.author.voice:
            channel = ctx.author.voice.channel
            if isinstance(channel, discord.VoiceChannel):
                await channel.connect()
        else:
            await ctx.send("You need to be in a voice channel")

    @commands.command()
    async def leave(self, ctx: commands.Context):
        """Leaves the voice channel"""
        if ctx.voice_client:
            await ctx.voice_client.disconnect(force=False)
        else:
            await ctx.send("Not in a voice channel")

async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))
