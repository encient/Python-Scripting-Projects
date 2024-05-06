# Instructor script

from pwn import *
import sys

# Check number of arguments
if len(sys.argv) != 2:
	print("Usage: {} <sha256sum>".format(sys.argv[0]))
	exit()

# Get the input hash and wordlist
user_hash_input = sys.argv[1]
password_file = "/usr/share/wordlists/rockyou.txt"
attempts = 0

# Crack the hash
with log.progress("Attempting to crack {}!\n".format(user_hash_input)) as p:
	with open(password_file, "r", encoding='latin-1') as password_list:
		for password in password_list:
			password = password.strip("\n").encode('latin-1')
			password_hash = sha256sumhex(password)
			p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))
			if password_hash == user_hash_input:
				p.success("Password hash found after {} attempts! '{}' hashes to {}!".format(attempts, password.decode('latin-1'), password_hash))
				exit()	
			attempts += 1
		p.failure("Hash not found!")
