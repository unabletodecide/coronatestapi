import requests
import json
from covapp import settings
from django.core.exceptions import ObjectDoesNotExist
from urllib.parse import urlencode

class CoronaAPI:
    def __init__(self):
        access_url = ""
        try:
            covid_api_ip = settings.COVID_API_IP
        except:
            print("COVID_API_IP is not defined.")
            covid_api_ip = ""
        if not(covid_api_ip.startswith('http://') or covid_api_ip.startswith('https://')):
            self.access_url = 'http://'+covid_api_ip
        else:
            self.access_url=covid_api_ip
    
    def getCovidData(self, country_code, timeline):
        if self.access_url == "":
            resp = HttpResponse("Unassigned COVID API IP in settings.", status=503)
            return [json.dumps(resp.content()), resp.status()]
        params = {'include': timeline}
        qstr = urlencode(params)
        try:
            final_url = self.access_url+'/countries/'+country_code+'?'+qstr
            print("Final URL is "+final_url)
            r = requests.get(final_url, timeout=5)
        except:
            raise
        return [json.loads(r.text), r.status_code]