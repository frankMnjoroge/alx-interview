#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    no_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for j in data:

        no_byte = 1 << 7

        if no_bytes == 0:

            while mask_byte & j:
                no_bytes += 1
                mask_byte = mask_byte >> 1

            if no_bytes == 0:
                continue

            if no_bytes == 1 or no_bytes > 4:
                return False

        else:
            if not (j & mask_1 and not (j & mask_2)):
                    return False

        no_bytes -= 1

    if no_bytes == 0:
        return True

    return False
