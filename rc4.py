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
from noisegenerator import NoiseGenerator
from numpy import arange
from matplotlib.pyplot import figure,show


# Current process
proc = psutil.Process(os.getpid())
# private key, degits
print(sys.argv[3])
ng = NoiseGenerator(sys.argv[3])

cpustate = CPUStat()
cpunoise = CPUStat()

percpu = False
sysInfo = False
noise = False

# Memory
memstate = MemoryStat()

# Hard Drive
drive = HardDriveStat()

# Graph ticks
time_xy = arange(0.0,256,1.0)

# Graph figure
s_key_figure = figure(1)

# graphs
key = s_key_figure.add_subplot(411)
cpu = s_key_figure.add_subplot(714)
noisegraph = s_key_figure.add_subplot(414)


# Y axis 0, to 10
cpu.set_ylim(0,2)
key.set_ylim(0,256)

cpu.set_xlim(0,6600)
key.set_xlim(0,256)

# Show grid 
cpu.grid(True)
noisegraph.grid(True)
key.grid(True)


# Labels
cpu.set_ylabel('Percentage')
cpu.set_xlabel('Time (milisecond)')
cpu.set_title('CPU')

noisegraph.set_ylabel('Percentage')
noisegraph.set_xlabel('Time (milisecond)')
noisegraph.set_title('With Noise')

key.set_ylabel('Value')
key.set_xlabel('Round')
key.set_title('S, Key, T')

def collectSystemData():
        # Capture cpu usage
        cpustate.addCPUInterval(proc.cpu_percent(interval=0.01) / psutil.cpu_count())
        
def collectNoiseData():
        # Caputer cpu usage with noise
        cpunoise.addCPUInterval(proc.cpu_percent(interval=0.01) / psutil.cpu_count())
        
# Populate S with data 0,...256
def initializeStateVector(s,k,monitor=False, noise=False):
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
                        
        if (monitor == True) and (noise == True):
                
                for i in range(0,256):
                        ng.generateNoise()
                        collectNoiseData()
                        s.append(i)
                        # Collect Sys data
                        collectNoiseData()
                        # Expand key to the same lenth as S
                        t.append(int(k[i % len(k) ]))
                        # Collect Sys data
                        ng.generateNoise()
                        collectNoiseData()
                        
        else:
                for i in range(0,256):
                        s.append(i)
                        # Expand key to the same lenth as S
                        t.append(int(k[i % len(k) ]))                
        return t

# Swap S data for permutaion
def swap(i,j,monitor=False,noise=False):

        # Regular swapping
        if monitor == False:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
        # Monitoring cpu and noise
        if (monitor == True) and (noise==True):
                ng.generateNoise()
                collectNoiseData()
                temp = s[i]
                ng.generateNoise()
                collectNoiseData()
                s[i] = s[j]
                collectNoiseData()
                s[j] = temp
        # Collect only cpu data
        else:
                # We are collected data after each operation below
                collectSystemData()
                temp = s[i]
                collectSystemData()
                s[i] = s[j]
                collectSystemData()
                s[j] = temp
        
def initPermutationOfS(s,monitor=False,noise=False):
        j=0
        if monitor == True:
                collectSystemData()
                for x in range(0,256):
                    collectSystemData()    
                    j = ( j + int(s[j]) + int(t[j]) ) % 256
                    collectSystemData()
                    swap(s[x],s[j],monitor,noise)
                    collectSystemData()
        if (monitor == True) and (noise == True):
                collectSystemData()
                for x in range(0,256):
                    collectNoiseData()    
                    j = ( j + int(s[j]) + int(t[j]) ) % 256
                    ng.generateNoise()
                    collectNoiseData()
                    swap(s[x],s[j],monitor,noise)
                    collectNoiseData()
        
        else:
                for x in range(0,256):
                    j = ( j + int(s[j]) + int(t[j]) ) % 256
                    # swap also monitors sys info internaly
                    swap(s[x],s[j],sysInfo)

# Encrypt M byte of data with stream key
def encrypt(data,key, monitor=False,noise=False):

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
                
        if (monitor == True) and (noise == True):
                # Capture each operation power usage
                ng.generateNoise()
                collectNoiseData()
                data_to_int = int(data,16)
                collectNoiseData()
                xor = data_to_int ^ int(key)
                ng.generateNoise()
                collectNoiseData()
                encrypted_hex = hex(xor)
                collectNoiseData()
                encrypt_hex = binascii.hexlify(encrypted_hex)
                collectNoiseData()
                
        else:
                data_to_int = int(data,16)
                xor = data_to_int ^ int(key)
                encrypted_hex = hex(xor)
                encrypt_hex = binascii.hexlify(encrypted_hex)
        return encrypted_hex

