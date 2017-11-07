#!/usr/bin/env python2.7

'''
    File name: args.py: process command line argument(s)
    
    Author: Manzoor Ahmed 
          : Pierre Vachon
    Date created: 11/06/2017
    Date last modified: 11/06/2017
    Python Version: 2.7
    Version 1.0
'''
import sys
class InputChecker:
    
    def __init__(self):
        self.argv = sys.argv
        self.validArgs = False
        self.command = None
        self.validKey = False
        self.extension = False
        
    def printUsage(self):
        print'rc4.py   General Commands Manual'
        print''
        print'NAME'
        print'rc4.py'
        print''
        print'usage: rc4.py [-eEdD][-k][-file file]'
        print''
        print'optional arguments:'
        print'-h, --help  show this help message and exit'
        print''

    def checkKey(self,k):
        if k.isdigit():
            return True
        else:
            return False
        
    def processCommand(self):
        valid = False
        if len(self.argv) == 1:
            print('No arguments supplied!')
            
        elif len(self.argv) == 2:
            if self.argv[1] != "":
                if  ( self.argv[1] == '-h' )  or ( self.argv[1] == '--help' ):
                    self.printUsage()
                elif self.argv[1] == '-e' or self.argv[1] == '-E':
                    self.command = 'encrypt'
                    print(self.command)
                elif self.argv[1] == '-d' or self.argv[1] == '-D':
                    self.command = 'decrypt'
                    print(self.command)
        elif len(self.argv) == 3:
            if ( self.argv[2] == '-k' )  or ( self.argv[2] == '--key' ) :
                print(self.argv[2])
            else:
                print 'Usage: did you want to run with -k option?'
                self.printUsage()
        elif len(self.argv) == 4:
            if (self.argv[3]) != "":
                if self.checkKey(self.argv[3]) == True:
                    self.validKey = True
                    print(self.argv[3])
                else:
                    print 'Invalid Key'
        elif len(self.argv) == 5:
            if self.argv[4] != "":
                if ( self.argv[4] == '-f' ) or ( self.argv[4]  == '--file' ):
                    print self.argv[4]
                else:
                    print 'No Stream data provided!'
        elif len(self.argv) == 6:
            if ((self.argv[4] == '-f') or (self.argv[4] == '-file')) and (self.checkKey(self.argv[3]) == True)  and \
               ((self.argv[2] == '-k' )  or ( self.argv[2] == '--key')) and ((self.argv[1] == '-e' or self.argv[1] == '-E') or (self.argv[1] == '-d' or self.argv[1] == '-D')):
                if(self.argv[5] != ""):
                   if self.argv[5].find(".") > 0:
                      self.extension = True
                      self.validArgs = True
                      print 'valid command!'
                      valid = True                      
                   else:
                      print 'Invalid extension'
            else:
                print 'invalid command'
        else:

            print 'Unknown args found!'
            return valid
        
   
