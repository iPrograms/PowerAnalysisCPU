#!/usr/bin/env python2.7
'''
    File name: NoiseGenerator.py
    Author: Manzoor Ahmed 
          : Pierre Vachon
    Date created: 11/18/2017
    Date last modified: 11/28/2017
    Python Version: 2.7-3.6
    Version 2.0
'''

from instructionrunner import InstructionRunner
import hashlib

class NoiseGenerator:

    def __init__(self,userkey):
        self.counter =0
        self.userkey = bin(int(userkey,16)).replace('0b','')
        self.hasheduserkey = bin(int(hashlib.sha256(str(userkey).encode('utf-8')).hexdigest(),16)).replace('0b','')
        self.hasheduserkey = list(map(int,self.hasheduserkey))
        self.userkey = list(map(int,self.userkey))
        self.tempkey = [0,0,0,0,0,0,0]
        self.value = 0
        self.generatedvalues = []
        self.noiseEnd = 500
        self.prev = 0
        self.flipindex = 0
        self.swapindex = 0

        self.start =0
        self.end = self.start + 7
        self.jumpinsttablesize = 32

        self.jumpinstructions = InstructionRunner()

    def runjumpinstruction(self,value):
        finalnoisevalue = 0
        if value == 0:
            finalnoisevalue = self.jumpinstructions.add(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 1:
            finalnoisevalue = self.jumpinstructions.subtract(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 2:
            finalnoisevalue = self.jumpinstructions.power2(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 3:
            finalnoisevalue = self.jumpinstructions.power3(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 4:
            finalnoisevalue = self.jumpinstructions.power4(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 5:
            finalnoisevalue = self.jumpinstructions.multipSelf(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 6:
            finalnoisevalue = self.jumpinstructions.quad(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 7:
            finalnoisevalue = self.jumpinstructions.equationOne(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 8:
            finalnoisevalue = self.jumpinstructions.equationTwo(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 9:
            finalnoisevalue = self.jumpinstructions.equationThree(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 10:
            finalnoisevalue = self.jumpinstructions.equationFour(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 11:
            finalnoisevalue = self.jumpinstructions.equationFive(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 12:
            finalnoisevalue = self.jumpinstructions.equationSix(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 13:
            finalnoisevalue = self.jumpinstructions.equationSeven(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 14:
            finalnoisevalue = self.jumpinstructions.equationEight(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 15:
            finalnoisevalue = self.jumpinstructions.equationNine(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 16:
            finalnoisevalue = self.jumpinstructions.equationTen(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 17:
            finalnoisevalue = self.jumpinstructions.equation11(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 18:
            finalnoisevalue = self.jumpinstructions.equation12(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 19:
            finalnoisevalue = self.jumpinstructions.equation14(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 20:
            finalnoisevalue = self.jumpinstructions.equation15(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 21:
            finalnoisevalue = self.jumpinstructions.equation16(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 22:
            finalnoisevalue = self.jumpinstructions.equation17(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 23:
            finalnoisevalue = self.jumpinstructions.equation18(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 24:
            finalnoisevalue = self.jumpinstructions.equation19(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 25:
            finalnoisevalue = self.jumpinstructions.equation20(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 26:
            finalnoisevalue = self.jumpinstructions.equation21(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 27:
            finalnoisevalue = self.jumpinstructions.equation22(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 28:
            finalnoisevalue = self.jumpinstructions.equation23(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 29:
            finalnoisevalue = self.jumpinstructions.equation24(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 30:
            finalnoisevalue = self.jumpinstructions.equation25(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value == 32:
            finalnoisevalue = self.jumpinstructions.equation26(value)
            self.generatedvalues.append(finalnoisevalue)
        return finalnoisevalue

    def swapbits(self,start):
        
        # swap bit number 4 and 0
        tmp = self.hasheduserkey[ start ]
        self.hasheduserkey[ start ]  = self.hasheduserkey[ start + 3 ]
        self.hasheduserkey[ start + 3 ]  = tmp
        self.swapindex = self.swapindex + 7

    def flipbits(self,start):
        # flip bit 5
        if self.hasheduserkey[ start + 4 ] == 1:
	   self.hasheduserkey[ start + 4 ] =  0
	   self.flipindex = self.flipindex + 7
		
	elif self.hasheduserkey[ start + 4 ] == 0:
            self.hasheduserkey[ start  + 4 ] =  1
            self.flipindex = self.flipindex + 7
    
    def nextvalue(self):
        bits = ''
        # Don't go over
        if (self.start + 7 > len(self.hasheduserkey)) or (self.end + 7 > len(self.hasheduserkey)):                                                         
            self.start = self.start + 7 % len(self.hasheduserkey)
            self.end   = self.end + 7   % len(self.hasheduserkey)

            # Grab 7 bits 
            for x in range(self.start,self.end):
                bits = bits + str(self.hasheduserkey[x % len(self.hasheduserkey)])

            if self.swapindex + 3 >= len(self.hasheduserkey):
                self.swapindex = 0
            if self.flipindex + 4 >= len(self.hasheduserkey):
                self.flipindex = 0

            # flip and swap bits for next use
            self.swapbits(self.swapindex)
            self.flipbits(self.flipindex)
                
        else:
            for x in range(self.start,self.end):
                bits = bits + str(self.hasheduserkey[x])

            if self.swapindex + 3 >= len(self.hasheduserkey):
                self.swapindex = 0
            if self.flipindex + 4 >= len(self.hasheduserkey):
                self.flipindex = 0
                
            # flip and swap bits for next use
            self.swapbits(self.swapindex)
            self.flipbits(self.flipindex)
                
            self.start = self.start + 7
            self.end   = self.end + 7
            
        return int(bits,2)
    
    def generateNoise(self):
        for x in range(1,self.noiseEnd):
            self.tempkey[0] = self.userkey[self.counter]
            (self.userkey[self.counter]) = ((self.userkey[self.counter]) != 1)
            self.tempkey[1] = self.userkey[ (( self.counter + 1) % 32) ]
            self.tempkey[2] = self.userkey[ (self.counter +2 ) % 32 ]
            (self.userkey[ (self.counter+2 ) %32 ]) = ((self.userkey[(self.counter+2) %32])!= 1)
            self.tempkey[3] = self.userkey[(self.counter+3)%32]
            self.tempkey[4] = self.userkey[(self.counter+4)%32]
            self.tempkey[5] = self.userkey[(self.counter+5)%32]
            (self.userkey[(self.counter+5)%32]) = ((self.userkey[(self.counter+5)%32]) != 1)
            self.tempkey[6] = self.userkey[(self.counter+6)%32]
            
            self.counter = (self.counter + 7 ) % len(self.userkey)
    
            jump = 64 * self.tempkey[0] + 32 * self.tempkey[1] + 16 * self.tempkey[2] + 8 * self.tempkey[3] + 4 * self.tempkey[4] + 2 * self.tempkey[5] + 1 * self.tempkey[6]
     
            value = (self.value + jump) % 31

        hashedkey7bits = self.nextvalue()
            
        noise = self.runjumpinstruction( hashedkey7bits % self.jumpinsttablesize)
        finalnoise = noise + self.prev
        self.prev = finalnoise  
        
        return finalnoise
             
    def getNoiseValues(self):
        return self.generatedvalues


