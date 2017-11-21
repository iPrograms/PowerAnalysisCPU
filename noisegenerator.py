#!/usr/bin/env python2.7
'''
    File name: NoiseGenerator.py
    Author: Manzoor Ahmed 
          : Pierre Vachon
    Date created: 11/18/2017
    Date last modified: 11/19/2017
    Python Version: 2.7-3.6
    Version 1.0
'''
from instructionrunner import InstructionRunner

class NoiseGenerator:

    def __init__(self,userkey, end):
        self.counter =0
        self.userkey = bin(userkey).replace('0b','')
        self.userkey = list(map(int,self.userkey))
        print(self.userkey)
        self.end = end
        self.tempkey = [0,0,0,0,0,0,0]
        self.value = 0
        self.generatedvalues = []

        self.jumpinstructions = InstructionRunner()

    def runjumpinstruction(self,value):
        finalnoisevalue = 0
        if value == 0:
            finalnoisevalue = self.jumpinstructions.add(value)
        if value == 1:
            finalnoisevalue = self.jumpinstructions.subtract(value)
        if value == 2:
            finalnoisevalue = self.jumpinstructions.power2(value)
        if value == 3:
            finalnoisevalue = self.jumpinstructions.power3(value)
        if value == 4:
            finalnoisevalue = self.jumpinstructions.power4(value)
        if value == 5:
            finalnoisevalue = self.jumpinstructions.multipSelf(value)
        if value == 6:
            finalnoisevalue = self.jumpinstructions.quad(value)
        if value >= 6 and value <= 10 :
            finalnoisevalue = self.jumpinstructions.equationOne(value)
        if value >= 11 and value <= 20:
            finalnoisevalue = self.jumpinstructions.equationTwo(value)
        if value >= 21 and value <= 30:
            finalnoisevalue = self.jumpinstructions.equationThree(value)
        if value >= 31 and value <= 40:
            finalnoisevalue = self.jumpinstructions.equationFour(value)
        if value >= 41 and value <= 50:
            finalnoisevalue = self.jumpinstructions.equationFive(value)
        if value >= 51 and value <= 60:
            finalnoisevalue = self.jumpinstructions.equationSix(value)
        if value >= 61 and value <= 70:
            finalnoisevalue = self.jumpinstructions.equationSeveb(value)
        if value >= 71 and value <= 80:
            finalnoisevalue = self.jumpinstructions.equationEight(value)
        if value >= 81 and value <= 90:
            finalnoisevalue = self.jumpinstructions.equationNine(value)
        if value >= 91 and value <= 100:
            finalnoisevalue = self.jumpinstructions.equationTen(value)
        if value >= 101 and value <= 110:
            finalnoisevalue = self.jumpinstructions.equation11(value)
        if value >= 111 and value <= 120:
            finalnoisevalue = self.jumpinstructions.equation12(value)
        if value >= 121 and value <= 130:
            finalnoisevalue = self.jumpinstructions.equation13(value)
                
        return finalnoisevalue
    
    def generateNoise(self):
        for x in range(1,self.end):
            self.tempkey[0] = self.userkey[self.counter]
            print (self.tempkey[0])
            (self.userkey[self.counter]) = ((self.userkey[self.counter]) != 1)
            self.tempkey[1] = self.userkey[ (( self.counter + 1) % 32) ]
            self.tempkey[2] = self.userkey[ (self.counter +2 ) % 32 ]
            (self.userkey[ (self.counter+2 ) %32 ]) = ((self.userkey[(self.counter+2) %32])!= 1)
            self.tempkey[3] = self.userkey[(self.counter+3)%32]
            self.tempkey[4] = self.userkey[(self.counter+4)%32]
            self.tempkey[5] = self.userkey[(self.counter+5)%32]
            (self.userkey[(self.counter+5)%32]) = ((self.userkey[(self.counter+5)%32]) != 1)
            self.tempkey[6] = self.userkey[(self.counter+6)%32]

            #self.counter = (self.counter + 7 )%32 --> Wil not work if key is smaller than 32
            # Fix, check key size
            self.counter = (self.counter + 7 ) % len(self.userkey)
            # if multip of 7 
            jump = 64 * self.tempkey[0] + 32 * self.tempkey[1] + 16 * self.tempkey[2] + 8 * self.tempkey[3] + 4 * self.tempkey[4] + 2 * self.tempkey[5] + 1 * self.tempkey[6]
    
            # We know where to jump, so call runjumpinstruction, ie if jump is 0 we run noise.runjumpinstruction(0) returning 10
            # jumpvalue = runjumpinstruction(jump)
            #
            # value is the final noisevalue? that is the value after jump instruction + value?
            # % 31 should be number of jump instructions
            
            value = (self.value + jump) % 31 # why 31

            finalnoise = self.runjumpinstruction(value)

            # store final noise values
            self.generatedvalues.append(finalnoise) 
            
    def getNoiseValues(self):
        return self.generatedvalues

noise = NoiseGenerator(1348499902910288282828,200)
noise.generateNoise()
print (noise.getNoiseValues())
print (noise.runjumpinstruction(130))
