import discord
import random

from discord.ext import commands


class Bolita(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bolita8')
    async def bolita8(self, ctx, *, question):
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

        embed.add_field(name=ctx.author.display_name + ' Pregunta:', value=question, inline=False)
        embed.add_field(name='Respuesta:', value=random.choice(responses), inline=False)
        await ctx.send(embed=embed)

    @bolita8.error
    async def bolita8_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="¡Error! ¡HappyBot esta triste!", color=0xfc051c)
            embed.add_field(name="!Error en la Matrix!", value="**Debes realizar una pregunta... Idiota!**",
                            inline=False)
            embed.add_field(name="Ejemplo de Sintaxis", value="`happy bolita8 [pregunta]`", inline=False)
            embed.set_image(url='https://i.pinimg.com/originals/4f/b4/04/4fb4040f32a0686a41ace938165bfe5a.gif')
            await ctx.send(embed=embed)
