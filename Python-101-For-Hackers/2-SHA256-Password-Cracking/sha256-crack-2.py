# Follow instructor script

from pwn import *
import sys

if len(sys.argv) != 2:
	print("Usage: {} <sha256-hash>".format(sys.argv[0]))
	exit()

user_hash = sys.argv[1]
wordlist = "/usr/share/wordlists/rockyou.txt"

with log.progress("Attempting to crack {}".format(user_hash)) as p:
	with open(wordlist, "r", encoding='latin-1') as wordlist:
		for word in wordlist:
			word = word.strip("\n").encode('latin-1')
			word_hash = sha256sumhex(word)
			p.status("{} : {}".format(word.decode('latin-1'), word_hash))

			if word_hash == user_hash:
				p.success("Password hash found. \n{}:{}".format(word.decode('latin-1'), word_hash))
				exit()
		p.failure("Hash not found.")