import discord
from discord.ext import commands
from typing import Optional


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def info_r34(self, ctx):
        embed = discord.Embed(description="Devuelve una imágen aleatoria de `rule34.xxx`, debes incluir un tag de "
                                          "búsqueda para obtener un resultado.", color=0xff80ff)
        embed.set_author(name=f'{"NSFW: rule34"}', icon_url=f'{self.bot.user.avatar_url}')
        embed.add_field(name="Sintaxis:", value="`happy r34 [tag]`", inline=False)
        embed.set_image(url='https://media1.tenor.com/images/c229d1dc0689096b4a5d4b74'
                            '3745e303/tenor.gif?itemid=13902070')
        await ctx.send(embed=embed)

    async def info_privr34(self, ctx):
        embed = discord.Embed(description="Envia una imágen aleatoria de `rule34.xxx` a tu chat privado, "
                                          "debes incluir un tag de "
                                          "búsqueda para obtener un resultado.", color=0xff80ff)
        embed.set_author(name=f'{"NSFW: rule34"}', icon_url=f'{self.bot.user.avatar_url}')
        embed.add_field(name="Sintaxis:", value="`happy privr34 [tag]`", inline=False)
        embed.set_image(url='https://media1.tenor.com/images/c229d1dc0689096b4a5d4b743745e30'
                            '3/tenor.gif?itemid=13902070')
        await ctx.send(embed=embed)

    async def info_bolita8(self, ctx):
        embed = discord.Embed(description="Devuelve una respuesta aleatoria.", color=0xff80ff)
        embed.set_author(name=f'{"Diversión: bolita8"}', icon_url=f'{self.bot.user.avatar_url}')
        embed.add_field(name="Sintaxis:", value="`happy bolita8 [pregunta]`", inline=False)
        embed.set_image(url='https://media1.tenor.com/images/c229d1dc0689096b4a5d4b743'
                            '745e303/tenor.gif?itemid=13902070')
        await ctx.send(embed=embed)

    async def info_limpiar(self, ctx):
        embed = discord.Embed(description="Elimina una cantidad de mensajes en un canal, "
                                          "la cantida maxima es: `100`.", color=0xff80ff)
        embed.set_author(name=f'{"Administración: limpiar"}', icon_url=f'{self.bot.user.avatar_url}')
        embed.add_field(name="Sintaxis:", value="`happy limpiar [cantidad]`", inline=False)
        embed.set_image(url='https://media1.tenor.com/images/c229d1dc0689096b4a5d4b743'
                            '745e303/tenor.gif?itemid=13902070')
        await ctx.send(embed=embed)

    @commands.command(name="limpiar")
    async def limpiar(self, ctx, arg):
        amount = 5
        try:
            amount = int(arg)
        except Exception:
            pass
        await ctx.channel.purge(limit=amount)

    @limpiar.error
    async def limpiar_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="¡Error! ¡HappyBot esta triste!", color=0xfc051c)
            embed.add_field(name="!Error en la Matrix!", value="**Debes añadir la cantidad de mensajes a eliminar... "
                                                               "idiota!.**",
                            inline=False)
            embed.add_field(name="Ejemplo de Sintaxis", value="`happy limpiar [cantidad]`", inline=False)
            embed.set_image(url='https://i.pinimg.com/originals/4f/b4/04/4fb4040f32a0686a41ace938165bfe5a.gif')
            await ctx.send(embed=embed)

    @commands.command(name='ayudita')
    async def ayudita(self, ctx, cmd: Optional[str]):
        if cmd is None:
            embed = discord.Embed(description="Hola! Me llamo **HappyBot** Esta es mi lista de comandos disponibles, "
                                              "espero que te diviertas.", color=0xff80ff)
            embed.set_author(name=f'{"Lista de comandos de HappyBot"}', icon_url=f'{self.bot.user.avatar_url}')
            embed.add_field(name="Diversión", value="`bolita8`", inline=False)

            embed.add_field(name="Administración", value="`limpiar`", inline=False)

            embed.add_field(name="NSFW", value="`r34` `privr34`", inline=False)

            embed.set_footer(text="Si requieres información detallada de algun comando: happy ayudita [comando]")
            embed.set_image(url='https://media1.tenor.com/images/203ee66b44de45f6119a9984de37b4e1/tenor.gif?itemid'
                                '=12887287')
            await ctx.send(embed=embed)
        else:
            if cmd == 'r34':
                await self.info_r34(ctx)

            elif cmd == 'privr34':
                await self.info_privr34(ctx)

            elif cmd == "bolita8":
                await self.info_bolita8(ctx)

            elif cmd == "limpiar":
                await self.info_limpiar(ctx)

            else:
                await ctx.send("❌ El comando no existe ❌")
