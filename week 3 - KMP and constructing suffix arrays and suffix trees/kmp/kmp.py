# python3
import sys


def compute_prefix_function(pattern):
    """
    Compute the prefix function (partial match table) for the pattern.
    """
    prefix_function = [0] * len(pattern)
    border = 0  # Length of the current border (prefix of the pattern)

    for i in range(1, len(pattern)):
        while border > 0 and pattern[i] != pattern[border]:
            border = prefix_function[border - 1]

        if pattern[i] == pattern[border]:
            border += 1
        else:
            border = 0

        prefix_function[i] = border

    return prefix_function


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    result = []
    prefix_function = compute_prefix_function(pattern + '#' + text)  # Concatenate pattern and text with a separator

    for i in range(len(pattern) + 1, len(prefix_function)):
        if prefix_function[i] == len(pattern):
            result.append(i - 2 * len(pattern))

    return result


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
