#!/usr/bin/env python2.7
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
import sys
import psutil as ps
import binascii
import psutil
import base64
from args import InputChecker
from stats import CPUStat, MemoryStat, HardDriveStat
from numpy import arange
from matplotlib.pyplot import figure,show


# Argv

inputchecker = InputChecker()

# Graph ticks
time_xy = arange(0.0,256,1.0)

# Graph figure
s_key_figure = figure(1)

# graphs
cpu = s_key_figure.add_subplot(313)
key = s_key_figure.add_subplot(211)

# Y axis 0, to 10
cpu.set_ylim(0,2)
key.set_ylim(0,256)

cpu.set_xlim(0,256)
key.set_xlim(0,256)

# Show grid 
cpu.grid(True)
key.grid(True)


# Labels
cpu.set_ylabel('Time')
cpu.set_xlabel('Value')
cpu.set_title('CPU Usage')


key.set_ylabel('Key')
key.set_xlabel('Round')
key.set_title('Key Generation')


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

def plotKey():
        for x in range(0,256):
                key.plot(x,s[x])
                

# Encrypt M byte of data with stream key
def encrypt(data,key):
        
        data_to_int = int(data,16)
        
        xor = data_to_int ^ int(key)
        
        encrypted_hex = hex(xor)

        encrypt_hex = binascii.hexlify(encrypted_hex)
        
        return encrypted_hex

# Decrypt
def decrypt(data,key):
              
        # key
        dec_val = int(data,16) ^ int(key)

        to_hex = hex(dec_val)

        try:

                if to_hex.endswith('L'):
                        original_val = binascii.unhexlify(to_hex[2:len(to_hex) -1 ].strip())
                        #print('**',original_val)
                else:
                        original_val = binascii.unhexlify(to_hex[2:])

                #print original_val.decode('hex')
        except binascii.Error as be:
                print('data error!', be)
        except binascii.Incomplete as bi:
                print('incomplete data error!', bi)
                
        return original_val

                    
# Open data stream from file, or any other type of data
def streamData(streamData,command):

        if(command is '-e') or ( command is '-E'):
                with open(streamData,'rb') as f:
                        a = 0
                        b = 0 
                        f.seek(0)
                        while True:

                                # Extract a block of 8 bytes from streamData to encrpt
                                byte = f.read(8)
                               
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
                                        #print(round_key)

                                        # Encrypt chunk with stream key
                                        #print ('encrypting...', chunk)
                                        encrpted_chunk = encrypt(chunk,round_key)
                                        # Change file extension
                                        file_with_ext = streamData + '.encrypted'
                                        
                                        # Append data
                                        with open(file_with_ext, 'ab+' ) as bf:
                                                bf.write(encrpted_chunk)
                                                bf.close()
                f.close()
                
        if (command is '-d') or (command is '-D'):
                with open(streamData,'rb') as fe:
                        a = 0
                        b = 0
                        fe.seek(0)
                        while True:
                                # Extract a block of 18 bytes from streamData to decrypt
                                data = fe.read(18)
                                
                                #print('reading dec data',data)
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
                                        
                                        #print(decrypt_chunk)
                                        
                                        # Change file extension
                                        file_with_ext = streamData

                                        # Get pathname
                                        abspath = os.path.dirname(file_with_ext)
                                        basename = os.path.basename(file_with_ext)
                                        copy = '/Copy_' + basename.replace('.encrypted','')

                                        newpath = abspath + copy
                                        print(newpath)
                                        # Append data
                                        with open(newpath, 'ab+' ) as bf:
                                                bf.write(decrypt_chunk)
                                                bf.close()
                fe.close()




if inputchecker.processCommand() == True:
        k = sys.argv[3]
        print(sys.argv[3])
        initializeStateVector()
        initPermutationOfS()

        stream = sys.argv[5]
        command = sys.argv[2]
        

        plotKey()
        # File to encrypt, needs abosolute path with extension
        streamData(sys.argv[5],sys.argv[2])

        show()
        s =[]
        t = []
        initializeStateVector()
        initPermutationOfS()

        streamData('/Users/user/Desktop/lorem.txt.encrypted','decrypt')


'''
if __name__ == "__main__":

    # CPU 
    s = CPUStat()

    # Memory
    m = MemoryStat()

    
    
#x values and ticks
t = arange(0.0, 100.0,1.0)

fig = figure(1)

ax1 = fig.add_subplot(111)

ax1.set_ylim((0,1.5))

ax1.grid(True)

for x in range(0,100):

    # Collect CPU stat
    # percpu = True, if want to collect all cpus data
    process = ps.Process(os.getpid())
    u = process.cpu_percent(interval=True)
    s.addCPUInterval(u)
    s.addTimeInterval(x)

    # Current process' memory usage
    mem = process.memory_percent()
    m.collectMemoryData(mem)
    m.collectTimerData(x)
    print(mem)

    #print(ps.disk_usage('/Users/user/Desktop/CloudDust/graph.py'))
    
print (s.getCPUdata())
print (s.getCPUtimeData())


-	solid line style
--	dashed line style
-.	dash-dot line style
:	dotted line style
.	point marker
,	pixel marker
o	circle marker
v	triangle_down marker
^	triangle_up marker
<	triangle_left marker
>	triangle_right marker
1	tri_down marker
2	tri_up marker
3	tri_left marker
4	tri_right marker
s	square marker
p	pentagon marker
*	star marker
h	hexagon1 marker
H	hexagon2 marker
+	plus marker
x	x marker
D	diamond marker
d	thin_diamond marker
|	vline marker
_	hline marker


# Graph cpu data
ax1.plot(s.getCPUtimeData(),s.getCPUdata(),'-o')

# Graph memory data
ax1.plot(m.getCollectedTime(),m.getCollectedMemData(), '--')


# Labels 
ax1.set_ylabel('Usage')
ax1.set_xlabel('Time')
ax1.set_title('RC4')

#color x labels
for label in ax1.get_xticklabels():
    label.set_color('green')
#color y labels
for label2 in ax1.get_yticklabels():
    label2.set_color('green')



show()'''



