import sys
sys.path.append('../website')
from pvar import dict_to_pvar_string, pvar_string_to_dict

string_form = \
"""
item=apple
quantity=1
color=green
taste=Red
"""

dict_form = {
    "item": "apple",
    "quantity": "1",
    "color": "green",
    "taste": "Red"
}

def test_d2s():
    assert dict_to_pvar_string(dict_form) == string_form.strip()

def test_s2d():
    assert pvar_string_to_dict(string_form) == dict_form
