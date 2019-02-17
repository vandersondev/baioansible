#! /usr/bin/env python3

import telnetlib, time


def main():
    HOST = 'india.colorado.edu'
    PORT = 13
    tn = telnetlib.Telnet(HOST, PORT)
    tn.set_debuglevel(1)
    print(tn.read_all().decode('utf-8'))


if __name__ == '__main__':
    main()
