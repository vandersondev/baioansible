#! /usr/bin/env python3

import telnetlib, time


def main():
    HOST = 'telehack.com'
    PORT = 23
    tn = telnetlib.Telnet(HOST, PORT)
    tn.set_debuglevel(0)
    tn.read_until(b'\r\n\r\n.')
    tn.write(b'uptime\r')
    print(tn.read_until(b'\r\n.').decode('utf-8'))
    tn.close()


if __name__ == '__main__':
    main()
