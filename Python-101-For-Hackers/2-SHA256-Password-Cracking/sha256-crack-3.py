# Modified script
# -w for custom wordlist

from pwn import *
import sys

COLOUR = '\033[93m'
RESET = '\033[0m'
wordlist = "/usr/share/wordlists/rockyou.txt"
user_hash = sys.argv[1]

# Get argument as hash
if len(sys.argv) < 2:
	print(f"Usage: {sys.argv[0]} <sha256-hash>")
	exit()

with log.progress(f"Attempting to crack {user_hash}") as p:
	with open(wordlist, "r", encoding='latin-1') as plist:
		for password in plist:
			password = password.strip("\n").encode('latin-1')
			password_hash = sha256sumhex(password)
			p.status(f"Trying '{password.decode('latin-1')}'")

			if user_hash == password_hash:
				print("Password found!")
				print(COLOUR + f"{password_hash} : {password.decode('latin-1')}" + RESET)
				exit()

		p.failure("Failed")


