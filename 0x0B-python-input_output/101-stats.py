#!/usr/bin/python3
"""This module contains a script that reads stdin line by line
and computes metrics:

Input format: '<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>'

Each 10 lines and after a keyboard interruption (CTRL + C), prints those
statistics since the beginning:
Total file size: File size: <total size>
where is the sum of all previous (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""

import sys

file_size = 0
status_codes = {"200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0}
it = 0


def print_stats():
    """Prints current statistics"""
    print(f'File size: {file_size}')
    for key, value in status_codes.items():
        if value > 0:
            print(f'{key}: {value}')


try:
    for line in sys.stdin:
        if it != 0 and it % 10 == 0:
            print_stats()
        content = line.split()
        try:
            if content[-2] in status_codes:
                status_codes[content[-2]] += 1
        except Exception as e:
            pass
        try:
            file_size += int(content[-1])
        except Exception as e:
            pass
        it += 1
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
