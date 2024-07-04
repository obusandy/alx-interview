#!/usr/bin/python3
"""
UTF-8 Validation:
a method that determines if a given data
set represents a valid UTF-8 encoding.
"""
from typing import List
def validUTF8(data: List[int]) -> bool:
    """
    Determines if the given data set reps a valid UTF-8 encoding.
    Args:
    - data ([int]): A list of int rep 1 byte of data each.
    Returns: - bool: True if data is a valid UTF-8 encoding,
    False otherwise.
    """

    num_rembytes = 0
    # No of rem bytes to complete the current UTF-8 character

    for byte in data:

        mask = 1 << 7

        # Mask to check if the byte is a part of a UTF-8 char

        if not num_rembytes:

            while byte & mask:
                num_rembytes += 1
                mask >>= 1

# If it's a single byte character
            if not num_rembytes:
                continue
                # If it's a single byte character, no need to check for it any more

            if num_rembytes == 1 or num_rembytes > 4:
                return False
        else:
# Check if the byte is a continuation byte (starts with 10)
            if byte >> 6 != 0b10:
                return False

        num_rembytes -= 1
# If all bytes have been correctly processed, total num of rem bytes should be 0
    return num_rembytes == 0