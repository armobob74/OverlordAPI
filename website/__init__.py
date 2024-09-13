import sys
from flask import Flask
import clr  # doesn't work on Linux
import os
from .views import views
from flask_cors import CORS


# Configure paths to DLLs
path_to_overlord = r"C:\Program Files (x86)\PAA\Overlord3"
sys.path.append(path_to_overlord)
clr.AddReference('Overlord.FlowRunEngine')
clr.AddReference('Overlord.Model')
clr.AddReference('Overlord.Utilities')
clr.AddReference('System')
# Once paths are configured, we import the Overlord namespaces
from Overlord.FlowRunEngine import Engine
from Overlord.Model import Procedure
from Overlord.Utilities import Core
import System

path_to_sequence = r"C:\Path\To\sequence.ovp"
path_to_pvar_file = r"C:\Path\To\variables.pvar" # this is a very simple file in PVAR format

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(views)
    from .api import api
    app.register_blueprint(api)
    app.config['pvar_lock'] = False
    return app
