import requests

def validate(url):
    try:
        requests.get(url)
        return True
    except:
        return False

