import sys
from typing import List
from pyrattf.pyra_converter import PyraConverter


def main(argv: List[str]):
    if len(argv) != 2 or len(argv[1].strip()) == 0:
        print("Usage: python3 pyra-ttf.py \"[algorithm]\"", file=sys.stderr)
        print(
            "or if from the pyrattf script: ./pyrattf.sh \"[algorithm]\"", file=sys.stderr)
        sys.exit(1)

    try:
        converted_alg = PyraConverter.convert_tip_alg_to_face_alg(argv[1])
        print(converted_alg)
        sys.exit(0)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)
