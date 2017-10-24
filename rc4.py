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
def encrypt(data,key,filename):

        data_to_int = int(data)

        xor = data_to_int ^ int(key)

        encrypted_hex = hex(xor)

        # Write hex value to file 
        writeToFile(filename, encrypted_hex,'enc')

# Decrypt
def decrypt(data,key,filename):

        data_to_int = int(data,16)

        xor = data_to_int ^ key

        decrypted_hex = str(xor)

        # Write hex value to file 
        writeToFile(filename, decrypted_hex,'dec')
        

# Write M byte of data to file
def writeToFile(filename,data,command):

        # Encrypt 
        if command== 'enc':
        
                # Change file extension
                file_with_ext = filename + '.encrypted'

                #print(file_with_ext)
                # Open if exists, otherwise create new
                with io.open(file_with_ext, 'wb' ) as ef:
                        ef.write(data)
                        #print bytearray(data)
                ef.close()

        # Decrypt
        if command == 'dec':
                file_with_original_ext = filename.replace('.encrypted','')
                
                try:
                        with io.open(file_with_original_ext, 'wb' ) as ef:
                                ef.write(data.encoding('utf-8'))
                        ef.close()
                except IOError as e:
                        print('I/O Error!')
                except ValueError as va:
                        print('Could not convert dec data data')
                except:
                        print('Unknown Error') 
                
# Open data stream from file, or any other type of data
def encryptStreamData(streamData):
        try:
                with io.open(streamData,"rb") as f:
        
                        a = 0
                        b = 0 

                        while True:

                                # Extract a block of 8 bytes from streamData to encrpt

                                #chunk = binascii.hexlify(f.read(1))
                                chunk = f.read(8)
                                print chunk
                                #chunk = chunk.decode()
                                print chunk
        
                                if not chunk:
                                        break

                                # Keep generating key 
                                a = ( a + 1 ) % 256
                                b = ( b + s[b] )  % 256
                                swap( s[ a ], s[ b ])
                                te = ( s[ a ] + s[ b ] ) % 256

                                # Encryption key
                                round_key = s[te]

                                # Encrypt chunk with stream key
                                print 'starts encrypting...'
                                encrypt(chunk,round_key,f.name)

                        # Done encrypted, clean up

                        #deleteFileContent(streamData)
                        #print 'data deleted, now just a shell!'

                        f.close()
                        
                        try:
                                # Double check encrypted file exists
                                with io.open(f.name + '.encrypted','rb') as encrypted_f:
                                        if encrypted_f:
                                                print('Done hacker!')
                                                print('Encrypted content -> ', encrypted_f.name)
                                        encrypted_f.close()
                                        
                        except IOError as e:
                                print('I/O')
                        except ValueError as ve:
                                print('Value Err')
                                print(sys.exc_info()[0])
                        except:
                                print('Unknown Error!')
                                raise
        
        except IOError as e:
                print('I/O Error!')
        except ValueError as va:
                print('Could not convert enc data')
                print(sys.exc_info()[0])
        except:
                print('Unknown Error')
                raise

def decryptStreamData(streamData):

        try:
                with io.open(streamData,"rb") as f:

                        a = 0
                        b = 0

                        while True:

                                # Extract a block of 1 byte from streamData to encrpt

                                chunk = binascii.hexlify(f.read(1))

                                if not chunk:
                                        break

                                # Keep generating key 
                                a = ( a + 1 ) % 256
                                b = ( b + s[b] )  % 256
                               
                                swap( s[ a ], s[ b ])
                                te = ( s[ a ] + s[ b ] ) % 256

                                # Encryption key
                                round_key = s[te]

                                # Encrypt chunk with stream key

                                decrypt(chunk,round_key,f.name)
                                
                # Done, clsoe file        
                f.close()
                        
        except IOError as e:
                print('I/O Error!')
        except ValueError as va:
                print('Could not convert dect data')
        except:
                print('Unknown Error')
                raise
        
initializeStateVector()
print()
print()

initPermutationOfS()
#initializeStateVector()
print()
print()

# File to encrypt, needs abosolute path with extension
encryptStreamData('/Users/user/Desktop/e.docx')


# File to decrypt, needs absolute path with .encrypted extension
# decryptStreamData('/Users/user/Desktop/e.docx.encrypted')

        
    


