"""
Run-length encoding (RLE) is a simple compression algorithm 
that gets a stream of data as the input and returns a
sequence of counts of consecutive data values in a row.
When decompressed the data will be fully recovered as RLE
is a lossless data compression.
"""

def encode_rle(input):
    """
    Gets a stream of data and compresses it
    under a Run-Length Encoding.
    :param input: The data to be encoded.
    :return: The encoded string.
    """
    if not input: return ''

    encoded_str = ''
    prev_ch = ''
    count = 1

    for ch in input:

        # Check If the subsequent character does not match
        if ch != prev_ch:
            # Add the count and character
            if prev_ch:
                encoded_str += str(count) + prev_ch
            # Reset the count and set the character
            count = 1
            prev_ch = ch
        else:
            # Otherwise increment the counter
            count += 1
    else:
        return encoded_str + (str(count) + prev_ch)


def decode_rle(input):
    """
    Gets a stream of data and decompresses it
    under a Run-Length Decoding.
    :param input: The data to be decoded.
    :return: The decoded string.
    """
    decode_str = ''
    count = ''

    for ch in input:
        # If not numerical
        if not ch.isdigit():
            # Expand it for the decoding
            decode_str += ch * int(count)
            count = ''
        else:
            # Add it in the counter
            count += ch
    return decode_str
