from typing import Tuple, Iterable


class PyraReducer:
    # Assumption: the inputs have been cleared via the PyraConverter first

    @staticmethod
    def is_rotation_move(move: str) -> bool:
        return move[0] == "[" and move[-1] == "]"

    @staticmethod
    def isolate_twist_elements(move: str) -> Tuple[str, str, str]:
        # Example: isolate_twist_elements("Dw2") -> ("1", "Dw", "2")
        # Example: isolate_twist_elements("2Fw") -> ("2", "Fw", "")
        # isolate_twist_elements: Str -> (Str, Str, Str)
        if len(move) >= 3 and move[0] == '2' and move[2] == 'w':
            return ("2", move[1:3], move[3:])
        else:
            return ("", move[0:2], move[2:])

    @staticmethod
    def isolate_rotation_elements(rotation: str) -> Tuple[str, str]:
        # Example: isolate_rotation_elements("[U]") -> ("U", "")
        # Example: isolate_rotation_elements("[R2']") -> ("R", "2'")
        return (rotation[1], rotation[2:-1])

    @staticmethod
    def cancel_rotations(moves: Iterable[str]) -> Iterable[str]:
        '''
        The input is the entire algorithm as converted over to face twists and rotations by the converter
        This method cancels out all the rotation moves
        '''

        # simulate pyraminx corners virtually
        # 0 = original U corner, 1 = original L corner, 2 = original R corner, 3 = original B corner
        # indices 0, 1, 2, 3 = the slots that the U, L, R, B corners start in, respectively
        virtual_pyra_corners = [0, 1, 2, 3]

        # example for below: [L.*] involves cycling indices 0 -> 2 -> 3
        rotation_vertex_indices_map = {"L": [0, 2, 3], "R": [
            0, 3, 1], "U": [1, 3, 2], "B": [2, 0, 1]}
        # translate vertex rotation turn suffixes to face CCW repetition times
        times_cw_map = {"": 1, "2": 2, "'": 2, "'2": 1, "2'": 1}

        # example for below: [Lw.*] involves cycling indices 0 -> 1 -> 3
        face_indices_map = {"Lw": [0, 1, 3], "Rw": [
            0, 3, 2], "Dw": [1, 2, 3], "Fw": [2, 1, 0]}
        indices_face_map = {"013": "Lw", "023": "Rw", "123": "Dw", "012": "Fw"}

        for move in moves:
            if PyraReducer.is_rotation_move(move):
                rotation_axis, rotation_amount_str = PyraReducer.isolate_rotation_elements(
                    move)
                vertices_to_swap = rotation_vertex_indices_map[rotation_axis]
                rotation_amount = times_cw_map[rotation_amount_str]
                # carry out the swap rotation_amount times
                for _ in range(rotation_amount):
                    temp = virtual_pyra_corners[vertices_to_swap[-1]]
                    for j in range(len(vertices_to_swap) - 1, 0, -1):
                        virtual_pyra_corners[vertices_to_swap[j]
                                             ] = virtual_pyra_corners[vertices_to_swap[j - 1]]
                    virtual_pyra_corners[vertices_to_swap[0]] = temp
            else:
                # $move is a face-turn move
                layers, face, rotation_amount_str = PyraReducer.isolate_twist_elements(
                    move)
                # we have to use virtual_pyra_corners to figure out which face is actually being turned
                # e.g. if virtual_pyra_corners is [0, 2, 3, 1]
                #      and the input turn is Rw [0, 3, 2], then we want to cycle elements of indices [0, 2, 1]
                #      of virtual_pyra_corners, which corresponds to 012 when turned into a sorted joined string,
                #      which corresponds to the output turn Fw.
                indices_for_turn = face_indices_map[face]
                vertices_on_face = [virtual_pyra_corners[index]
                                    for index in indices_for_turn]
                key = "".join([str(x) for x in sorted(vertices_on_face)])
                output_face = indices_face_map[key]
                yield layers + output_face + rotation_amount_str
