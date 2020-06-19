import pytest
from pyra_reducer import PyraReducer

# Assumption for these tests: the moves have already been validated by the converter
def test_is_rotation_move():
    moves = ["Rw", "R2'", "r", "2Dw", "Fw", "[B]", "[L2]", "[U]", "[R'2]", "[B2']"]
    expected_is_rotation = [False, False, False, False, False, True, True, True, True, True]
    for move, expected in zip(moves, expected_is_rotation):
        assert PyraReducer.is_rotation_move(move) == expected

def test_isolate_twist_elements():
    moves = ["Rw", "Dw2'", "2Lw", "2Fw'2", "2Rw'", "2Dw", "Lw'2", "Fw2"]
    expecteds = [("", "Rw", ""), ("", "Dw", "2'"), ("2", "Lw", ""), ("2", "Fw", "'2"),
        ("2", "Rw", "'"), ("2", "Dw", ""), ("", "Lw", "'2"), ("", "Fw", "2")]
    for move, expected in zip(moves, expecteds):
        assert PyraReducer.isolate_twist_elements(move) == expected

def test_isolate_rotation_elements():
    moves = ["[R]", "[U2']", "[L]", "[B'2]", "[L']", "[U]", "[R'2]", "[B2]"]
    expecteds = [("R", ""), ("U", "2'"), ("L", ""), ("B", "'2"),
        ("L", "'"), ("U", ""), ("R", "'2"), ("B", "2")]
    for move, expected in zip(moves, expecteds):
        assert PyraReducer.isolate_rotation_elements(move) == expected

def test_cancel_rotations_basic():
    moves = [[], ["Lw", "[R]"], ["Rw'2", "[L'2]"], ["Fw2", "[B2]"], ["Dw'", "[U']"]]
    expecteds = [[], ["Lw"], ["Rw'2"], ["Fw2"], ["Dw'"]]
    for move, expected in zip(moves, expecteds):
        assert list(PyraReducer.cancel_rotations(move)) == expected

def test_cancel_rotations_basic_l():
    moves = [
        ["Lw", "[R]", "Lw"], ["Lw", "[L]", "Lw"], ["Lw", "[B]", "Lw"], ["Lw", "[U]", "Lw"],
        ["Lw", "[R']", "Lw"], ["Lw", "[L']", "Lw"], ["Lw", "[B']", "Lw"], ["Lw", "[U']", "Lw"]
    ]
    expecteds = [
        ["Lw", "Lw"], ["Lw", "Dw"], ["Lw", "Rw"], ["Lw", "Fw"],
        ["Lw", "Lw"], ["Lw", "Fw"], ["Lw", "Dw"], ["Lw", "Rw"]
    ]
    for move, expected in zip(moves, expecteds):
        assert list(PyraReducer.cancel_rotations(move)) == expected

def test_cancel_rotations_basic_l_primes():
    moves = [
        ["Lw", "[R]", "Lw'"], ["Lw'", "[L]", "Lw"], ["Lw'", "[B]", "Lw'"], ["2Lw", "[U]", "2Lw"],
        ["Lw'", "[R']", "Lw'"], ["Lw'", "[L']", "Lw"], ["Lw'", "[B']", "Lw'"], ["2Lw", "[U']", "2Lw"]
    ]
    expecteds = [
        ["Lw", "Lw'"], ["Lw'", "Dw"], ["Lw'", "Rw'"], ["2Lw", "2Fw"],
        ["Lw'", "Lw'"], ["Lw'", "Fw"], ["Lw'", "Dw'"], ["2Lw", "2Rw"]
    ]
    for move, expected in zip(moves, expecteds):
        assert list(PyraReducer.cancel_rotations(move)) == expected

def test_cancel_rotations_basic_r():
    moves = [
        ["Rw", "[R]", "Rw"], ["Rw", "[L]", "Rw"], ["Rw", "[B]", "Rw"], ["Rw", "[U]", "Rw"],
        ["Rw", "[R']", "Rw"], ["Rw", "[L']", "Rw"], ["Rw", "[B']", "Rw"], ["Rw", "[U']", "Rw"]
    ]
    expecteds = [
        ["Rw", "Fw"], ["Rw", "Rw"], ["Rw", "Dw"], ["Rw", "Lw"],
        ["Rw", "Dw"], ["Rw", "Rw"], ["Rw", "Lw"], ["Rw", "Fw"]
    ]
    for move, expected in zip(moves, expecteds):
        assert list(PyraReducer.cancel_rotations(move)) == expected

def test_cancel_rotations_basic_d():
    moves = [
        ["Dw", "[R]", "Dw"], ["Dw", "[L]", "Dw"], ["Dw", "[B]", "Dw"], ["Dw", "[U]", "Dw"],
        ["Dw", "[R']", "Dw"], ["Dw", "[L']", "Dw"], ["Dw", "[B']", "Dw"], ["Dw", "[U']", "Dw"]
    ]
    expecteds = [
        ["Dw", "Rw"], ["Dw", "Fw"], ["Dw", "Lw"], ["Dw", "Dw"],
        ["Dw", "Fw"], ["Dw", "Lw"], ["Dw", "Rw"], ["Dw", "Dw"]
    ]
    for move, expected in zip(moves, expecteds):
        assert list(PyraReducer.cancel_rotations(move)) == expected

def test_cancel_rotations_basic_f():
    moves = [
        ["Fw", "[R]", "Fw"], ["Fw", "[L]", "Fw"], ["Fw", "[B]", "Fw"], ["Fw", "[U]", "Fw"],
        ["Fw", "[R']", "Fw"], ["Fw", "[L']", "Fw"], ["Fw", "[B']", "Fw"], ["Fw", "[U']", "Fw"]
    ]
    expecteds = [
        ["Fw", "Dw"], ["Fw", "Lw"], ["Fw", "Fw"], ["Fw", "Rw"],
        ["Fw", "Rw"], ["Fw", "Dw"], ["Fw", "Fw"], ["Fw", "Lw"]
    ]
    for move, expected in zip(moves, expecteds):
        assert list(PyraReducer.cancel_rotations(move)) == expected

def test_cancel_rotations_intermediate():
    moves = [
        ["Lw", "[R]", "Lw", "[L]", "Lw"], ["Lw", "[B]", "Lw", "[U]", "Lw'"],
        ["Lw", "[R']", "Dw", "[L']", "Lw"], ["Dw'", "[B']", "Fw'", "[U']", "Rw'"]
    ]
    expecteds = [
        ["Lw", "Lw", "Rw"], ["Lw", "Rw", "Fw'"],
        ["Lw", "Fw", "Rw"], ["Dw'", "Fw'", "Fw'"],
    ]
    for move, expected in zip(moves, expecteds):
        assert list(PyraReducer.cancel_rotations(move)) == expected
