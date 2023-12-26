#!/usr/bin/python3
"""
0-stats.py - Prints out status code and file size statistics
    of logs inputted from stdin
"""

from sys import stdin
from typing import Dict


total_size: int = 0
status_count: Dict[str, int] = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_stats():
    """
    Prints out the status code and file statistics

    Returns: None
    """
    print("File size: {}".format(total_size))
    for status in sorted(status_count.keys()):
        if status_count[status] != 0:
            print("{}: {}".format(status, status_count[status]))



def parse_logs():
    """
    Goes through the logs inputted via stdin, Printing out
        the status code and file size statistics every 10 lines

    Returns: None
    """
    global total_size
    global status_count
    count: int = 0

    try:
        for log in stdin:
            sections = log.split(' ')
            if ((len(sections) != 9) or
                    (sections[1] != '-') or
                    (sections[4] != '"GET') or
                    (sections[5] != '/projects/260') or
                    (sections[6] != 'HTTP/1.1"') or
                    (sections[7] not in status_count.keys())):
                pass
            try:
                total_size += int(sections[8])
            except TypeError:
                pass
            status_count[sections[7]] += 1
            count += 1
            if count % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise


if __name__ == "__main__":
    parse_logs()
