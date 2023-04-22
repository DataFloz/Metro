import json
import requests

from bl.transformer_runner_interface import TransforerRunnerInterface


class HttpTransformer(TransforerRunnerInterface):
    '''Inhierent from TransforerRunnerInterface: responsible for HTTP transformation.'''
    def __init__(self, http_url, headers={}, params={}):
        self.http_url = http_url
        self.headers = headers
        self.params = params

    def run_logic(self, msg):
        json_msg = json.dumps(msg)
        reponse = requests.post(self.http_url, params=self.params,json=json_msg,
                                headers=self.headers, timeout=60)
        print(f"res: {reponse.json()}")

        return reponse.json()
