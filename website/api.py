from flask import Blueprint
from . import Core, Engine, Procedure, System

api = Blueprint('api', __name__, url_prefix='api')

@api.route('/run-sequence')
def run_sequence():
    Core.Commands.RuntimeInitialize()
    engine = Engine()
    proc_info = System.IO.FileInfo(r"C:\Path\To\sequence.ovp")
    procedure = Procedure(proc_info)

    engine.ProcedureComplete += engine_procedure_complete
    engine.Start(procedure, Engine.RunType.Normal)
    return "Sequence started!"

def engine_procedure_complete(sender, e):
    print("Run completed")