# Decrypt
def decrypt(data,key, monitor=False,noise=False):

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
                        
        elif (monitor == True) and (noise == True):
                # key
                ng.generateNoise()
                collectNoiseData()
                dec_val = int(data,16) ^ int(key)
                ng.generateNoise()
                collectNoiseData()
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
def streamData(command,key,streamData,sysInfo,noise=False):

        # No monitoring
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
                                                decrypt_chunk = decrypt(data,round_key,sysInfo,noise)
                                                
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
                        
        # CPU and noise monitoring
        elif (sysInfo == True) and (noise == True):
                if(command == '-e') or ( command == '-E'):
                        with open(streamData,'rb') as f:
                                a = 0
                                b = 0 
                                f.seek(0)
                                ng.generateNoise()
                                collectNoiseData()
                                while True:
                                        # Extract a block of 8 bytes from streamData to encrpt
                                        collectNoiseData()
                                        byte = f.read(8)
                                        ng.generateNoise()
                                        collectNoiseData()
                                        chunk = binascii.hexlify(byte)
                                        if not chunk:
                                                break
                                        else:
                                                # Keep generating key
                                                collectNoiseData()
                                                a = ( a + 1 ) % 256
                                                collectSystemData()
                                                b = ( b + s[b] )  % 256
                                                collectNoiseData()
                                                swap( s[ a ], s[ b ],sysInfo, noise)
                                                collectNoiseData()
                                                te = ( s[ a ] + s[ b ] ) % 256
                                                collectNoiseData()

                                                # Encryption key
                                                round_key = s[te]
                                                ng.generateNoise()
                                                collectNoiseData()
                                                
                                                encrpted_chunk = encrypt(chunk,round_key,sysInfo,noise)
                                                collectNoiseData()
                                                # Change file extension
                                                file_with_ext = streamData +  '.encrypted'
                                                
                                                # Append data
                                                with open(file_with_ext, 'ab+' ) as bf:
                                                        collectNoiseData()
                                                        bf.write(encrpted_chunk)
                                                        collectNoiseData()
                                                        bf.close()
                        f.close()
                        
                elif (command == '-d') or (command == '-D'):
                        with open(streamData,'rb') as fe:
                                a = 0
                                b = 0
                                fe.seek(0)
                                collectNoiseData()
                                while True:
                                        # Extract a block of 18 bytes from streamData to decrypt
                                        collectNoiseData()
                                        data = fe.read(18)
                                        ng.generateNoise()
                                        if not data:
                                                break
                                        else:
                                                # Keep generating key
                                                collectNoiseData()
                                                a = ( a + 1 ) % 256
                                                collectNoiseData()
                                                b = ( b + s[b] )  % 256
                                                collectNoiseData()
                                                swap( s[ a ], s[ b ], sysInfo, noise)
                                                collectNoiseData()
                                                ng.generateNoise()
                                                te = ( s[ a ] + s[ b ] ) % 256
                                                collectNoiseData()

                                                # Decryption key
                                                round_key = s[te]
                                                collectNoiseData()

                                                decrypt_chunk = decrypt(data,round_key,sysInfo,noise)
                                                collectNoiseData()
                                                # Change file extension
                                                file_with_ext = streamData
                                                # Get pathname
                                                abspath = os.path.abspath(file_with_ext)
                                                basename = os.path.basename(file_with_ext)
                                                copy = abspath.replace(basename,'') + 'Copy_' + basename.replace('.encrypted','')
                                                newpath = copy
                                                # Append data
                                                with open(newpath, 'ab+' ) as bf:
                                                        collectNoiseData()
                                                        bf.write(decrypt_chunk)
                                                        collectNoiseData()
                                                        bf.close()
                        fe.close()
                else:
                        print('unknown command! Did you want to use with -e or -E option?')
                
        # CPU
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
                                                swap( s[ a ], s[ b ],sysInfo, noise)
                                                collectSystemData()
                                                te = ( s[ a ] + s[ b ] ) % 256
                                                collectSystemData()

                                                # Encryption key
                                                round_key = s[te]
                                                collectSystemData()
                                                
                                                encrpted_chunk = encrypt(chunk,round_key,sysInfo,noise)
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
                                                swap( s[ a ], s[ b ], sysInfo, noise)
                                                collectSystemData()
                                                te = ( s[ a ] + s[ b ] ) % 256
                                                collectSystemData()

                                                # Decryption key
                                                round_key = s[te]
                                                collectSystemData()

                                                decrypt_chunk = decrypt(data,round_key,sysInfo,noise)
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
                print(sys.argv[6])
                
        if len(sys.argv) == 8:
                noise = True
                print(noise)
                print(sys.argv[7])
                
        if (sysInfo == True) and (noise==False):
                k = sys.argv[3]
                s = []

                print ('Initializing S...')
                
                a = len(cpustate.getCPUdata())
                t = initializeStateVector(s,k,sysInfo,noise)
                
                #plotOriginalS(s)
                key.plot(s,'-b', label='S')
                print ('Permuting S...')

                b = len(cpustate.getCPUdata()) - a
                initPermutationOfS(s,sysInfo,noise)
                c = len(cpustate.getCPUdata()) - b
                
                stream = sys.argv[5]
                command = sys.argv[2]
               
                # File to encrypt, needs abosolute path with extension
                print ('Main operation..')

                d = len(cpustate.getCPUdata()) - c

                streamData(sys.argv[1],sys.argv[2],sys.argv[5],sysInfo,noise)

                e = len(cpustate.getCPUdata()) - d
                        
                cpu.plot(cpustate.getCPUdata(), '-r',label='Actual CPU')
                noisegraph.plot(cpunoise.getCPUdata(), '-r',label='With Noise')

                cpu.legend(loc='upper right')
                noisegraph.legend(loc='upper right')
                key.legend(loc='upper right')

                key.plot(s,'-g', label='Permuted S or T')
                key.plot(t,'-r', label='Expanded Key')
                
                # Mark operation locations
                
                cpu.annotate('Init S', xy=(0, 1), xytext=(0, 2),
                    arrowprops=dict(facecolor='black', shrink=0.01),
                    )
                cpu.annotate('Start Permutaiton', xy=(b, 1), xytext=(b+5, 2),
                    arrowprops=dict(facecolor='black', shrink=0.01),
                    )
            
                cpu.annotate('Main Operations', xy=(d, 1), xytext=(d+5, 2),
                    arrowprops=dict(facecolor='black', shrink=0.01),
                    )
                cpu.annotate('End RC4', xy=(len(cpustate.getCPUdata()), 1), xytext=(e+5, 2),
                    arrowprops=dict(facecolor='black', shrink=0.01),
                    )

                print ('cpu',cpustate.getCPUdata())
                print ('time:', len(cpustate.getCPUdata()))

                show()
                
        elif (noise == True) and (sysInfo == True):
              
                k = sys.argv[3]
                s = []

                print ('Initializing S...')
                
                a = len(cpunoise.getCPUdata())
                t = initializeStateVector(s,k,sysInfo,noise)
                
                #plotOriginalS(s)
                key.plot(s,'-b', label='S')
                print ('Permuting S...')

                b = len(cpunoise.getCPUdata()) - a
                initPermutationOfS(s,sysInfo,noise)
                c = len(cpunoise.getCPUdata()) - b
                
                stream = sys.argv[5]
                command = sys.argv[2]
               
                # File to encrypt, needs abosolute path with extension
                print ('Main operation..')

                d = len(cpunoise.getCPUdata()) - c

                streamData(sys.argv[1],sys.argv[2],sys.argv[5],sysInfo,noise)

                e = len(cpunoise.getCPUdata()) - d
                        
                #cpu.plot(cpunoise.getCPUdata(), '-r',label='Actual CPU')
                noisegraph.plot(cpunoise.getCPUdata(), '-b',label='With Noise')

                #cpu.legend(loc='upper right')
                noisegraph.legend(loc='upper right')
                key.legend(loc='upper right')

                key.plot(s,'-g', label='Permuted S or T')
                key.plot(t,'-r', label='Expanded Key')
                
                # Mark operation locations
                
                noisegraph.annotate('Init S', xy=(0, 1), xytext=(0, 2),
                    arrowprops=dict(facecolor='black', shrink=0.01),
                    )
                noisegraph.annotate('Start Permutaiton', xy=(b, 1), xytext=(b+5, 2),
                    arrowprops=dict(facecolor='black', shrink=0.01),
                    )
            
                noisegraph.annotate('Main Operations', xy=(d, 1), xytext=(d+5, 2),
                    arrowprops=dict(facecolor='black', shrink=0.01),
                    )
                noisegraph.annotate('End RC4', xy=(len(cpustate.getCPUdata()), 1), xytext=(e+5, 2),
                    arrowprops=dict(facecolor='black', shrink=0.01),
                    )

                print ('cpu',cpunoise.getCPUdata())
                print ('time:', len(cpunoise.getCPUdata()))

                show()
