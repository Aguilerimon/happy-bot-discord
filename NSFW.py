import urllib.request as u
import xml.etree.ElementTree as et
import discord
import random
import rule34
import time

from discord.ext import commands
from discord import DMChannel

ltime = time.asctime(time.localtime())


def xmlfile(url):
    file = et.parse(u.urlopen(url))
    for n in file.iter('post'):
        fileurl = n.attrib['file_url']
        return fileurl


def xmlcount(url):
    file = et.parse(u.urlopen(url))
    for n in file.iter('posts'):
        filecount = n.attrib['count']
        return filecount


def randomize(tag, randomint):
    newint = 0
    r = rule34.Rule34

    # Se evalua si el argumento de entrada PID es mayor de 2000, si es mayor, la variable randomint se iguala a 2000
    # y se vuelve a buscar un numero aleatorio entre 2000 y 1
    if randomint > 2000:
        randomint = 2000
        newint = random.randint(1, randomint)

    elif randomint > 1:
        newint = random.randint(1, randomint)

    elif randomint < 1:
        if randomint == 0:
            newint = 0
        elif randomint != 0:
            newint = 1

    # Se genera una nueva URL, ahora añadiendo el numero generado como valor del argumento PID
    url = r.urlGen(tags=tag, limit=1, PID=newint)

    # Se obtiene el enlace de la imagen o el webm del XML generado mediante la funcion xmlfile
    response = xmlfile(url)

    # Evaluamos si en el enlace existe la palabra clave webm
    if 'mp4' in response:

        print(f'[INFO {ltime}]: El resultado de la búsqueda es de tipo video')

        # Evaluamos si existe la palabra clave sound en el tag de busqueda original
        if 'sound' not in tag:

            # Evaluamos si existe la palabra clave webm en el tag de busqueda original
            if 'Webm' not in tag:

                if 'webm' not in tag:
                    # Si se llega hasta aqui, quiere decir que el resultado de la busqueda es un webm sound sin que el
                    # usuario haya especificado tales tags de busqueda, por lo cual se procede a ejecutar la funcion
                    # randomize hasta que se obtenga un resultado que cumpla con las especificaciones de busqueda del
                    # usuario (Se volvera a generar un nuevo XML)
                    print(f'[INFO {ltime}]: Intento recursivo')
                    response = randomize(tag, int(xmlcount(r.urlGen(tags=tag, limit=1))))
        else:
            pass

    # Si el resultado no es un webm, quiere decir que el resultado es una imagen (jpg, png, gif)
    elif 'mp4' not in response:
        print(f'[INFO {ltime}]: El resultado de la búsqueda es de tipo imagen')

    return response


