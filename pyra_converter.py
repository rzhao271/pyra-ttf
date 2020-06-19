from pyra_face_mapper import PyraFaceMapper
from pyra_reducer import PyraReducer

class PyraConverter:
    # Goal: given a vertex-turning pyraminx alg, convert it to its equivalent face-turning alg
    # Valid vertices (WCA): U, L, R, B, u, l, r, b
    # Valid faces: Dw, Rw, Lw, Fw, 2Dw, 2Rw, 2Lw, 2Fw
    # Valid vertex directions: [none], ', 2, 2', '2

    # convert_tip_alg_to_face_alg: Str -> Str
    @staticmethod
    def convert_tip_alg_to_face_alg(vertex_alg):
        if len(vertex_alg) == 0:
            return ""

        moves = vertex_alg.split(" ")
        face_moves_with_rotations = " ".join(PyraFaceMapper.convert_vertex_twist_to_face_twist(move) for move in moves)
        face_moves = PyraReducer.cancel_rotations(face_moves_with_rotations.split(" "))
        return " ".join(face_moves)
