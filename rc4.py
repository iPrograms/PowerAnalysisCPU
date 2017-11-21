#!/usr/bin/env python2.7
'''
    File name: rc4.py
    Author: Manzoor Ahmed 
          : Pierre Vachon
    Date created: 10/20/2017
    Date last modified: 11/15/2017
    Python Version: 2.7-3.6
    Version 2.0
'''

import os
import sys
import psutil as ps
import binascii
import psutil
import base64
import time
from args import InputChecker
from stats import CPUStat, MemoryStat, HardDriveStat
from numpy import arange
from matplotlib.pyplot import figure,show

# Current process
proc = psutil.Process(os.getpid())

cpustate = CPUStat()
percpu = False
sysInfo = False

# Memory
memstate = MemoryStat()

# Hard Drive
drive = HardDriveStat()

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

cpu.set_xlim(0,6600)
key.set_xlim(0,256)

# Show grid 
cpu.grid(True)
key.grid(True)


# Labels
cpu.set_ylabel('Percentage')
cpu.set_xlabel('Time')
cpu.set_title('CPU, Memory, Hard Drive')

key.set_ylabel('Value')
key.set_xlabel('Round')
key.set_title('S, Key, T')


# Start monitoring cpu usage of this process
# Start monitoring memory usage of this process
# Start monitoring hard drive access

def collectSystemData():
        # Capture cpu usage
        cpustate.addCPUInterval(proc.cpu_percent(interval=0.01) / psutil.cpu_count())
        print(proc.cpu_percent(interval=0.01) / psutil.cpu_count())
        # Capture mem usage
        memstate.collectMemoryData(proc.memory_percent())
        
        # Capture drive access TODO
        psutil.disk_io_counters(perdisk=False).read_count

        # Capture other info if required...

# Populate S with data 0,...256
def initializeStateVector(s,k,monitor=False):
        t = []
        # Need to capture system information
        if monitor == True:
                for i in range(0,256):
                        collectSystemData()
                        s.append(i)
                        # Collect Sys data
                        collectSystemData()
                        # Expand key to the same lenth as S
                        t.append(int(k[i % len(k) ]))
                        # Collect Sys data
                        collectSystemData()              
        else:
                for i in range(0,256):
                        s.append(i)
                        # Expand key to the same lenth as S
                        t.append(int(k[i % len(k) ]))                
        return t

# Swap S data for permutaion
def swap(i,j,monitor=False):

        if monitor == False:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
        else:
                # We are collected data after each operation below
                collectSystemData()
                temp = s[i]
                collectSystemData()
                s[i] = s[j]
                collectSystemData()
                s[j] = temp
        
def initPermutationOfS(s,monitor=False):
        j=0
        if monitor == True:
                collectSystemData()
                for x in range(0,256):
                    collectSystemData()    
                    j = ( j + int(s[j]) + int(t[j]) ) % 256
                    collectSystemData()
                    swap(s[x],s[j])
                    collectSystemData()
        else:
                for x in range(0,256):
                    j = ( j + int(s[j]) + int(t[j]) ) % 256
                    # swap also monitors sys info internaly
                    swap(s[x],s[j],sysInfo)

# Encrypt M byte of data with stream key
def encrypt(data,key, monitor=False):

        if monitor == True:
                # Capture each operation power usage
                collectSystemData()
                data_to_int = int(data,16)
                collectSystemData()
                xor = data_to_int ^ int(key)
                collectSystemData()
                encrypted_hex = hex(xor)
                collectSystemData()
                encrypt_hex = binascii.hexlify(encrypted_hex)
                collectSystemData()
        else:
                data_to_int = int(data,16)
                xor = data_to_int ^ int(key)
                encrypted_hex = hex(xor)
                encrypt_hex = binascii.hexlify(encrypted_hex)
        return encrypted_hex

# Decrypt
def decrypt(data,key, monitor=False):

        if monitor == False:
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
        else:
                # key
                collectSystemData()
                dec_val = int(data,16) ^ int(key)
                collectSystemData()
                to_hex = hex(dec_val)

                # Don't need to monitor, not part of algorithm
                try:
                        if to_hex.endswith('L'):
                                original_val = binascii.unhexlify(to_hex[2:len(to_hex) -1 ].strip())
                        else:
                                original_val = binascii.unhexlify(to_hex[2:])
                except binascii.Error as be:
                        print('data error!', be)
                except binascii.Incomplete as bi:
                        print('incomplete data error!', bi)
                
        return original_val

