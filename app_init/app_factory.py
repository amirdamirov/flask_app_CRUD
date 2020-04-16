from flask import Flask
import os
from db_setup.db_conf import db

settings = {
     "dev" : "settings.devsettings.DevelopSettings",
     "prod" : "settings.prodsettings.PrdSettings"
           
           }

def get_settings(settings_name):
    if settings.get(settings_name):
        return settings.get(settings_name)

    raise Exception("Bele %s settings yoxdu sihtir" % settings_name)

def create_app(settings_name):
    app = Flask(__name__)
    settings_obj = get_settings(settings_name)
    app.config.from_object(settings_obj)
    db.init_app(app) 

    with app.app_context():
        db.create_all()
    
    return app