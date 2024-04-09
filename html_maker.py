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
    return template