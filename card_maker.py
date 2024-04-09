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
