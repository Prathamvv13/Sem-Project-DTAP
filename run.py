# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from flask import Flask,request
import os
from   flask_migrate import Migrate
from   flask_minify  import Minify
from   sys import exit

# import win32api
import os


from apps.config import config_dict
from apps import create_app, db

# application = Flask(__name__)

# @application.route("/present")
# def present():
#     import sys

# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')
app = create_app(app_config)
Migrate(app, db)

if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)
    
if DEBUG:
    app.logger.info('DEBUG            = ' + str(DEBUG)             )
    app.logger.info('Page Compression = ' + 'FALSE' if DEBUG else 'TRUE' )
    app.logger.info('DBMS             = ' + app_config.SQLALCHEMY_DATABASE_URI)
    app.logger.info('ASSETS_ROOT      = ' + app_config.ASSETS_ROOT )

app.config['UPLOAD_FOLDER'] = 'C:\\Users\\HCN\\Desktop\\Uploads'
# app.config['UPLOAD_FOLDER'] = 'C:'
# C:\Users\HCN\Desktop\Uploads
@app.route('/upload' , methods = ['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        f.save(file_path)
        print("File Path:", file_path)
        # application = r"C:\Program Files\Microsoft Office\root\OfficeXX\POWERPNT.EXE"
        # win32api.ShellExecute(0, "open", application, file_path, "", 1)
        # f.save(f.filename)
        print("post")
        # name = request.form['spoken']
        # print(name)
    # return render_template('index.    html')
    return "success"

@app.route('/voiceip' , methods = ['POST'])
def voiceip():
    print('Request received!')
    data = request.get_json()
    spoken_text = data['spoken']
    # spoken_text = request.form['spoken']
    print(spoken_text) 
    return spoken_text   
if __name__ == "__main__":
    app.run()
