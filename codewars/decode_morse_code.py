"""
Decoding morse code,
More information: https://www.codewars.com/kata/54b724efac3d5402db00065e/train/python
"""

# MORSE_CODE is dictionary constant provided with assigment (contains all needed characters in morse code)
def decodeMorse(morse_code):
    return "".join(map(lambda a: MORSE_CODE[a] if a != 'x' else ' ' , morse_code.strip().replace('   ',' x ').split())