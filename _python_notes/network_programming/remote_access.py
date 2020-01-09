#!/usr/bin/env python

"""
Remote Access
    Use paramiko (not part of standard library, but included with Anaconda)
    Create ssh client
    Create transport object to use sftp

    To avoid the "I haven't seen this host before" prompt, call set_missing_host_key_policy()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPoliciy())

    The exec_command() method executs a command on the remote host, and returns a triple with the
    remote command's stdin, stdout, and stderr as file-like ojbects

    Note
        Paramiko is used by Ansible and other sys admin tools
        Find out more about paramiko at http://www.lag.net/paramiko/
        Find out more about Ansible at http://www.ansible.com/
"""