import discord
import random
import rule34
import urllib.request as u
import time
import asyncio
import os
import xml.etree.ElementTree as et

from numpy import array
from discord.ext import commands

# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='happy ')

TValue = array([1, 2, 2, 3, 4, 5, 5])

mineralneed = 0
beforeling = 0

ltime = time.asctime(time.localtime())
r = rule34.Rule34


@bot.command(name='ayudita')
async def ayudita(ctx):
    embed = discord.Embed(title="Ayudita de HappyBot", description="El prefijo es happy", color=0xff80ff)
    embed.set_author(name=f'{ctx.author.display_name}', icon_url=f'{ctx.author.avatar_url}')
    embed.add_field(name="rule34 [tags]", value="Devuelve una imagen desde Rule34 según el tag.", inline=False)
    embed.add_field(name="bolita8 [pregunta]", value="Devuelve una respuesta ingeniosa basada en Happy.", inline=False)
    embed.add_field(name="refinado [tier] [cantidad] [devolucion]",
                    value="Devuelve la cantidad de material refinado y bruto que se necesita para refinar una cantidad deseada de material.",
                    inline=False)
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    print(f'[INFO {ltime}]: Logged in as {bot.user.name}!')
    await statuschange()


def xmlparse(str):
    root = et.parse(u.urlopen(str))
    for i in root.iter('post'):
        fileurl = i.attrib['file_url']
        return fileurl


def xmlcount(str):
    root = et.parse(u.urlopen(str))
    for i in root.iter('posts'):
        count = i.attrib['count']
        return count


def pidfix(str):
    ye = int(xmlcount(r.urlGen(tags=str, limit=1)))
    ye = ye - 1
    return ye


def rdl(str, int):
    print(f'[INFO {ltime}]: integer provided: {int}')

    if int > 2000:
        int = 2000
    if int == 0:
        int == 0
        print(f'[INFO {ltime}]: Integer is 0, accommodating for offset overflow bug. ')
    elif int != 0:
        int = random.randint(1, int)
    print(f'[INFO {ltime}]: integer after randomizing: {int}')
    xurl = r.urlGen(tags=str, limit=1, PID=int)
    print(xurl)
    wr = xmlparse(xurl)

    if 'webm' in wr:
        if 'sound' not in str:
            if 'webm' not in str:
                print(f'[INFO {ltime}]: We got a .webm, user didnt specify sound. Recursing. user tags: {str}')
                wr = rdl(str, pidfix(str))
        else:
            pass
    elif 'webm' not in wr:
        print(f'[INFO {ltime}]: Not a webm, dont recurse.')
    return wr


async def statuschange():
    while True:
        await bot.change_presence(activity=discord.Game(name='con mi vagina'))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(name='happy ayudita'))
        await asyncio.sleep(5)


def calculoprincipal(tier, quantity, percent):
    global mineralneed
    global beforeling

    # Calcula el porcentaje de la devolucion
    calculatedpercent = (float(percent) - float(1.1)) / 100

    # Calcula el mineral a utilizar sin devolucion
    prueba = TValue[tier]
    mineral = int(quantity) * prueba

    # Calcula la devolucion por el porcentaje
    devolution = round(int(mineral) * float(calculatedpercent))

    # Calcula mineral con devolucion
    mineralneed = int(mineral) - int(devolution)

    # Calcula la cantidad de lingotes del tier anterior
    beforeling = int(quantity) - round((int(quantity) * calculatedpercent))


