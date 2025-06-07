import math

###########################################################################
# These are the Parameters of the LZSS Algorythm You Should USE
#   you can change these parameters to smaller values for testing, but
#   make sure to use these for the final encoding/decoding and export
###########################################################################

# The size in bits of the complete Sliding Window including Search Buffer and Look Ahead Buffer
window_size = 4 * 1028 * 8 #  bit = 4KB = 32768 bit

# The size in bits of the Look Ahead Buffer
look_ahead_buffer_size = 256 # bit

# The size in bits of the Search Buffer
search_buffer_size = window_size - look_ahead_buffer_size

# The minimal length of digits to be treated as a found match
min_match_length = 3


# The number of bit digits needed to binary encode the offset values
offset_bit_length = int(math.ceil(math.log2(search_buffer_size))) + 1

# The number of bit digits needed to binary encode the match length values
match_bit_length = int(math.ceil(math.log2(look_ahead_buffer_size))) + 1


####################################################
# implement the ASCII CHAR TO BINARY CONVERSION here
####################################################
def lzss_encode(to_encode: str) -> str:
    i = 0
    encoded = ''
    while i < len(to_encode):
        match_offset = 0
        match_length = 0
        max_len = min(look_ahead_buffer_size, len(to_encode) - i)

        search_start = max(0, i - search_buffer_size)
        for j in range(search_start, i):
            length = 0
            while (length < max_len and
                   to_encode[j + length] == to_encode[i + length]):
                length += 1
                if j + length >= i or i + length >= len(to_encode):
                    break
            if length >= min_match_length and length > match_length:
                match_offset = i - j
                match_length = length

        if match_length >= min_match_length:
            offset_bin = format(match_offset, f'0{offset_bit_length}b')
            length_bin = format(match_length, f'0{match_bit_length}b')
            encoded += '1' + offset_bin + length_bin
            i += match_length
        else:
            encoded += '0' + to_encode[i]
            i += 1

    return encoded



####################################################
# implement the ASCII CHAR TO BINARY CONVERSION here
####################################################
def lzss_decode(to_decode: str) -> str:
    decoded = ''
    i = 0
    while i < len(to_decode):
        flag = to_decode[i]
        i += 1
        if flag == '0':
            decoded += to_decode[i]
            i += 1
        elif flag == '1':
            offset = int(to_decode[i:i + offset_bit_length], 2)
            i += offset_bit_length
            length = int(to_decode[i:i + match_bit_length], 2)
            i += match_bit_length
            start = len(decoded) - offset
            for j in range(length):
                decoded += decoded[start + j]

    return decoded
