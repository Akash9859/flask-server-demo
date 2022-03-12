"""
This Server will serve as master server for all projects.
It will call project specific sctipts from scripts folder based on project requirement and name recived in request json.
"""

from flask import Flask
from waitress import serve
from jproperties import Properties

app = Flask('__main__')

version = '1.0.0'
config_dic = {}

@app.route('/version', methods = ['Get'])
def project_version():
    return f'App is running with version {version}'

def read_config():
    global config_dic
    configs = Properties()
    with open('config/config.properties', 'rb') as config_file:
        configs.load(config_file)
    items_view = configs.items()
    for item in items_view:
        config_dic[item[0]] = item[1].data

if __name__ == '__main__':
    read_config()
    print(config_dic)
    app.run(debug=False,host='192.168.1.4',port=4000)
