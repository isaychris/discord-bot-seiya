import configparser
import requests
from urllib.parse import quote

config = configparser.ConfigParser()
config.read('config.ini')
API_KEY = config['DEFAULT']['TRANSLATE_API']

def getTranslation(input):
    base = 'https://translation.googleapis.com/language/translate/v2?'

    query = 'q=' + quote(input)
    target = '&target=' + 'ja'
    source = '&source=' + 'en'
    key = '&key=' + API_KEY
    url = base + query + target + source + key

    response = requests.get(url)
    data = response.json()
    return data['data']['translations'][0]['translatedText']