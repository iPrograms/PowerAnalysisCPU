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

    def arevalidArgs(self):
        if ( self.validArgs == True ) and ( self.validKey == True) and ( self.extension == True):
            return True
        else:
            return False
    
    def printUsage(self):
        print'+----------------------------------------------+'
        print''
        print' rc4.py   General Commands Manual'
        print''
        print' NAME'
        print' rc4.py'
        print''
        print' Usage: rc4.py [-eEdD][-k][-f file]'
        print''
        print' Optional arguments:'
        print' -h, --help  show this help message and exit'
        print' -sys, --sytem monitor system resources'
        print' -n,--noise monitor system resources with added noise'
        print''
        print'+-----------------------------------------------+'

    def checkKey(self,k):
        if k.isdigit() and len(k) >8:
            return True
        else:
            return False
        
    def processCommand(self, args):
        valid = False
        if len(args) == 1:
            print('No arguments supplied!')
            
        elif len(args) == 2:
            if args[1] != "":
                if  ( args[1] == '-h' )  or ( args[1] == '--help' ):
                    self.printUsage()
                elif args[1] == '-e' or args[1] == '-E':
                    self.command = 'encrypt'
                    print(self.command)
                elif args[1] == '-d' or args[1] == '-D':
                    self.command = 'decrypt'
                    print(self.command)
        elif len(args) == 3:
            if ( args[2] == '-k' )  or ( args[2] == '--key' ) :
                print(args[2])
            else:
                print 'Usage: did you want to run with -k option?'
                self.printUsage()
        elif len(args) == 4:
            if (args[3]) != "":
                if self.checkKey(args[3]) == True:
                    self.validKey = True
                    print(args[3])
                else:
                    print 'Invalid Key'
        elif len(args) == 5:
            if args[4] != "":
                if ( args[4] == '-f' ) or ( args[4]  == '--file' ):
                    print self.argv[4]
                else:
                    print 'No Stream data provided!'
        elif len(args) == 6:
            if ((args[4] == '-f') or (args[4] == '--file')) and (self.checkKey(args[3]) == True)  and \
               ((args[2] == '-k' )  or ( args[2] == '--key')) and ((args[1] == '-e' or args[1] == '-E') or  (args[1] == '-d' or args[1] == '-D')):
                if(args[5] != ""):
                   if args[5].find(".") > 0:
                      self.extension = True
                      self.validArgs = True
                      print 'valid command'
                      return True
                   else:
                      print 'Invalid extension'
            else:
                print 'invalid command'
        # -sys, -system        
        elif len(args) == 7:
            if ((args[4] == '-f') or (args[4] == '--file')) and (self.checkKey(args[3]) == True)  and \
               ((args[2] == '-k' )  or ( args[2] == '--key')) and ((args[1] == '-e' or args[1] == '-E') or  (args[1] == '-d' or args[1] == '-D')):
                if(args[5] != ""):
                   if args[5].find(".") > 0:
                      self.extension = True
                      if (args[6] != ""):
                          if(args[6] == '-sys') or (args[6]) == '--system':
                              self.validArgs = True
                              print 'monitoring system resources, cpu.'
                              return True
                          else:
                              print 'Invalid argument -> ' + args[6]
                   else:
                      print 'Invalid extension'
        # -n noise       
        elif len(args) == 8:
            if ((args[4] == '-f') or (args[4] == '-file')) and (self.checkKey(args[3]) == True)  and \
               ((args[2] == '-k' )  or ( args[2] == '--key')) and ((args[1] == '-e' or args[1] == '-E') or  (args[1] == '-d' or args[1] == '-D')):
                if(args[5] != ""):
                   if args[5].find(".") > 0:
                      self.extension = True
                      if (args[6] != ""):
                          if(args[6] == '-sys') or (args[6]) == '--system':
                              if(args[7] !=""):
                                  if(args[7] == '-n') or (args[7] == '--noise'):
                                      self.validArgs = True
                                      print 'monitoring systemd resources with noise'
                                      self.validArgs = True
                                      return True
                              else:
                                  print 'Invalid argument -> ' + args[7]
                   else:
                      print 'Invalid extension'
        
        else:
            print 'Unknown args found!'
    
        
   