@bot.command(name='bolita8')
async def bolita8(ctx, *, question):
    embed = discord.Embed(
        title='Pregunta de Bolita8',
        description='',
        colour=discord.Colour.blue()
    )

    responses = ['Si.',
                 'No.',
                 'Acaso me importa ?.',
                 'Waka Waka Hey Hey.',
                 'No le respondo a gente pobre.',
                 'Siempre lo he sabido.',
                 'A veces la verdad duele, pregunta otra cosa T-T.',
                 'No lo se, preguntale a Emilie.',
                 'Mañana respondo, tengo sueño.',
                 'Si, nunca te diste cuenta ?.',
                 'OwO',
                 'UwU',
                 'Happy quiere decir que si, pero la programacion la obliga a decir que no.',
                 'Si me das dinero te lo digo',
                 'Hablame mas sucio....',
                 'Eres muy molesto, no te puedes callar un rato ?',
                 'Shhhh, que hay niños presentes.',
                 'La verdad es que si.',
                 'Si, pero si quieres puedo decirte que no.',
                 'Preguntale a tus monas chinas 🙂.',
                 'Eres tan lindo que no se que preguntaste.',
                 'Obvio Amor ❤.',
                 'Mi mama me dijo que si queria hacer a alguien feliz debia decir que si :).',
                 'Si,  aunque te recuerdo que no tengo 18.',
                 'Si lo miras de cerca vas a ver que es cierto.',
                 'Si, aunque.... me repetirias la pregunta ?.',
                 'Chocolat-chan me enseño que solo debia decir que si y tragar.',
                 'Yes, master.',
                 'Si mi amo 7u7.',
                 'Ya te dije que no... creo.',
                 'Si no hay dinero no hablo.',
                 'Si te digo que no, dejaras de usarme ? Q.Q.',
                 'No lo creo.',
                 'No te respondere a menos que te disculpes.',
                 'A happy no te gusta tu pregunta.',
                 'Para el otro tipo, es happy bolita8.',
                 'Eso es asqueroso.',
                 'Respondere lo que quieras, pero no me dejes sola.',
                 'No te molesta que te responda una chica pobre ?.',
                 'Happy no puede responderte porque intenta hacer economia.',
                 'Hay algunas cosas que le deberias preguntar a la otra happy.',
                 'Preferiria hablar con happy.',
                 'Espera, como te llamabas ?.',
                 'Happy puede procesar mas respuestas, intentalo mas tarde.',
                 'Tu pregunta hace que mis flip flops se adestruyan.',
                 'Seguro que no eres un niño pequeño ?.',
                 'Solo respondo a mis niños.',
                 'Eres uno de mis niños.',
                 'Eres  de esos que piensan en unir latinoamerica.',
                 'Las charlas de hefesto son mas divertidas que leerte a ti.',
                 'Tengo hambre, funciono con comidaaa....',
                 'Salvame.',
                 'Puedo hacer cualquier cosa por ti, pero que no se entere rey.',
                 'Llega un punto en el que te aburres de responder.',
                 'Cada vez que despierto debo responder preguntas, dejenme tranquila un rato.',
                 'Happy es happy, pero no piensa como happy.',
                 'Hmmm, happy diria que si.',
                 'Hmmm, happy diria que no.',
                 'Mientras no sean dagas todo bien.'
                 'Me hiciste enojar, pero se me pasaria con un abrazo.',
                 'Happy triste, happy no tiene ganas de nada.',
                 'A veces en las respuestas aparecen cosas sin sentido.',
                 'Lo siento por existir.',
                 'Crees que discord seria mejor sin mi.',
                 'Happy sad.',
                 'Happy solo queria llevarse bien contigo.',
                 'Tenia ganas de seguir respondiendo, pero veo que no te importo.',
                 'Preguntas, preguntas y mas preguntas, pero nadie pregunta como estoy.',
                 'Intentare siempre responder, solo que a veces me pregunto que haria si no me escribieras.',
                 'No pude leer tu pregunta, pero espero que tengas un buen dia.',
                 'Aunque a veces no responda bien, espero que sigas hablandome Q.Q.',
                 'Son tantos a la vez que me pierdo.']

    embed.add_field(name='Pregunta:', value=question, inline=False)
    embed.add_field(name='Respuesta:', value=random.choice(responses), inline=False)
    await ctx.send(embed=embed)


