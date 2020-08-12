#!/usr/bin/python3

import paramiko
from scp import SCPClient

hostname = "localhost"
username = "berto"
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
key_path ="/home/berto/.ssh/id_rsa"
ssh.connect(hostname, 22, username, pkey=paramiko.rsakey.RSAKey.from_private_key_file(key_path))
ssh.scp = SCPClient(ssh.get_transport())
stdin, stdout, stderr = ssh.exec_command("ls -al")
print("stdout: " + format(stdout.read().decode().strip()))
print("stderr: " + format(stderr.read().decode().strip()))
ssh.close()
