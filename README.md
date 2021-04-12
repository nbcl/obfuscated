# Obfuscated

Obfuscating tools for Python.

## Proof of concept

Best "Hello, World!" available using the current tools:

```python
getattr(__import__(open.__doc__[2655] + str.__doc__[146]), dict.__doc__[240] + UnicodeTranslateError.__doc__[22] + input.__doc__[262] + int.__doc__[287] + exec.__doc__[129])(1, (__build_class__.__doc__[104].upper() + exec.__doc__[129] + property.__doc__[726] + property.__doc__[726] + open.__doc__[2655] + __import__.__doc__[771] + globals.__doc__[118] + ImportWarning.__name__[6] + open.__doc__[2655] + UnicodeTranslateError.__doc__[22] + property.__doc__[726] + staticmethod.__doc__[483] + range.__doc__[263]).encode(map.__doc__[64] + int.__doc__[287] + print.__doc__[331]))
```

## Tools

### [alphabet.py](tools/alphabet.py)

Generates a random ASCII letters alphabet using `.__name__` and `.__doc__` instances.

```python
>>> my_dict = alphabet()
>>> my_dict
{
   'a': zip.__doc__[266],
   'b': max.__doc__[27],
   'c': breakpoint.__doc__[93],
   ...
   'X': 'X',
   'Y': 'Y',
   'Z': input.__doc__[230],
}
```

The following characters are currently not available in any instance: `H`, `Q`, `X`, `Y`.

Additional, non-alphabet characters can also be added on generation.

```python
>>> my_dict = alphabet([" ", "!", "-"])
>>> my_dict
{
   'a': locals.__doc__[189],
   'b': dir.__doc__[423],
   'c': classmethod.__doc__[46],
   ...
   ' ': open.__doc__[388],
   '!': range.__doc__[263],
   '-': __build_class__.__doc__[60]
}

```