class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='privr34')
    async def privr34(self, ctx, *, arg):
        if ctx.channel.is_nsfw():
            r = rule34.Rule34

            # Obtiene el ID del usuario el cual pide la solicitud
            user = await self.bot.fetch_user(ctx.author.id)

            arg = str(arg)

            print(f'[DEBUG {ltime}]: Tags ingresados: {arg}')
            waitone = await ctx.send("***:heart: Estoy calculando tus fetiches, espera un poco.***")

            # Se genera un URL aleatoria con el generador propio de la libreria de RULE34
            url = r.urlGen(tags=arg, limit=1)
            print(f'[DEBUG {ltime}]: URL XML generado: {url}')

            # Se obtiene el valor del atributo count del XML analizado por la funcion xmlcount
            countnum = int(xmlcount(url))
            print(f'[INFO {ltime}]: Valor del count extraido del XML: {countnum}')

            if countnum != 0:
                # Se obtiene una respuesta enviando el tag de busqueda y un numero aleatorio entre 1 y el valor del
                # atributo count
                answer = randomize(arg, random.randint(1, countnum))
                print(f'[INFO {ltime}]: Enlace extraido del XML: {answer}')

                # Se envia al canal de discord el enlace webm resultante
                if 'mp4' in answer:
                    await waitone.delete()
                    await DMChannel.send(user, answer)

                # Se envia al canal de discord el enlace de la imagen mediante un embed message
                elif 'mp4' not in answer:
                    embed = discord.Embed(title=f'Rule34: {arg}', color=ctx.author.color)
                    embed.set_author(name=f'{ctx.author.display_name}', icon_url=f'{ctx.author.avatar_url}')
                    embed.set_thumbnail(url='https://rule34.paheal.net/themes/rule34v2/rule34_logo_top.png')
                    embed.set_image(url=f'{answer}')
                    embed.set_footer(text="Te gusta lo que ves ?",
                                     icon_url=f'{ctx.author.avatar_url}')
                    await waitone.delete()
                    await DMChannel.send(user, embed=embed)
            else:
                await waitone.delete()
                embed = discord.Embed(title="¡Error! ¡HappyBot esta triste!", color=0xfc051c)
                embed.add_field(name="Error en la Matrix", value="**La búsqueda no existe... aún.**",
                                inline=False)
                embed.add_field(name="Ejemplo de Sintaxis", value="`happy rule34 [Kindred]`", inline=False)
                embed.set_image(url='https://i.pinimg.com/originals/4f/b4/04/4fb4040f32a0686a41ace938165bfe5a.gif')
                await ctx.send(embed=embed)
        else:
            await ctx.send("❌ El comando solo se puede ejecutar en un canal NSFW ❌")

    @commands.command(name='r34')
    async def r34(self, ctx, *, arg):
        if ctx.channel.is_nsfw():
            r = rule34.Rule34

            arg = str(arg)

            print(f'[DEBUG {ltime}]: Tags ingresados: {arg}')
            waitone = await ctx.send("***:heart: Estoy calculando tus fetiches, espera un poco.***")

            # Se genera un URL aleatoria con el generador propio de la libreria de RULE34
            url = r.urlGen(tags=arg, limit=1)
            print(f'[DEBUG {ltime}]: URL XML generado: {url}')

            # Se obtiene el valor del atributo count del XML analizado por la funcion xmlcount
            countnum = int(xmlcount(url))
            print(f'[INFO {ltime}]: Valor del count extraido del XML: {countnum}')

            if countnum != 0:
                # Se obtiene una respuesta enviando el tag de busqueda y un numero aleatorio entre 1 y el valor del
                # atributo count
                answer = randomize(arg, random.randint(1, countnum))
                print(f'[INFO {ltime}]: Enlace extraido del XML: {answer}')

                # Se envia al canal de discord el enlace webm resultante
                if 'mp4' in answer:
                    await waitone.delete()
                    await ctx.send(answer)

                # Se envia al canal de discord el enlace de la imagen mediante un embed message
                elif 'mp4' not in answer:
                    embed = discord.Embed(title=f'Rule34: {arg}', color=ctx.author.color)
                    embed.set_author(name=f'{ctx.author.display_name}', icon_url=f'{ctx.author.avatar_url}')
                    embed.set_thumbnail(url='https://rule34.paheal.net/themes/rule34v2/rule34_logo_top.png')
                    embed.set_image(url=f'{answer}')
                    embed.set_footer(text="Te gusta lo que ves ?",
                                     icon_url=f'{ctx.author.avatar_url}')
                    await waitone.delete()
                    await ctx.send(embed=embed)
            else:
                await waitone.delete()
                embed = discord.Embed(title="¡Error! ¡HappyBot esta triste!", color=0xfc051c)
                embed.add_field(name="Error en la Matrix", value="**La búsqueda no existe... aún.**",
                                inline=False)
                embed.add_field(name="Ejemplo de Sintaxis", value="`happy rule34 [Kindred]`", inline=False)
                embed.set_image(url='https://i.pinimg.com/originals/4f/b4/04/4fb4040f32a0686a41ace938165bfe5a.gif')
                await ctx.send(embed=embed)
        else:
            await ctx.send("❌ El comando solo se puede ejecutar en un canal NSFW ❌")

    @r34.error
    async def r34_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="¡Error! ¡HappyBot esta triste!", color=0xfc051c)
            embed.add_field(name="!Error en la Matrix!", value="**Debes añadir una búsqueda... idiota!.**",
                            inline=False)
            embed.add_field(name="Ejemplo de Sintaxis", value="`happy rule34 [Kindred]`", inline=False)
            embed.set_image(url='https://i.pinimg.com/originals/4f/b4/04/4fb4040f32a0686a41ace938165bfe5a.gif')
            await ctx.send(embed=embed)

    @privr34.error
    async def privr34_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="¡Error! ¡HappyBot esta triste!", color=0xfc051c)
            embed.add_field(name="!Error en la Matrix!", value="**Debes añadir una búsqueda... idiota!.**",
                            inline=False)
            embed.add_field(name="Ejemplo de Sintaxis", value="`happy rule34 [Kindred]`", inline=False)
            embed.set_image(url='https://i.pinimg.com/originals/4f/b4/04/4fb4040f32a0686a41ace938165bfe5a.gif')
            await ctx.send(embed=embed)
