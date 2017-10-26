'''
    File name: rc4.py
    Author: Manzoor Ahmed 
          : Pierre Vachon
    Date created: 10/10/2017
    Date last modified: 10/10/2017
    Python Version: 3.6
    Version 1.0
'''

import os
import io
import binascii
import sys
import psutil
import base64

# Initialization vector [0,1,...256]
s = []

# Private key to initialy permute initialization vector S
k = '12139757927403241289018348180751234973456123041823903030394848210389384746819101838437128191'

t = []

# Populate S with data 0,...256
def initializeStateVector():
        for i in range(0,256):
                s.append(i)
                # Expand key to the same lenth as S
                t.append(int(k[i % len(k) ]))
        print('S: ',s)

# Swap S data for permutaion
def swap(i,j):
	temp = s[i]
	s[i] = s[j]
	s[j] = temp

def initPermutationOfS():
        j=0
        
        for x in range(0,256):
            j = ( j + int(s[j]) + int(t[j]) ) % 256
            swap(s[x],s[j])
            
        print('Permuted S: ',s)

# Encrypt M byte of data with stream key
def encrypt(data,key):

        
        data_to_int = int(data,16)
        xor = data_to_int ^ key
        
        encrypted_hex = hex(xor)
        print ('encode',encrypted_hex.encode())
        
        print(encrypted_hex)
        return encrypted_hex


# Decrypt
def decrypt(data,key):

        data_to_int = int(data.strip(),16)
        xor = data_to_int ^ key
        
        print('xored value', xor)
        to_hex = hex(xor)
        
        print('to_hex', to_hex)
        
        decrypted = binascii.unhexlify(to_hex.strip())
        
        print ('decrypted value:', decrypted)

        return binascii.unhexlify(str(to_hex)[2:])
                    
# Open data stream from file, or any other type of data
def streamData(streamData,command):

        if command is 'encrypt':
                with open(streamData,'rb') as f:
                        a = 0
                        b = 0 

                        while True:

                                # Extract a block of 8 bytes from streamData to encrpt
                                byte = f.read(8)
                                print('data',byte)
                                chunk = binascii.hexlify(byte)                
                                if not chunk:
                                        break
                                else:
                                        # Keep generating key 
                                        a = ( a + 1 ) % 256
                                        b = ( b + s[b] )  % 256
                                        swap( s[ a ], s[ b ])
                                        te = ( s[ a ] + s[ b ] ) % 256

                                        # Encryption key
                                        round_key = s[te]
                                        print(round_key)

                                        # Encrypt chunk with stream key
                                        print ('encrypting...')
                                        encrpted_chunk = encrypt(chunk,round_key)
                                        # Change file extension
                                        file_with_ext = streamData + '.encrypted'
                                        # Append data
                                        with open(file_with_ext, 'ab+' ) as bf:
                                                bf.write(encrpted_chunk)
                                                bf.close()
                f.close()
                
        if command is 'decrypt':
                with open(streamData,'rb') as fe:
                        a = 0
                        b = 0 
                        while True:
                                # Extract a block of 18 bytes from streamData to decrypt
                                data = fe.read(18)
                                if not data:
                                        break
                                else:
                                        # Keep generating key
                                       
                                        a = ( a + 1 ) % 256
                                        b = ( b + s[b] )  % 256
                                        swap( s[ a ], s[ b ])
                                        te = ( s[ a ] + s[ b ] ) % 256

                                        # Decryption key
                                        round_key = s[te]

                                        print(round_key)

                                        # Decrypt chunk with stream key
                                        #print ('dencrypting...')
                                        decrypt_chunk = decrypt(data,round_key)
                                        print(decrypt_chunk)
                                        # Change file extension
                                        file_with_ext = streamData
                                        # Append data
                                        #with open(file_with_ext, 'wb+' ) as bf:
                                                #bf.write(decrypt_chunk)
                                                #bf.close()

                fe.close()        
initializeStateVector()
initPermutationOfS()

# File to encrypt, needs abosolute path with extension
streamData('/Users/user/Desktop/BITS.py','encrypt')

s =[]
t = []
initializeStateVector()
initPermutationOfS()

streamData('/Users/user/Desktop/BITS.py.encrypted','decrypt')


        
    


