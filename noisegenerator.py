#!/usr/bin/env python2.7
'''
    File name: NoiseGenerator.py
    Author: Manzoor Ahmed 
          : Pierre Vachon
    Date created: 11/18/2017
    Date last modified: 11/26/2017
    Python Version: 2.7-3.6
    Version 2.0
'''
from instructionrunner import InstructionRunner
import hashlib

class NoiseGenerator:

    def __init__(self,userkey):
        self.counter =0
        self.userkey = bin(int(userkey,16)).replace('0b','')
        #hash key and get binary value
        self.hasheduserkey = bin(int(hashlib.sha256(str(userkey).encode('utf-8')).hexdigest(),16)).replace('0b','')
        self.hasheduserkey = list(map(int,self.hasheduserkey))
        self.userkey = list(map(int,self.userkey))
        self.tempkey = [0,0,0,0,0,0,0]
        self.value = 0
        self.generatedvalues = []
        self.noiseEnd = 500 

        self.start =0
        self.end = self.start + 7

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
            
        if value >= 6 and value <= 10 :
            finalnoisevalue = self.jumpinstructions.equationOne(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 11 and value <= 20:
            finalnoisevalue = self.jumpinstructions.equationTwo(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 21 and value <= 30:
            finalnoisevalue = self.jumpinstructions.equationThree(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 31 and value <= 40:
            finalnoisevalue = self.jumpinstructions.equationFour(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 41 and value <= 50:
            finalnoisevalue = self.jumpinstructions.equationFive(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 51 and value <= 60:
            finalnoisevalue = self.jumpinstructions.equationSix(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 61 and value <= 70:
            finalnoisevalue = self.jumpinstructions.equationSeven(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 71 and value <= 80:
            finalnoisevalue = self.jumpinstructions.equationEight(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 81 and value <= 90:
            finalnoisevalue = self.jumpinstructions.equationNine(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 91 and value <= 100:
            finalnoisevalue = self.jumpinstructions.equationTen(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 101 and value <= 110:
            finalnoisevalue = self.jumpinstructions.equation11(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 111 and value <= 120:
            finalnoisevalue = self.jumpinstructions.equation12(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 121 and value <= 130:
            finalnoisevalue = self.jumpinstructions.equation14(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 131 and value <= 140:
            finalnoisevalue = self.jumpinstructions.equation15(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 141 and value <= 150:
            finalnoisevalue = self.jumpinstructions.equation16(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 151 and value <= 160:
            finalnoisevalue = self.jumpinstructions.equation17(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 161 and value <= 170:
            finalnoisevalue = self.jumpinstructions.equation18(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 171 and value <= 180:
            finalnoisevalue = self.jumpinstructions.equation19(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 181 and value <= 190:
            finalnoisevalue = self.jumpinstructions.equation20(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 191 and value <= 200:
            finalnoisevalue = self.jumpinstructions.equation21(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 201 and value <= 400:
            finalnoisevalue = self.jumpinstructions.equation22(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 401 and value <= 600:
            finalnoisevalue = self.jumpinstructions.equation23(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 601 and value <= 800:
            finalnoisevalue = self.jumpinstructions.equation24(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 801 and value <= 1000:
            finalnoisevalue = self.jumpinstructions.equation25(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 1001 and value <= 2000:
            finalnoisevalue = self.jumpinstructions.equation26(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 2001 and value <= 3000:
            finalnoisevalue = self.jumpinstructions.equation27(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 3001 and value <= 4000:
            finalnoisevalue = self.jumpinstructions.equation28(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 4001 and value <= 5000:
            finalnoisevalue = self.jumpinstructions.equation29(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 5001 and value <= 6000:
            finalnoisevalue = self.jumpinstructions.equation30(value)
            self.generatedvalues.append(finalnoisevalue)
            
        if value >= 6001 and value <= 10000:
            finalnoisevalue = self.jumpinstructions.equation31(value)
            self.generatedvalues.append(finalnoisevalue)
        return finalnoisevalue

    def nextvalue(self):
        bits = ''
        if (self.start + 7 > len(self.hasheduserkey)) or (self.end + 7 > len(self.hasheduserkey)):                                                         
            self.start = self.start + 7 % len(self.hasheduserkey)
            self.end   = self.end + 7   % len(self.hasheduserkey)

            for x in range(self.start,self.end):
                bits = bits + str(self.hasheduserkey[x % len(self.hasheduserkey)])
        else:
            for x in range(self.start,self.end):
                bits = bits + str(self.hasheduserkey[x])
            self.start = self.start + 7
            self.end   = self.end + 7
        #print('(s:e:b)',self.start, self.end,bits)

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
            
        finalnoise = self.runjumpinstruction(hashedkey7bits)
                 
        return finalnoise
             
    def getNoiseValues(self):
        return self.generatedvalues
    

#noise = NoiseGenerator(8987777788776667765)
#for x in range(0,30):
#   noise.generateNoise()
#print (noise.getNoiseValues())


