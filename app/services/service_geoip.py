from decouple import config
from fastapi.responses import JSONResponse
import requests

class GeoipService:
    def __init__(self):
        self.config = ''

    def get_ip(self):
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]

    def get_location(self, ip_address):
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        return response