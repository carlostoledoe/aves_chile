'''
La aplicación crea un index.html con varias aves presentadas en card.
--------------------------------------------------------------------
request_get(url)    : Crea un objeto JSON llamado photos con todas las aves de la API
html_card()         : Toma el objeto photos y crea diferentes cards adjuntándolas en una variable card
crear_html ()       : Toma las cards creadas y las interpola en una plantilla html y crea un archivo index.html  
'''

from module import request_get, html_card, crear_html

# Url a consultar
url =  'https://aves.ninjas.cl/api/birds'

crear_html(html_card(request_get(url)))