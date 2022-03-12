"""
This Server will serve as master server for all projects.
It will call project specific sctipts from scripts folder based on project requirement and name recived in request json.
"""

from flask import Flask
from waitress import serve
from jproperties import Properties
from flask import request

app = Flask('__main__')

version = '1.0.0'
config_dic = {}

@app.route('/version', methods = ['Get'])
def project_version():
    return f'App is running with version {version}'

def read_config():
    """
    this method will read required configuration informations from config/config.properties file.
    """
    global config_dic
    configs = Properties()
    with open('config/config.properties', 'rb') as config_file:
        configs.load(config_file)
    items_view = configs.items()
    for item in items_view:
        config_dic[item[0]] = item[1].data

@app.route('/exercise',methods=['post'])
def execute_exercise():
    """
    this method is used to perform requested excersice.
    Request:
    {
        "scriptName": "excersice1",
        "url": "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.GBP.EUR.SP00.A?detail=dataonly"
    }

    Return:
    {
        "requiredDF": ''
    }
    """
    data_values = call_method(request.json['scriptName'], 'exchange_rate', request.json)
    response = {'return_code': 0, 'message': 'Success', 'data': data_values}
    return response

def call_method(script, name, request_json):
    """
    This method is responsible to call method of a script dynamically

    :param script: Name of the script to load
    :param name: Name of the method to call
    :param request_json: Json accepted from request
    :return: response_dict
    """
    
    response_dict = {}

    pkg = __import__('scripts', fromlist=[script])
    mod = getattr(pkg, script)
    getattr(mod, 'init')(config_dic)
    response_dict = getattr(mod, name)(request_json)
    
    return response_dict

if __name__ == '__main__':
    read_config()
    app.run(debug=False,host=config_dic['host'],port = config_dic['port'])
