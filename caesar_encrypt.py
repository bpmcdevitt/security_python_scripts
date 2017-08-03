#!/usr/bin/env python
# this will solve a caesar cipher with the corresponding shift number
# uses python built ins ord and char to convert ascii text to ordinal number then subtracts shifted number from ordinal 
import sys

msg = str(sys.argv[1])
msg_length = len(msg)
shift_amt = int(sys.argv[2])

def get_ord(msg):

    ord_msg_list = []

    for letter in msg:
        ord_msg_list.append(ord(letter))
    return ord_msg_list

def add_shift(shift_amt):
    
    add_shift_list = []

    for ordinal in get_ord(msg):
      add_shift_list.append(chr(ordinal + shift_amt))
    return add_shift_list

print(*add_shift(shift_amt), sep='', end='\n', flush=True)
