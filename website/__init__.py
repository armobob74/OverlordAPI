import sys
from flask import Flask
import clr  # doesn't work on Linux
from .views import views
from .api import api

# Configure paths to DLLs
sys.path.append(r"C:\Program Files\Overlord3")
clr.AddReference('Overlord.FlowRunEngine')
clr.AddReference('Overlord.Model')
clr.AddReference('Overlord.Utilities')
# Once paths are configured, we import the Overlord namespaces
from Overlord.FlowRunEngine import Engine, Procedure
from Overlord.Utilities import Core

path_to_sequence = r"C:\Path\To\sequence.ovp"
path_to_pvar_file = r"C:\Path\To\variables.pvar" # this is a very simple file in PVAR format

def create_app():
    app = Flask(__name__)
    app.register_blueprint(views)
    app.register_blueprint(api)
