##########################
# DO NOT CHANGE THIS FILE!
##########################
from distutils.versionpredicate import re_paren

# Exception: You can comment out the single steps for testing but make sure all file exports take place in the end!

from ASCII_converter import*
from LZSS_encoder import*


# Execute this main method to apply the Encoding and Decoding steps to the relevant files
# The solution is only intended to work with the ASCII set of characters!
if __name__ == '__main__':

    ##### Full Loop Encoding and Decoding #####

    # Load the Lorem Ipsum Text to be decoded
    with open('text_files/LZSS_to_encode.txt', 'r') as file:
        text_to_encode = file.read()
        print(text_to_encode)

    # Convert the ASCII characters to their 7-bit binary representation
    binary_text = convert_ascii_to_binary(text_to_encode)
    print(len(binary_text),'bit text:', binary_text)

    # Apply the LZSS Encoding on the binary text string
    lzss_encoded_text = lzss_encode(binary_text)
    print(len(lzss_encoded_text), 'bit text:', lzss_encoded_text)

    # Decode the encoded binary text string again (just for testing)
    re_decoded_binary_text = lzss_decode(lzss_encoded_text)
    print(len(re_decoded_binary_text), 'bit text:', re_decoded_binary_text)

    # Convert the 7-bit binary representation back to the human-readable ASCII characters (just for testing)
    # This text should be the same as the input text
    re_decoded_text = convert_binary_to_ascii(re_decoded_binary_text)
    print(re_decoded_text)


    ##### Saving the Encoding Steps to Files #####

    # Save the Binary ASCII representation
    with open('text_files/binary_to_encode.txt', 'w') as file:
        file.write(binary_text)

    # Save the Encoded Text
    with open('text_files/LZSS_encoded.txt', 'w') as file:
        file.write(lzss_encoded_text)


    ##### Decoding of a Pre-Encoded File#####

    # Open the encoded example file for decoding
    with open('text_files/LZSS_to_decode.txt', 'r') as file:
        text_to_decode = file.read()
        print(text_to_decode)

    # Decode the encoded binary text string
    decoded_binary_text = lzss_decode(text_to_decode)
    print(decoded_binary_text)

    # Convert the 7-bit binary representation back to the human-readable ASCII characters
    decoded_text = convert_binary_to_ascii(decoded_binary_text)
    print(decoded_text)


    ##### Saving the Decoding Steps to Files #####

    # Save the Decoded Binary ASCII representation
    with open('text_files/binary_to_decode.txt', 'w') as file:
        file.write(decoded_binary_text)

    # Save the complete Decoded File
    with open('text_files/LZSS_decoded.txt', 'w') as file:
        file.write(decoded_text)