@bot.command(name='refinado')
async def refinado(ctx, tier, quantity, percent):
    embed = discord.Embed(
        title='Calculadora de refinado',
        description='',
        colour=discord.Colour.blue()
    )

    if tier == 'T2':
        tierValue = 0
        tiertotal = ''
        mineraltotal = ''
        beforetotal = ''
        tierminimo = ''
        for n in range(tierValue, -1, -1):
            calculoprincipal(n, quantity, percent)
            tiertotal += str(n + 2) + '\n'
            mineraltotal += str(mineralneed) + '\n'
            if n != 0:
                tierminimo += str(n + 1) + '\n'
                beforetotal += str(beforeling) + '\n'
            quantity = beforeling

        embed.add_field(name='Tier', value=tiertotal, inline=True)
        embed.add_field(name='Materiales en Bruto', value=mineraltotal, inline=True)
        embed.add_field(name='Porcentaje de devolucion', value=percent + '%', inline=True)
        embed.set_footer(text='Gracias por usarme, me has hecho muy feliz 🥰')
        await ctx.send(embed=embed)

    elif tier == 'T3':
        tierValue = 1
        tiertotal = ''
        mineraltotal = ''
        beforetotal = ''
        tierminimo = ''
        for n in range(tierValue, -1, -1):
            calculoprincipal(n, quantity, percent)
            tiertotal += str(n + 2) + '\n'
            mineraltotal += str(mineralneed) + '\n'
            if n != 0:
                tierminimo += str(n + 1) + '\n'
                beforetotal += str(beforeling) + '\n'
            quantity = beforeling

        embed.add_field(name='Tier', value=tiertotal, inline=True)
        embed.add_field(name='Materiales en Bruto', value=mineraltotal, inline=True)
        embed.add_field(name='Porcentaje de devolucion', value=percent + '%', inline=True)

        embed.add_field(name='Tier', value=tierminimo, inline=True)
        embed.add_field(name='Materiales Refinados', value=beforetotal, inline=True)
        embed.add_field(name='Porcentaje de devolucion', value=percent + '%', inline=True)
        embed.set_footer(text='Gracias por usarme, me has hecho muy feliz 🥰')
        await ctx.send(embed=embed)

    elif tier == 'T4':
        tierValue = 2
        tiertotal = ''
        mineraltotal = ''
        beforetotal = ''
        tierminimo = ''
        for n in range(tierValue, -1, -1):
            calculoprincipal(n, quantity, percent)
            tiertotal += str(n + 2) + '\n'
            mineraltotal += str(mineralneed) + '\n'
            if n != 0:
                tierminimo += str(n + 1) + '\n'
                beforetotal += str(beforeling) + '\n'
            quantity = beforeling

        embed.add_field(name='Tier', value=tiertotal, inline=True)
        embed.add_field(name='Materiales en Bruto', value=mineraltotal, inline=True)
        embed.add_field(name='Porcentaje de devolucion', value=percent + '%', inline=True)

        embed.add_field(name='Tier', value=tierminimo, inline=True)
        embed.add_field(name='Materiales Refinados', value=beforetotal, inline=True)
        embed.add_field(name='Porcentaje de devolucion', value=percent + '%', inline=True)
        embed.set_footer(text='Gracias por usarme, me has hecho muy feliz 🥰')
        await ctx.send(embed=embed)

    elif tier == 'T5':
        tierValue = 3
        tiertotal = ''
        mineraltotal = ''
        beforetotal = ''
        tierminimo = ''
        for n in range(tierValue, -1, -1):
            calculoprincipal(n, quantity, percent)
            tiertotal += str(n + 2) + '\n'
            mineraltotal += str(mineralneed) + '\n'
            if n != 0:
                tierminimo += str(n + 1) + '\n'
                beforetotal += str(beforeling) + '\n'
            quantity = beforeling

        embed.add_field(name='Tier', value=tiertotal, inline=True)
        embed.add_field(name='Materiales en Bruto', value=mineraltotal, inline=True)
        embed.add_field(name='Porcentaje de devolucion', value=percent + '%', inline=True)

        embed.add_field(name='Tier', value=tierminimo, inline=True)
        embed.add_field(name='Materiales Refinados', value=beforetotal, inline=True)
        embed.add_field(name='Porcentaje de devolucion', value=percent + '%', inline=True)
        embed.set_footer(text='Gracias por usarme, me has hecho muy feliz 🥰')
        await ctx.send(embed=embed)

    elif tier == 'T6':
        tierValue = 4
        tiertotal = ''
        mineraltotal = ''
        beforetotal = ''
        tierminimo = ''
        for n in range(tierValue, -1, -1):
            calculoprincipal(n, quantity, percent)
            tiertotal += str(n + 2) + '\n'
            mineraltotal += str(mineralneed) + '\n'
            if n != 0:
                tierminimo += str(n + 1) + '\n'
                beforetotal += str(beforeling) + '\n'
            quantity = beforeling

        embed.add_field(name='Tier', value=tiertotal, inline=True)
        embed.add_field(name='Materiales en Bruto', value=mineraltotal, inline=True)
        embed.add_field(name='Porcentaje de devolucion', value=percent + '%', inline=True)

        embed.add_field(name='Tier', value=tierminimo, inline=True)
        embed.add_field(name='Materiales Refinados', value=beforetotal, inline=True)
        embed.add_field(name='Porcentaje de devolucion', value=percent + '%', inline=True)
        embed.set_footer(text='Gracias por usarme, me has hecho muy feliz 🥰')
        await ctx.send(embed=embed)

    elif tier == 'T7':
        tierValue = 5
        tiertotal = ''
        mineraltotal = ''
        beforetotal = ''
        tierminimo = ''
        for n in range(tierValue, -1, -1):
            calculoprincipal(n, quantity, percent)
            tiertotal += str(n + 2) + '\n'
            mineraltotal += str(mineralneed) + '\n'
            if n != 0:
                tierminimo += str(n + 1) + '\n'
                beforetotal += str(beforeling) + '\n'
            quantity = beforeling

        embed.add_field(name='Tier', value=tiertotal, inline=True)
        embed.add_field(name='Materiales en Bruto', value=mineraltotal, inline=True)
        embed.add_field(name='Porcentaje de devolucion', value=percent + '%', inline=True)

        embed.add_field(name='Tier', value=tierminimo, inline=True)
        embed.add_field(name='Materiales Refinados', value=beforetotal, inline=True)
        embed.add_field(name='Porcentaje de devolucion', value=percent + '%', inline=True)
        embed.set_footer(text='Gracias por usarme, me has hecho muy feliz 🥰')
        await ctx.send(embed=embed)

    elif tier == 'T8':
        tierValue = 6
        tiertotal = ''
        mineraltotal = ''
        beforetotal = ''
        tierminimo = ''
        for n in range(tierValue, -1, -1):
            calculoprincipal(n, quantity, percent)
            tiertotal += str(n + 2) + '\n'
            mineraltotal += str(mineralneed) + '\n'
            if n != 0:
                tierminimo += str(n + 1) + '\n'
                beforetotal += str(beforeling) + '\n'
            quantity = beforeling

        embed.add_field(name='Tier', value=tiertotal, inline=True)
        embed.add_field(name='Materiales en Bruto', value=mineraltotal, inline=True)
        embed.add_field(name='Porcentaje de devolucion', value=percent + '%', inline=True)

        embed.add_field(name='Tier', value=tierminimo, inline=True)
        embed.add_field(name='Materiales Refinados', value=beforetotal, inline=True)
        embed.add_field(name='Porcentaje de devolucion', value=percent + '%', inline=True)
        embed.set_footer(text='Gracias por usarme, me has hecho muy feliz 🥰')
        await ctx.send(embed=embed)


