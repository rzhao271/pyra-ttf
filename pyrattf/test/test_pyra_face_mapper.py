import pytest
from pyrattf.pyra_face_mapper import PyraFaceMapper


def test_is_face_twist():
    vertex_moves = [
        "R", "Rw", "L", "Lw", "D", "Dw", "F", "Fw",
        "R2", "Rw'", "Lw2'", "L'2", "Dw'2", "Dw2", "F'", "Fw2"
    ]
    expected_is_face_turn = [
        False, True, False, True, False, True, False, True,
        False, True, True, False, True, True, False, True
    ]
    for move, expected in zip(vertex_moves, expected_is_face_turn):
        assert PyraFaceMapper.is_face_twist(move) == expected


def test_is_face_twist_dual_layer():
    vertex_moves = [
        "2R", "2Rw", "2L", "2Lw", "D", "2Dw", "F", "Fw",
        "R2", "Rw'", "2Lw2'", "L'2", "2Dw'2", "2Dw2", "F'", "2Fw2"
    ]
    expected_is_face_turn = [
        False, True, False, True, False, True, False, True,
        False, True, True, False, True, True, False, True
    ]
    for move, expected in zip(vertex_moves, expected_is_face_turn):
        assert PyraFaceMapper.is_face_twist(move) == expected


def test_convert_vertex_twist_to_face_twist_r():
    vertex_moves = ["R", "R'", "R2", "R'2", "R2'"]
    expected_face_moves = ["Lw [R]", "Lw' [R']",
                           "Lw2 [R2]", "Lw'2 [R'2]", "Lw2' [R2']"]
    for v, e in zip(vertex_moves, expected_face_moves):
        assert PyraFaceMapper.convert_vertex_twist_to_face_twist(v) == e
    vertex_moves = ["r", "r'", "r2", "r'2", "r2'"]
    expected_face_moves = ["2Lw [R]", "2Lw' [R']",
                           "2Lw2 [R2]", "2Lw'2 [R'2]", "2Lw2' [R2']"]
    for v, e in zip(vertex_moves, expected_face_moves):
        assert PyraFaceMapper.convert_vertex_twist_to_face_twist(v) == e
    vertex_moves = ["r3", "r'3", "r3'", "R3", "R'3", "R3'"]
    for v in vertex_moves:
        try:
            PyraFaceMapper.convert_vertex_twist_to_face_twist(v)
            assert False
        except AssertionError:
            raise
        except:
            pass


def test_convert_vertex_twist_to_face_twist_l():
    vertex_moves = ["L", "L'", "L2", "L'2", "L2'"]
    expected_face_moves = ["Rw [L]", "Rw' [L']",
                           "Rw2 [L2]", "Rw'2 [L'2]", "Rw2' [L2']"]
    for v, e in zip(vertex_moves, expected_face_moves):
        assert PyraFaceMapper.convert_vertex_twist_to_face_twist(v) == e
    vertex_moves = ["l", "l'", "l2", "l'2", "l2'"]
    expected_face_moves = ["2Rw [L]", "2Rw' [L']",
                           "2Rw2 [L2]", "2Rw'2 [L'2]", "2Rw2' [L2']"]
    for v, e in zip(vertex_moves, expected_face_moves):
        assert PyraFaceMapper.convert_vertex_twist_to_face_twist(v) == e
    vertex_moves = ["l3", "l'3", "l3'", "L3", "L'3", "L3'"]
    for v in vertex_moves:
        try:
            PyraFaceMapper.convert_vertex_twist_to_face_twist(v)
            assert False
        except AssertionError:
            raise
        except:
            pass


def test_convert_vertex_twist_to_face_twist_b():
    vertex_moves = ["B", "B'", "B2", "B'2", "B2'"]
    expected_face_moves = ["Fw [B]", "Fw' [B']",
                           "Fw2 [B2]", "Fw'2 [B'2]", "Fw2' [B2']"]
    for v, e in zip(vertex_moves, expected_face_moves):
        assert PyraFaceMapper.convert_vertex_twist_to_face_twist(v) == e
    vertex_moves = ["b", "b'", "b2", "b'2", "b2'"]
    expected_face_moves = ["2Fw [B]", "2Fw' [B']",
                           "2Fw2 [B2]", "2Fw'2 [B'2]", "2Fw2' [B2']"]
    for v, e in zip(vertex_moves, expected_face_moves):
        assert PyraFaceMapper.convert_vertex_twist_to_face_twist(v) == e
    vertex_moves = ["b3", "b'3", "b3'", "b3", "b'3", "b3'"]
    for v in vertex_moves:
        try:
            PyraFaceMapper.convert_vertex_twist_to_face_twist(v)
            assert False
        except AssertionError:
            raise
        except:
            pass


def test_convert_vertex_twist_to_face_twist_u():
    vertex_moves = ["U", "U'", "U2", "U'2", "U2'"]
    expected_face_moves = ["Dw [U]", "Dw' [U']",
                           "Dw2 [U2]", "Dw'2 [U'2]", "Dw2' [U2']"]
    for v, e in zip(vertex_moves, expected_face_moves):
        assert PyraFaceMapper.convert_vertex_twist_to_face_twist(v) == e
    vertex_moves = ["u", "u'", "u2", "u'2", "u2'"]
    expected_face_moves = ["2Dw [U]", "2Dw' [U']",
                           "2Dw2 [U2]", "2Dw'2 [U'2]", "2Dw2' [U2']"]
    for v, e in zip(vertex_moves, expected_face_moves):
        assert PyraFaceMapper.convert_vertex_twist_to_face_twist(v) == e
    vertex_moves = ["u3", "u'3", "u3'", "u3", "u'3", "u3'"]
    for v in vertex_moves:
        try:
            PyraFaceMapper.convert_vertex_twist_to_face_twist(v)
            assert False
        except AssertionError:
            raise
        except:
            pass


def test_convert_vertex_twist_to_face_twist_invalid():
    invalid_list = ["P", "P'", "B U", "F", "Bw", "H3", "u4"]
    for inv in invalid_list:
        try:
            PyraFaceMapper.convert_vertex_twist_to_face_twist(inv)
            assert False
        except AssertionError:
            raise
        except:
            pass
