
'''
    File name: stats.py
    Monitors cpu usgage of process, memory usage, and hard drive access
    Author: Manzoor Ahmed 
          : Pierre Vachon
    Date created: 10/26/2017
    Date last modified: 10/26/2017
    Python Version: 3.6
    Version 1.0
'''

from matplotlib.pyplot import figure, show
from numpy import arange
import psutil as ps
import os


# CPU Statistics
class CPUStat:

    def __init__(self):
        self.cpu = []
        self.time = []
        self.pointColor = []
    
    def addCPUInterval(self,val):
        self.cpu.append(val)

    def addTimeInterval(self,t):
        self.time.append(t)

    def setPointColor(self,color):
        self.pointColor.append(color)
    
    def getCPUdata(self):
        return self.cpu

    def getCPUtimeData(self):
        return self.time

    def getPointColors(self):
        return self.pointColors
    
    def getColorOfPoint(self,index):
        return self.pointColor[index]


# Memory Statistics
class MemoryStat:

    def __init__(self):
        self.memmoryData = []
        self.time = []
        
    def collectMemoryData(self,data):
        self.memmoryData.append(data)

    def collectTimerData(self,time):
        self.time.append(time)

    def getCollectedMemData(self):
        return self.memmoryData

    def getCollectedTime(self):
        return self.time

# Hard Drive access Statistics
class HardDriveStat:

    def __init__(self):
            self.access = []
            self.time = []
    def addAccess(self,data):
        self.access.append(data)

    def addAccessTime(self,time):
        self.time.append(time)

    def getaccess(self):
        return self.access

    def getAccessTime(self):
        return self.time

