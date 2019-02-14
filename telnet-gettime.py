#! /usr/bin/env python3

import telnetlib, time


def main():
    HOST = 'india.colorado.edu'
    PORT = 13
    tn = telnetlib.Telnet(HOST, PORT)
    r = tn.read_all().decode('utf-8')
    time.sleep(1)
    print(r)


if __name__ == '__main__':
    main()
