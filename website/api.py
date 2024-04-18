from flask import Blueprint, request
from .pvar import dict_to_pvar_string
from . import Core, Engine, Procedure, System

api = Blueprint('api', __name__, url_prefix='/api')
path_to_pvar_file = r"C:\Users\chris\Desktop\overlord_variables\release_variables.pvar"
@api.route('/run-sequence',methods=['POST'])
def run_sequence():
    pvar_dict = request.json['kwargs']
    pvar_str = dict_to_pvar_string(pvar_dict)
    with open(path_to_pvar_file,'w') as f:
        f.write(pvar_str)
    Core.Commands.RuntimeInitialize()
    engine = Engine()
    try:
        proc_info = System.IO.FileInfo(r"C:\Program Files (x86)\PAA\Overlord3\Procedures\Testing\PMAN_Move.ovp")
    except:
        raise FileNotFoundError("Can't find the ovp!")
    procedure = Procedure(proc_info)
    engine.ProcedureComplete += engine_procedure_complete
    engine.Start(procedure)
    return "Sequence started!"

def engine_procedure_complete(sender, e):
    print("Run completed")
