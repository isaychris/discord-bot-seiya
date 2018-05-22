import configparser
import requests
from urllib.parse import quote

config = configparser.ConfigParser()
config.read('config.ini')
API_KEY = config['DEFAULT']['BING_API']

def getImage(input):
    base = 'https://api.cognitive.microsoft.com/bing/v7.0/images/search?'

    query = 'q=' + quote(input)
    count = '&count=' + '1'
    offset = '&offset=' + '0'
    key = '&subscription-key=' + API_KEY
    url = base + query + count + offset + key

    response = requests.get(url)
    data = response.json()

    return data['value'][0]['contentUrl']