"""
Name: Jalen Vaughn
Date: 2/13/24
File: utils.py
Description: Contains helper functions relevant to the other files in the directory.
Dependencies/Imports: 
"""


def print_header(header=None) -> None:
    """
    Prints a header to the console with a given text inside
    :param header: Optional string to use for the text inside the header.
    """
    if header is None:
        print("=" * 60)

    else:  # calculate the correct amount of "=" and dead space to properly fit header in the center
        width = 60  # total size
        padding = (width - len(header)) // 2  # the amount of "=" signs to put on both sides
        print("=" * padding, header, "=" * padding)
