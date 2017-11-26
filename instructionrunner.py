#!/usr/bin/env python2.7
'''
    File name: InstructionRunner.py
    Author: Manzoor Ahmed 
          : Pierre Vachon
    Date created: 11/15/2017
    Date last modified: 11/15/2017
    Python Version: 2.7-3.6
    Version 1.0
'''

#InstructionRunner: Runs the following instructions at a given time

class InstructionRunner:

    # Add 10 with a noise value
    def add(self, noisevalue):
        return 10 + noisevalue

    # Subtract 10 from noise value
    def subtract(self,noisevalue):
        return noisevalue - 10

    # noisevalue squared
    def power2(self, noisevalue):
        return noisevalue ** 2

    # cubbed value of noise
    def power3(self, noisevalue):
        return noisevalue ** 3

    # noisevlaue to the 4th power
    def power4(self, noisevalue):
        return noisevalue **4

    # noisevalue raised to self
    def multipSelf(self, noisevalue):
        return noisevalue ** noisevalue
    
    def quad(self,noisevalue):
        return noisevalue + 2 * 4

    def equationOne(self,noisevalue):
        return noisevalue * 2 - 1
    
    def equationTwo(self,noisevalue):
        return noisevalue * 3 - 1
    
    def equationThree(self,noisevalue):
        return noisevalue * 4 -1 % 10
    
    def equationFour(self, noisevalue):
        return noisevalue + 3 * 2
    
    def equationFive(self,noisevalue):
        return noisevalue **2 % 10
    
    def equationSix(self,noisevalue):
        return noisevalue ** 3 % 10
    
    def equationSeven(self, noisevalue):
        return noisevalue **4 % 10 + 3
    
    def equationEight(self,noisevalue):
        return noisevalue
    
    def equationNine(self,noisevalue):
        return noisevalue * 2 + 1 / 3
    
    def equationTen(self,noisevalue):
        return noisevalue * 6 / 2
    
    def equation11(self, noisevalue):
        return noisevalue + 8 % 4

    def equation12(self, noisevalue):
        return noisevalue  ** 5 % 10

    def equation13(self, noisevalue):
        return noisevalue + 9 % 2

    def equation14(self, noisevalue):
        return 14

    def equation15(self, noisevalue):
        return noisevalue * 3 % 8

    def equation16(self, noisevalue):
        return noisevalue ** 10 - noisevalue * 2
    
    def equation17(self, noisevalue):
        return noisevalue / 2 + 7 * 90 - 12
    
    def equation18(self, noisevalue):
        return (noisevalue + noisevalue) % 9
    
    def equation19(self, noisevalue):
        return noisevalue **3 / 100 + 3
    
    def equation20(self, noisevalue):
        return noisevalue + 1 % 8
    
    def equation21(self, noisevalue):
        return noisevalue + 1 * 4 % 7

    def equation22(self, noisevalue):
        return noisevalue / 200
    
    def equation23(self, noisevalue):
        return noisevalue * 3 - 90
    
    def equation24(self, noisevalue):
        return noisevalue * (2 ** 3 % 16 ) + 9

    def equation25(self, noisevalue):
        return noisevalue + 9 / 23

    def equation26(self, noisevalue):
        return noisevalue + 100 / 33 % 12

    def equation27(self, noisevalue):
        return noisevalue / 12 % 3

    def equation28(self,noisevalue):
        return noisevalue + 1 % 7 * 12

    def equation29(self, noisevalue):
        return noisevalue + 3 % 23

    def equation30(self, noisevalue):
        return noisevalue ** 4 % 4
    
    def equation31(self, noisevalue):
        return noisevalue + 77 / 12 % 9
    

    
