import discord
from discord.ext import commands
import time
import youtube_dl

ltime = time.asctime(time.localtime())


class Musica(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("No estas conectado a un canal de voz")
        else:
            waitone = await ctx.send("***:heart: Conectando al canal de voz...***")
            await ctx.author.voice.channel.connect()
            await waitone.delete()

    @commands.command()
    async def disconnect(self, ctx):
        print(f'[DEBUG {ltime}]: Desconectando del canal de voz..')
        await ctx.voice_client.disconnect()

    @commands.command()
    async def p(self, ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':
            '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}

        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("Estoy agarrando señal carnal...")

    @commands.command()
    async def resume(self, ctx):
        ctx.voice_client.resume()
        await ctx.send("Y volvemos a la normalidad")

    @commands.command()
    async def stop(self, ctx):
        ctx.voice_client.stop()
        await ctx.send("Ahorita no joven")
