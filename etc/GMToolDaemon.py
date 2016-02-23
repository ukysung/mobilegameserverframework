
import os
import sys
import atexit
import time

def main():
    pid = os.fork()
    if pid > 0:
        sys.exit()

    os.chdir('/')
    os.setsid()
    os.umask(0)

    file = open('/dev/null', 'w')
    def close_file():
        file.close()

    sys.stdin = file
    sys.stdout = file
    sys.stderr = file

    atexit.register(close_file)

    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()

