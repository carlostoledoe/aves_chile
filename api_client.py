import requests
import json


def request_get(url):
    '''Esta función recibe como parámetro la url de una api y entrega un
    objeto JSON con los datos'''
    return json.loads(requests.get(url).text) 