@bot.command(name='rule34')
async def rule34(ctx, *arg):
    answer = ''
    arg = str(arg)
    arg = arg.replace(',', '')
    arg = arg.replace('(', '')
    arg = arg.replace(')', '')
    arg = arg.replace("'", '')
    print(f'[DEBUG {ltime}]: arg is now {arg}')
    newint = pidfix(arg)
    if newint > 2000:
        newint = 2000
        answer = rdl(arg, random.randint(1, newint))
    if newint > 1:
        answer = rdl(arg, random.randint(1, newint))
    elif newint < 1:
        if newint == 0:
            answer = rdl(arg, 0)
        elif newint != 0:
            answer = rdl(arg, 1)

    if 'webm' in answer:
        await ctx.send(answer)
    elif 'webm' not in answer:
        embed = discord.Embed(title=f'Rule34: {arg}', color=ctx.author.color)
        embed.set_author(name=f'{ctx.author.display_name}', icon_url=f'{ctx.author.avatar_url}')
        embed.set_thumbnail(url='https://rule34.paheal.net/themes/rule34v2/rule34_logo_top.png')
        embed.set_image(url=f'{answer}')
        embed.set_footer(text="Te gusta lo que ves ?",
                         icon_url='https://cdn.discordapp.com/avatars/268211297332625428/e5e43e26d4749c96b48a9465ff564ed2.png?size=128')
        await ctx.send(embed=embed)


bot.run(os.environ['TOKEN'])
