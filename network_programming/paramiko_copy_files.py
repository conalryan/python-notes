#!/usr/bin/env python

import os
import paramiko

"""
Copying files with Paramiko
    Create transport
    Create SFTP client with transport
    
    First create a Transport object
    Using a with block will automatically close the Transport object.
    
    From the transport object you can create an SFTPClient. On you have this, call standard FTP/SFTP methods on that object
        listdir_iter()
        get()
        put()
        mkdir()
        rmdir()
        etc.
"""
REMOTE_DIR = 'text_files'

# Create paramiko Transport instance
with paramiko.Transport(('localhost', 22)) as transport:
    # Connect to remote host
    transport.connect(username='python', password='l0lz')
    # Create SFTP client using Transport instance
    sftp = paramiko.SFTPClient.from_transport(transport)
    # Get list of items on default (login) folder (listdir_iter() returns a generator)
    for item in sftp.listdir_iter():
        print(item)
    print('-' * 60)

    # Get a file from the remote host
    remote_file = os.path.join(REMOTE_DIR, 'betsy.txt')

    # Create a folder on the remote host
    sftp.mkdir(REMOTE_DIR)
    # Copy a file to the remote host
    sftp.put('data/alice.txt', remote_file)
    # Copy a file from the remote host
    sftp.get(remote_file, 'eileen.txt')

# Use SSHClient to confirm operations (not needed, just for illustration)
with paramiko.SSHClient() as ssh:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect('localhost', username='python', password='l0lz')
    except paramiko.SSHException as err:
        print(err)
        exit()

    stdin, stdout, stderr  = ssh.exec_command('ls -l {}'.format(REMOTE_DIR))
    print(stdout.read().decode())
    print('-' * 60)

    stdin, stdout, stderr = ssh.exec_command('rm -f {}/betsy.txt'.format(REMOTE_DIR))
    stdin, stdout, stderr = ssh.exec_command('rmdir {}'.format(REMOTE_DIR))

    stdin, stdout, stderr = ssh.exec_command('ls -l')
    print(stdout.read().decode())
    print('-' * 60)
