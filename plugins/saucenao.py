import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
API_KEY = config['DEFAULT']['SAUCENAO_API']

def getSauce(image):
    url = 'https://saucenao.com/search.php?db=999&output_type=2&testmode=1&numres=16&api_key=' + API_KEY + '&url=' + image
    response = requests.get(url)
    data = response.json()

    if data['header']['status'] != 0 or 'anidb_aid' not in data['results'][0]['data']:
        return None

    return data['results'][0]['data']

