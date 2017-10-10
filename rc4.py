
import os

# Initialization vector [0,1,...256]
s = []

# Private key to initialy permute initialization vector S
k = '12139757927403241289018348180751234973456123041823903030394848210389384746819101838437128191'


t = []

def initializeStateVector():
        for i in range(0,256):
                s.append(i)
                
                # Expand key to the same lenth as S
                t.append(int(k[i % len(k) ]))
        print('S: ',s)

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

def encrypt(data,key):

        print('** ', type(data))
        print('-->',type(key))


        # Chagne to int
        #decode = data.decode('utf-8')
        #decode = int(decode)

        #zor = bin( decode ^ key )
        
        #print('data', decode, '^', key , '->', zor)
            
def getStreamData(streamData):

        try:
                with open(streamData,"rb") as file:
        
                        a = 0
                        b = 0 

                        while True:


                                # Extract a block of 1 byte from streamData to encrpt

                                chunk = file.read(1)

                                if not chunk:
                                        break
                                        
                                a = ( a + 1 ) % 256
                                b = ( b + s[b] )  % 256
                                swap( s[ a ], s[ b ])
                                te = ( s[ a ] + s[ b ] ) % 256
                                round_key = s[te]

                                print('Stream Key:  > ',bytes([ round_key ]) )

                                # Encrypt chunk with stream key

                                print(encrypt(chunk,bytes([round_key])))
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

getStreamData('/Users/user/Desktop/Screen Shot 2017-10-09 at 8.00.20 PM.png')

        
    


