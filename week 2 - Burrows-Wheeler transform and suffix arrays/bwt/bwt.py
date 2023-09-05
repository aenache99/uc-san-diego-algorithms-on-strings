# python3
import sys


def BWT(text):
    # Create a list of all cyclic rotations of the text
    rotations = [text[i:] + text[:i] for i in range(len(text))]

    # Sort the list of rotations lexicographically
    sorted_rotations = sorted(rotations)

    # Extract the last characters of each sorted rotation to form the BWT
    bwt = ''.join(rotation[-1] for rotation in sorted_rotations)

    return bwt


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    bwt = BWT(text)
    print(bwt)
