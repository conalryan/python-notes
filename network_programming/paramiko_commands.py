#!/usr/bin/env python

import paramiko

# Create paramiko client
with paramiko.SSHClient() as ssh:

    # Ignore missing keys (this is safe)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to remote host
    ssh.connect('localhost', 22, username='admin', password='password')

    # Execute remote command; returns standard I/O objects
    stdin, stdout, stderr  = ssh.exec_command('whoami')
    # Read stdout of command
    print(stdout.read().decode())
    print('-' * 60)

    # Execute remote command; returns standard I/O objects
    stdin, stdout, stderr  = ssh.exec_command('ls -l')
    # Read stdout of command
    print(stdout.read().decode())
    print('-' * 60)

    # Execute remote command; returns standard I/O objects
    stdin, stdout, stderr = ssh.exec_command('ls -l /etc/passwd /etc/horcrux')
    print("STDOUT:")
    # Read stdout of command
    print(stdout.read().decode())
    print("STDERR:")
    # Read stderr of command
    print(stderr.read().decode())
    print('-' * 60)
