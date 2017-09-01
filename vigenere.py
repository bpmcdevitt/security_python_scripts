#!/usr/bin/env python
# implementation of the vigenere cipher

class Vigenere(object):
    ''' The Vigenere cipher, options are to encrypt/decrypt '''
    
    def __init__(self):
        self.alphakeys = dict(
