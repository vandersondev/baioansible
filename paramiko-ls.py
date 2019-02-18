#! /usr/bin/env python3

import paramiko


def main():
    HOST = '172.16.82.129'

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(HOST)
    stdin, stdout, stderr = client.exec_command('ls -ls')
    print(stdout.read().decode('utf-8'))


if __name__ == '__main__':
    main()
