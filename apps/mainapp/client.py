import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

class ElasticClinet():
    def __init__(self, query, search_endpoint) -> None:
        self.query = query
        self.search_endpoint = search_endpoint
        self.username_elastic=str(os.getenv('ELASTIC_USERNAME')),
        self.password_elastic=str(os.getenv('ELASTIC_PASSWORD')),
        self.cert_file=str(os.getenv('ELASTIC_CERT_FILE'))
        self.url = "https://elastic:9200/"

    def getHits(self):
        try: 
            response = requests.post(self.search_endpoint, json=self.query, auth=(self.username_elastic, self.password_elastic), verify=self.cert_file)
            if response.status_code == 200:
                response_json = json.loads(response.text)
                hits = response_json.get("hits", {}).get("hits", [])
                err = None
        except requests.exceptions.RequestException as e: 
            hits = None
            err = (f"Error: {e}") 
        except Exception as e:
            hits = None
            err = (f"Unexpected error: {e}") 
    
        return hits, err