#!/usr/bin/env python
# python script using the atbash cipher
import sys

# make dict with ciphertext values

reversed_xyz = {'A': 'Z','B':'Y','C':'X','D':'W', 'E':'V', 'F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N','N':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A'}


def encrypt_msg(msg):
    msg = msg.upper()
    msg_l = []
    encrypt_l = []
    for letter in msg:
        msg_l.append(letter)
    for i in range(len(msg_l)):
       if msg_l[i] in reversed_xyz:
            encrypt_l.append(reversed_xyz[msg_l[i]])
    print "".join([str(x) for x in encrypt_l])

def decrypt_msg(msg):
    msg = msg.upper()
    msg_l = []
    decrypt_l = []
    for letter in msg:
        msg_l.append(letter)
    for i in range(len(msg_l)):
        if msg_l[i] in reversed_xyz.viewvalues():
            decrypt_l.append(reversed_xyz[msg_l[i]])
    print "".join([str(x) for x in decrypt_l])

encrypt_msg('TEST')
decrypt_msg('GVHG')