# Open data stream from file, or any other type of data
def streamData(command,key,streamData,sysInfo):
        if sysInfo == False:
                if(command == '-e') or ( command == '-E'):
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
                                                encrpted_chunk = encrypt(chunk,round_key,sysInfo)
                                                # Change file extension
                                                file_with_ext = streamData +  '.encrypted'
                                                
                                                # Append data
                                                with open(file_with_ext, 'ab+' ) as bf:
                                                        bf.write(encrpted_chunk)
                                                        bf.close()
                        f.close()
                        
                elif (command == '-d') or (command == '-D'):
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
                                                decrypt_chunk = decrypt(data,round_key,sysInfo)
                                                
                                                # Change file extension
                                                file_with_ext = streamData
                                        
                                                # Get pathname
                                                abspath = os.path.abspath(file_with_ext)
                                                
                                                basename = os.path.basename(file_with_ext)
                                                copy = abspath.replace(basename,'') + 'Copy_' + basename.replace('.encrypted','')
                                                
                                                newpath = copy
                                                
                                                # Append data
                                                with open(newpath, 'ab+' ) as bf:
                                                        bf.write(decrypt_chunk)
                                                        bf.close()
                        fe.close()
                else:
                        print('unknown command! Did you want to use with -e or -E option?')
                        
        # User to monitor sys resources
        else:
                if(command == '-e') or ( command == '-E'):
                        with open(streamData,'rb') as f:
                                a = 0
                                b = 0 
                                f.seek(0)
                                collectSystemData()
                                while True:
                                        # Extract a block of 8 bytes from streamData to encrpt
                                        collectSystemData()
                                        byte = f.read(8)
                                        collectSystemData()
                                        chunk = binascii.hexlify(byte)
                                        if not chunk:
                                                break
                                        else:
                                                # Keep generating key
                                                collectSystemData()
                                                a = ( a + 1 ) % 256
                                                collectSystemData()
                                                b = ( b + s[b] )  % 256
                                                collectSystemData()
                                                swap( s[ a ], s[ b ])
                                                collectSystemData()
                                                te = ( s[ a ] + s[ b ] ) % 256
                                                collectSystemData()

                                                # Encryption key
                                                round_key = s[te]
                                                collectSystemData()
                                                
                                                encrpted_chunk = encrypt(chunk,round_key,sysInfo)
                                                collectSystemData()
                                                # Change file extension
                                                file_with_ext = streamData +  '.encrypted'
                                                
                                                # Append data
                                                with open(file_with_ext, 'ab+' ) as bf:
                                                        collectSystemData()
                                                        bf.write(encrpted_chunk)
                                                        collectSystemData()
                                                        bf.close()
                        f.close()
                        
                elif (command == '-d') or (command == '-D'):
                        with open(streamData,'rb') as fe:
                                a = 0
                                b = 0
                                fe.seek(0)
                                collectSystemData()
                                while True:
                                        # Extract a block of 18 bytes from streamData to decrypt
                                        collectSystemData()
                                        data = fe.read(18)
                                        if not data:
                                                break
                                        else:
                                                # Keep generating key
                                                collectSystemData()
                                                a = ( a + 1 ) % 256
                                                collectSystemData()
                                                b = ( b + s[b] )  % 256
                                                collectSystemData()
                                                swap( s[ a ], s[ b ])
                                                collectSystemData()
                                                te = ( s[ a ] + s[ b ] ) % 256
                                                collectSystemData()

                                                # Decryption key
                                                round_key = s[te]
                                                collectSystemData()

                                                decrypt_chunk = decrypt(data,round_key,sysInfo)
                                                collectSystemData()
                                                # Change file extension
                                                file_with_ext = streamData
                                                # Get pathname
                                                abspath = os.path.abspath(file_with_ext)
                                                basename = os.path.basename(file_with_ext)
                                                copy = abspath.replace(basename,'') + 'Copy_' + basename.replace('.encrypted','')
                                                newpath = copy
                                                # Append data
                                                with open(newpath, 'ab+' ) as bf:
                                                        collectSystemData()
                                                        bf.write(decrypt_chunk)
                                                        collectSystemData()
                                                        bf.close()
                        fe.close()
                else:
                        print('unknown command! Did you want to use with -e or -E option?')
                
       
# Validate input first                
inpch = InputChecker()

if inpch.processCommand(sys.argv) == True:

        # Are we monitoring system info?
        if len(sys.argv) == 7:
                sysInfo = True

        k = sys.argv[3]
        s = []

        print ('Initializing S...')
        
        a = len(cpustate.getCPUdata())
        t = initializeStateVector(s,k,sysInfo)
        
        #plotOriginalS(s)
        key.plot(s,'-b', label='S')
        print 'Permuting S...'

        b = len(cpustate.getCPUdata()) - a
        initPermutationOfS(s,sysInfo)
        c = len(cpustate.getCPUdata()) - b
        
        key.plot(s,'-g', label='Permuted S or T')
        key.plot(t,'-r', label='Expanded Key')
        
        stream = sys.argv[5]
        command = sys.argv[2]
       
        # File to encrypt, needs abosolute path with extension
        print ('Main operation..')

        d = len(cpustate.getCPUdata()) - c
        streamData(sys.argv[1],sys.argv[2],sys.argv[5],sysInfo)
        e = len(cpustate.getCPUdata()) - d
        
        #plotCPUData(cpustate.getCPUtimeData(),cpustate.getCPUdata())
        
        cpu.plot(cpustate.getCPUdata(), '-r',label='Actual CPU')
        cpu.plot(memstate.getCollectedMemData(), label='Memory')

        cpu.legend(loc='upper right')
        key.legend(loc='upper right')
        
 
        print ('cpu',cpustate.getCPUdata())
        print ('time:', len(cpustate.getCPUdata()))
        print ('mem',memstate.getCollectedMemData())

        # Mark operation locations
        
        cpu.annotate('Init S', xy=(0, 1), xytext=(0, 2),
            arrowprops=dict(facecolor='black', shrink=0.01),
            )
        #cpu.annotate('End S', xy=(a, 1), xytext=(a+5, 2),
        #    arrowprops=dict(facecolor='black', shrink=0.01),
        #    )
        cpu.annotate('Start Permutaiton', xy=(b, 1), xytext=(b+5, 2),
            arrowprops=dict(facecolor='black', shrink=0.01),
            )
        cpu.annotate('End Permutation', xy=(c, 1), xytext=(c+5, 2),
            arrowprops=dict(facecolor='black', shrink=0.01),
            )
        cpu.annotate('Main Operations', xy=(d, 1), xytext=(d+5, 2),
            arrowprops=dict(facecolor='black', shrink=0.01),
            )
        cpu.annotate('End RC4', xy=(e, 1), xytext=(e+5, 2),
            arrowprops=dict(facecolor='black', shrink=0.01),
            )
  
        

        show()
