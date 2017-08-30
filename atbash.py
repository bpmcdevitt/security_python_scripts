#!/usr/bin/env python
# python script using the atbash cipher
import sys

# make dict with ciphertext values

class Atbash(object):
    ''' The atbash cipher implementation. ability to encrypt/decrypt using this
    cipher '''

    def __init__(self):
        self.reversed_xyz = {'A': 'Z','B':'Y','C':'X','D':'W', 'E':'V', 'F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N','N':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A'}


    def encrypt(self, msg):
        msg = msg.upper()
        msg_l = []
        encrypt_l = []
        for letter in msg:
            msg_l.append(letter)
        for i in range(len(msg_l)):
            if msg_l[i] in self.reversed_xyz:
                encrypt_l.append(self.reversed_xyz[msg_l[i]])
        return "".join([str(x) for x in encrypt_l])

    def decrypt(self, msg):
        msg = msg.upper()
        msg_l = []
        decrypt_l = []
        for letter in msg:
            msg_l.append(letter)
        for i in range(len(msg_l)):
            if msg_l[i] in self.reversed_xyz.viewvalues():
                decrypt_l.append(self.reversed_xyz[msg_l[i]])
        return "".join([str(x) for x in decrypt_l])

atbash = Atbash()


# TESTS
print(atbash.encrypt('TEST'))
print(atbash.decrypt('GVHG'))
