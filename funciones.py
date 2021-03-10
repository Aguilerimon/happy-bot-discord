import urllib.request as u
import xml.etree.ElementTree as et
import random
import rule34
import time

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
    r = rule34.Rule34

    # Se vuelve a realizar una busqueda de un numero aleatorio para garantizar el funcionamiento de la recursividad
    # si es necesaria
    newint = random.randint(1, randomint)

    # Se genera una nueva URL, ahora añadiendo el numero generado como valor del argumento PID
    url = r.urlGen(tags=tag, limit=1, PID=newint)

    # Se obtiene el enlace de la imagen o el webm del XML generado mediante la funcion xmlfile
    response = xmlfile(url)

    # Evaluamos si en el enlace existe la palabra clave webm
    if 'webm' in response:

        # Evaluamos si existe la palabra clave sound en el tag de busqueda original
        if 'sound' not in tag:

            # Evaluamos si existe la palabra clave webm en el tag de busqueda original
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
    elif 'webm' not in response:
        print(f'[INFO {ltime}]: El resultado de la búsqueda es de tipo imagen')

    return response