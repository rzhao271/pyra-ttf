class PyraFaceMapper:
    @staticmethod
    def is_face_twist(original_move: str) -> bool:
        return (len(original_move) >= 2 and original_move[1] == 'w') or \
            (len(original_move) >=
             3 and original_move[0] == '2' and original_move[2] == 'w')

    @staticmethod
    def convert_vertex_twist_to_face_twist(original_move: str) -> str:
        '''
        Given a vertex twist X, translate it to a face twist followed by a vertex-based rotation
        For example, U becomes Dw [U], and U' becomes Dw' [U']
        Given a face twist, keep it after checking validity
        For example, Dw' stays as Dw'
        '''
        vertex_face_map = {
            "U": "Dw", "R": "Lw", "L": "Rw", "B": "Fw",
            "u": "2Dw", "r": "2Lw", "l": "2Rw", "b": "2Fw"
        }
        accepted_directions = ["", "'", "2", "2'", "'2"]
        accepted_faces = vertex_face_map.values()
        if PyraFaceMapper.is_face_twist(original_move):
            # e.g. if the original move is Dw2 or 2Fw2', etc.,
            # the move should be left unchanged but verified
            wide_move_char_index = original_move.find('w')
            if wide_move_char_index < 0:
                raise Exception("Invalid move entered: " + original_move)
            move_direction = original_move[wide_move_char_index + 1:]
            face_move = original_move[:wide_move_char_index + 1]
            if face_move not in accepted_faces:
                raise Exception("Invalid move entered: " + original_move)
            final_face_move = original_move
        else:
            # e.g. if the original move is u',
            # the face move with the direction is 2Dw',
            # and the following_rotation is [U']
            vertex_move_tip = original_move[:1]
            move_direction = original_move[1:]
            face_move = vertex_face_map.get(vertex_move_tip)
            if face_move is None:
                raise Exception("Invalid move entered: " + original_move)
            face_move_with_direction = face_move + move_direction
            final_face_move = face_move_with_direction + \
                " " + "[" + original_move.upper() + "]"

        if move_direction not in accepted_directions:
            raise Exception("Invalid move direction detected")

        return final_face_move
