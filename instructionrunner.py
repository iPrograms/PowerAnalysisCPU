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
        return 10 + 20000000

    # Subtract 10 from noise value
    def subtract(self,noisevalue):
        return  10 * 10

    # noisevalue squared
    def power2(self, noisevalue):
        return 2** 2

    # cubbed value of noise
    def power3(self, noisevalue):
        return 3** 3

    # noisevlaue to the 4th power
    def power4(self, noisevalue):
        return 4**4

    # noisevalue raised to self
    def multipSelf(self, noisevalue):
        return 9999 ** 3
    
    def quad(self,noisevalue):
        return 34 + 2 * 4

    def equationOne(self,noisevalue):
        return noisevalue * 2 - 1
    
    def equationTwo(self,noisevalue):
        return 100 * 3 - 1
    
    def equationThree(self,noisevalue):
        return  4 **4 -1 % 10
    
    def equationFour(self, noisevalue):
        return  3 * 2 **100
    
    def equationFive(self,noisevalue):
        return 20 **2 % 10
    
    def equationSix(self,noisevalue):
        return 20 ** 3 % 10
    
    def equationSeven(self, noisevalue):
        return 19001019 * 4 % 10 + 3
    
    def equationEight(self,noisevalue):
        return noisevalue
    
    def equationNine(self,noisevalue):
        return 987654321 * 2 + 1 / 3
    
    def equationTen(self,noisevalue):
        return 2 + 90 * 6 / 2
    
    def equation11(self, noisevalue):
        return 9929 + 8 % 4

    def equation12(self, noisevalue):
        return 5 % 10

    def equation13(self, noisevalue):
        return 9 % 2

    def equation14(self, noisevalue):
        return 14

    def equation15(self, noisevalue):
        return 3 % 8 * 100

    def equation16(self , noisevalue):
        return  900 * 2 + 10 * 2
    
    def equation17(self, noisevalue):
        return 2 + 7 * 90 - 12
    
    def equation18(self, noisevalue):
        return 300 + 20 - 2 * 9
    
    def equation19(self, noisevalue):
        return 5 **3 / 100 + 3
    
    def equation20(self, noisevalue):
        return 111 + 1 % 8 * 200
    
    def equation21(self, noisevalue):
        return noisevalue + 1 * 4 % 7

    def equation22(self, noisevalue):
        return 200
    
    def equation23(self, noisevalue):
        return 2 * 3 - 90 ** 5
    
    def equation24(self, noisevalue):
        return (2 ** 3 % 16 ) + 9 **2 

    def equation25(self, noisevalue):
        return 9 / 23

    def equation26(self, noisevalue):
        return 100 / 33 % 12

    def equation27(self, noisevalue):
        return 33333333 / 12 % 3

    def equation28(self,noisevalue):
        return 9999999999999 + 1 % 7 * 12

    def equation29(self, noisevalue):
        return noisevalue + 3 % 23

    def equation30(self, noisevalue):
        return 10 ** 4 % 4
    
    def equation31(self, noisevalue):
        return 20 + 77 / 12 % 9
    

    
