import requests
import json


def request_get(url):
    '''Esta función recibe como parámetro la url de una api y entrega un
    objeto JSON con los datos'''
    return json.loads(requests.get(url).text) 


def html_card(photos):
    '''Esta función crea cards con los datos obtenidos del objeto JSON. Recibe el parámetro photos, que es 
    el objeto JSON creado de la función request_get(url) ejecutada en main. Luego, se crea un string 
    vacio para ser llenado con las card, a las cuales se les interpolado las imágenes y nombres obtenidos al 
    iterar el diccionario photos (el objeto JSON). Por cada iteración, interpola datos a la plantilla card y se
    suma a la variable card'''
    card = ''
    for photo in photos:
        card += f'''<div class="col-3">
                        <div class="card mt-3" style="width: 12rem;">
                            <img src="{photo['images']['thumb']}" class="card-img-top" alt="{photo['name']['english']}">
                            <div class="card-body">
                                <h5 class="card-title">{photo['name']['spanish']}</h5>
                            </div>
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item"><strong>En ingles:</strong><em> {photo['name']['english']}</em></li>
                                <li class="list-group-item"><strong>En latínñ:</strong><em> {photo['name']['latin']}</em></li>
                            </ul>
                            <div class="card-body">
                                <a href="{photo['images']['full']}" class="card-link">Ver en grande</a>
                            </div>
                        </div>
                    </div>'''
    return card


def crear_html(card):
    '''Esta fución crea un archivo index.html con las cards. Se recibe el parámetro card, el cual contiene
    todas las card anteriomente creadas por la función html_card(photos). Interpola la varible card una plantilla
    html y luego crea un archivo index.html con el template ya modificado'''
    template = f'''<!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Aves Chile</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        <body>
            <div class="container">
                <h1>Aves Chile</h1>
                <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Enim aspernatur perspiciatis cumque aliquam alias perferendis voluptates. Sunt fuga inventore, nesciunt dolor sapiente, ab dignissimos voluptas unde eligendi asperiores, ad animi!</p>
                <div class="row">
                    {card}
                </div>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </body>
    </html>'''
    with open('index.html', 'w') as f:
        return f.write(template)
