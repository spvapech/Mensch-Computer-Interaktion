# Use this Dictionary ASCII Table for the conversion
from ASCII_table import ascii_table

####################################################
# implement the ASCII CHAR TO BINARY CONVERSION here
####################################################

def convert_ascii_to_binary(string: str) -> str:

    binary_string = ''.join(ascii_table[char] for char in string)

    return str(binary_string)


####################################################
# implement the BINARY TO ASCII CHAR CONVERSION here
####################################################
def convert_binary_to_ascii(binary_string: str) -> str:
    reverse_table = {v: k for k, v in ascii_table.items()}
    ascii_string = ''.join(
        reverse_table[binary_string[i:i + 7]] for i in range(0, len(binary_string), 7)
    )

    return ascii_string