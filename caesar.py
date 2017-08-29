#!/usr/bin/env python
# this will solve a caesar cipher with the corresponding shift number
# uses python built ins ord and char to convert ascii text to ordinal number then subtracts shifted number from ordinal 
import sys

class Caesar(object):
    ''' The Caesar class which will give the options to encrypt or decrypt the
    chosen shift # '''
    
    def __init__(self):
        return

    def encrypt(self, msg, shift_amt):

        self.msg = str(msg)
        self.shift_amt = shift_amt
        msg_length = len(msg)

        ord_msg_list = []
        
        for letter in msg:
            ord_msg_list.append(ord(letter))

        add_shift_list = []
        
        for ordinal in ord_msg_list:
            add_shift_list.append(chr(ordinal + shift_amt))
        return "".join([str(x) for x in add_shift_list])
        
    def decrypt(self, msg, shift_amt):
        
        self.msg =str(msg)
        self.shift_amt = shift_amt
        msg_length = len(msg)

        ord_msg_list = []

        for letter in msg:
            ord_msg_list.append(ord(letter))

        subtract_shift_list = []

        for ordinal in ord_msg_list:
            subtract_shift_list.append(chr(ordinal - shift_amt))
        return "".join([str(x) for x in subtract_shift_list])



caesar = Caesar()

# TESTS
print('encryption test 1: ' + caesar.encrypt('testing', 5))
print('encryption test 2: ' + caesar.encrypt('blahblahblah', 13))
print('encryption test 3: ' + caesar.encrypt('helloworld', 3)) 

print '\n' 

print('decryption test 1: ' + caesar.decrypt('yjxynsl', 5))
print('decryption test 2: ' + caesar.decrypt('oynuoynuoynu', 13))
print('decryption test 3: ' + caesar.decrypt('khoorzruog', 3))
