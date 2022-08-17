#!/usr/bin/python3
"""
This module contain the function that mesure statistics
"""

if __name__ == '__main__':

    import sys

    statusCode = {"200": 0,
                  "301": 0,
                  "400": 0,
                  "401": 0,
                  "403": 0,
                  "404": 0,
                  "405": 0,
                  "500": 0
                  }
    fileSize = 0
    lines = 0

    def print_stat(statusCode, fileSize):
        """This function print the statistics"""
        print("File size: {:d}".format(fileSize))
        for statusCode, item in sorted(statusCode.items()):
            if item:
                print("{:s}: {:d}".format(statusCode, item))

    try:
        for line in sys.stdin:
            if lines != 0 and lines % 10 == 0:
                print_stat(statusCode, fileSize)
            lines += 1
            data = line.split()
            try:
                stCode = data[-2]
                if stCode in statusCode:
                    statusCode[stCode] += 1
                fileSize += int(data[-1])
            except Exception:
                pass
        print_stat(statusCode, fileSize)
    except KeyboardInterrupt:
        print_stat(statusCode, fileSize)
        raise
