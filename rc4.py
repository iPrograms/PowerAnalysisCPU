
import os
import binascii
import sys

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

        data_to_int = int(data,16)

        xor = data_to_int ^ key

        encrypted_hex = hex(xor)

        # Write hex value to file 
        writeToFile(filename, encrypted_hex,'enc')

# Write M byte of data to file
def writeToFile(file,data,enc):

        # Encrypt 
        if enc == 'enc':
        
                # Change file extension
                file_with_ext = file + '.encrypted'

                #print(file_with_ext)
                # Open if exists, otherwise create new
                with open(file_with_ext, 'w+') as ef:
                        ef.write(data)
                ef.close()

        # Decrypt
        if enc == 'dec':
                file_with_original_ext = file.replace('.encrypted','')
                print(file_with_original_ext)


# Open data stream from file, or any other type of data
def getStreamData(streamData):

        try:
                with open(streamData,"rb") as file:
        
                        a = 0
                        b = 0 

                        while True:

                                # Extract a block of 8 bytes from streamData to encrpt

                                chunk = binascii.hexlify(file.read(8))

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
 
                                encrypt(chunk,round_key,file.name)

                        # Double check encrypted file exists
                        with open(file.name + '.encrypted','rb') as encrypted_f:
                                if encrypted_f:
                                        print('Done hacker!')
                                        print('Encrypted content -> ', encrypted_f.name)
                        encrypted_f.close()
                        
                        
        except IOError as e:
                print('I/O Error!')
        except ValueError as va:
                print('Could not convert data')
        except:
                print('Unknown Error')
                raise

                                                 
initializeStateVector()
print()
print()

initPermutationOfS()
print()
print()

# file to encrypt, needs abosolute path with extension

getStreamData('/Users/user/Desktop/n.odt')

        
    


