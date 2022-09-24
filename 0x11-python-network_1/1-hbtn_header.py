#!/usr/bin/python3
'''script for task 1'''

if __name__ == '__main__':
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.info()['X-Request-Id'])
