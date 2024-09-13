from flask import Blueprint, request, current_app
from .pvar import dict_to_pvar_string
from . import Core, Engine, Procedure, System
import time

api = Blueprint('api', __name__, url_prefix='/api')
path_to_pvar_file = r"C:\Users\chris\Desktop\overlord_variables\release_variables.pvar"


@api.route('/move-plate',methods=['POST'])
def move_plate():
    """
    Either Get from a location or Put to it
    Currently supporting HotelA, HotelB, Timepoint_collector, Ultrasonic Station, and PlateLoc
    """
    pvar_dict = request.json['kwargs']
    pvar_str = dict_to_pvar_string(pvar_dict)
    while current_app.config['pvar_lock']:
        print("waiting for pvar lock...")
        time.sleep(0.27)
    current_app.config['pvar_lock'] = True
    with open(path_to_pvar_file,'w') as f:
        f.write(pvar_str)
    Core.Commands.RuntimeInitialize()
    engine = Engine()
    try:
        proc_info = System.IO.FileInfo(r"C:\Program Files (x86)\PAA\Overlord3\Procedures\Testing\PMAN_Move.ovp")
    except:
        raise FileNotFoundError("Can't find the PMAN_Move ovp!")
    procedure = Procedure(proc_info)
    engine.ProcedureComplete += engine_procedure_complete
    engine.Start(procedure)
    current_app.config['pvar_lock'] = False
    return "Sequence ended!"

@api.route('seal-plate',methods=['POST'])
def seal_plate():
    """ This seals whatever plate is on PlateLoc """
    Core.Commands.RuntimeInitialize()
    engine = Engine()
    try:
        proc_info = System.IO.FileInfo(r"C:\Program Files (x86)\PAA\Overlord3\Procedures\Testing\PlateSealer_execute.ovp")
    except:
        raise FileNotFoundError("Can't find the PlateLoc ovp!")
    procedure = Procedure(proc_info)
    engine.ProcedureComplete += engine_procedure_complete
    engine.Start(procedure)
    return "Sequence started!"

def engine_procedure_complete(sender, e):
    print("Run completed")
