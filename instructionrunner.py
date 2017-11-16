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

    # Add more...



    



    # End 


# Testing...
# Creat InstructionRunner 
instrunner = InstructionRunner()

# Call power with noisevalue 4
print(instrunner.power2(4))

    
