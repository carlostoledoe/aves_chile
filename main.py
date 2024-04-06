from module import request_get, html_card, crear_html

# Url a consultar
url =  'https://aves.ninjas.cl/api/birds'

crear_html(html_card(request_get(url)))