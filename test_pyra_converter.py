import pytest
from pyra_converter import PyraConverter

def test_pyra_converter_basic():
    assert PyraConverter.convert_tip_alg_to_face_alg("") == ""
    assert PyraConverter.convert_tip_alg_to_face_alg("R") == "Lw"
    assert PyraConverter.convert_tip_alg_to_face_alg("R U") == "Lw Rw"

def test_pyra_converter_sledgehammer():
    assert PyraConverter.convert_tip_alg_to_face_alg("R' L R L'") == "Lw' Dw Fw Lw'"
    assert PyraConverter.convert_tip_alg_to_face_alg("r' l r l'") == "2Lw' 2Dw 2Fw 2Lw'"
