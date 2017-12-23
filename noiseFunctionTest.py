#!/usr/bin/env python2.7
'''
    File name: noiseFucntionTest.py
    Author: Pierre Vachon
    Date created: 11/18/2017
    Date last modified: 12/23/2017
    Python Version: 2.7-3.6
    Version 3.0
'''

# One single test of random noise generator from key example. 

# Assume user's key

key = [True, False, True
       , True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, True, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, True, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, True, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, True, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, True, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, True, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, True, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True]
tempkey = [False, False, False, False, False, False, False]
value = 0
counter = 0
keylength = len(key)
tablelength = 31
testvector1 = [0] * tablelength

test2 = [0] * 31 * 31
temptest2value = 0



for i in range (1, 500000):
	tempkey[0] = key[counter]
	tempkey[1] = key[(counter+1)%keylength]
	tempkey[2] = key[(counter+2)%keylength]
	tempkey[3] = key[(counter+3)%keylength]
	tempkey[4] = key[(counter+4)%keylength]
	tempkey[5] = key[(counter+5)%keylength]

	#bit flip
	key[(counter+5)%keylength] = (key[(counter+5)%keylength] != 1)
	tempkey[6] = key[(counter+6)%keylength]

	#swap values
	key[counter] = tempkey[4]
	key[(counter+4)%keylength] = tempkey[0]
	counter = (counter + 7)%keylength
	jump = 64 * tempkey[0] + 32 * tempkey[1] + 16 * tempkey[2] + 8 * tempkey[3] + 4 * tempkey[4] + 2 * tempkey[5] + 1 * tempkey[6]
	temptest2value = value	
	value = (value + jump)%tablelength
	testvector1 [value] = testvector1[value] + 1
	test2[temptest2value * 31 + value] = test2[temptest2value * 31 + value] + 1
