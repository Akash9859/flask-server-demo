"""
This Server will serve as master server for all projects.
It will call project specific sctipts from scripts folder based on project requirement and name recived in request json.
"""

from flask import Flask, jsonify
from waitress import serve
from jproperties import Properties
from flask import request
from sys import exc_info
from Logger import LogConfig
from Logger import Log
import traceback

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
    data_values['data'] is html of requested dataframe.
    {
        {'return_code': 0,
        'message': 'Successful operation', 
        'data': data_values['data']}
    }
    """
    brix_logger = Log.Log.get_logger()
    try:
        data_values = call_method(request.json['scriptName'], 'exchange_rate', request.json)
        brix_logger.info("Response JSON:: " + str(data_values))
        if data_values['code']==0:
            response = {'return_code': 0,
                'message': 'Successful operation', 
                'data': data_values['data']}
        else:
            response = {'return_code': 1,
                'message': 'Execution of exercise 1 failed', 
                'data': data_values['data']}
        return jsonify(response)
    except Exception as exe:
        a,b,c =exc_info()
        print('error in line no::',str(c.tb_lineno))
        print(a)
        print(b)
        brix_logger.error("Script Name: ImporterConverterServer :: " + str(exe.args))
        brix_logger.error(traceback.format_exc())
        return_json = {
            'return_code': 1,
            'message': 'server failed',
            'data': str(c.tb_lineno)
        }
        return jsonify(return_json)

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
    LogConfig.LogConfig(config_dic).configure_log()
    app.run(debug=False,host=config_dic['host'],port = config_dic['port'])
