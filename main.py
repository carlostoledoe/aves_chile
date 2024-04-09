from api_client import request_get
from card_maker import html_card
from html_maker import crear_html
from index_maker import crear_index

# Url a consultar
url =  'https://aves.ninjas.cl/api/birds'

# Se ejecuta cuatro funciones de forma anidada
crear_index(crear_html(html_card(request_get(url))))
