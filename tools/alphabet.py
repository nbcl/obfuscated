# GNU AFFERO GENERAL PUBLIC LICENSE
# Version 3, 19 November 2007

from string import ascii_letters
from random import choice


def update(d: dict, func: str, attr: str) -> None:
    """ Updates dictionary with new char instances

    Tries the complete "attr" (attribute) (either
    __doc__ or __name__) from "func" (function) to find
    alphabet character instances, updating "d" (dict)
    in-place.

    Args:
        d : An alphabet dictionary instance
        func : The selected function
        attr : Attribute of the function

    Returns:
        None
    """
    try:
        string = eval(f"{func}.{attr}")
        for index in range(len(string)):
            char = string[index]
            if char in d:
                d[char] = d[char].copy() + \
                    [f"{func}.{attr}[{index}]"]
    except:
        print(f"{func} : has no .{attr}")


def choose(d: dict, c: str) -> str:
    """ Chooses a random generator for a char

    Uses random choice or yields key if no option
    was found before.

    Args:
        d : An alphabet dictionary instance
        c : Character to select

    Returns:
        Random generator function or character key
    """
    return choice(d[c]) if d[c] else c


def alphabet(chars: list = []) -> dict:
    """ Generates a random ascii letters alphabet using

    Uses .__doc__ and .__name__ instances from __builtins__
    to generate a custom dictionary with each character
    from ascii.letters.

    Args:
        chars (optional) : Additional character list

    Returns:
        An alphabet dictionary 
    """
    # Build initial dictionary with ascii letters and additional chars
    alphabet = dict.fromkeys(ascii_letters, []) | dict.fromkeys(chars, [])

    # Update all function instances from __builtins__
    for f in __builtins__.__dict__:
        update(alphabet, f, "__name__")
        update(alphabet, f, "__doc__")

    # Choose a random instance for each char
    return {char: choose(alphabet, char) for char, _ in alphabet.items()}
