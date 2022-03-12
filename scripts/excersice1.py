
from sys import exc_info
from flask import request
import json
import requestes
def init(configs):
    global configs_dict
    configs_dict = configs

def exchange_rate(request_json):
    print(request_json)
    try:
        print(1)
        response = requests.get(request_json['url'])
        data = json.loads(response.text)
        print(data)
    except Exception as exe:
        a,b,c =exc_info()
        print('error in line no::',c.tb_lineno)
    return 'executed'