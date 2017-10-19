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

if __name__ == "__main__":

    # CPU 
    s = CPUStat()

    # Memory
    m = MemoryStat()

    
    
#x values and ticks
t = arange(0.0, 100.0,1.0)

fig = figure(1)

ax1 = fig.add_subplot(111)

ax1.set_ylim((0,1.5))

ax1.grid(True)

for x in range(0,100):

    # Collect CPU stat
    # percpu = True, if want to collect all cpus data
    process = ps.Process(os.getpid())
    u = process.cpu_percent(interval=True)
    s.addCPUInterval(u)
    s.addTimeInterval(x)

    # Current process' memory usage
    mem = process.memory_percent()
    m.collectMemoryData(mem)
    m.collectTimerData(x)
    print(mem)

    #print(ps.disk_usage('/Users/user/Desktop/CloudDust/graph.py'))
    
print (s.getCPUdata())
print (s.getCPUtimeData())

''''
-	solid line style
--	dashed line style
-.	dash-dot line style
:	dotted line style
.	point marker
,	pixel marker
o	circle marker
v	triangle_down marker
^	triangle_up marker
<	triangle_left marker
>	triangle_right marker
1	tri_down marker
2	tri_up marker
3	tri_left marker
4	tri_right marker
s	square marker
p	pentagon marker
*	star marker
h	hexagon1 marker
H	hexagon2 marker
+	plus marker
x	x marker
D	diamond marker
d	thin_diamond marker
|	vline marker
_	hline marker
'''

# Graph cpu data
ax1.plot(s.getCPUtimeData(),s.getCPUdata(),'-o')

# Graph memory data
ax1.plot(m.getCollectedTime(),m.getCollectedMemData(), '--')


# Labels 
ax1.set_ylabel('Usage')
ax1.set_xlabel('Time')
ax1.set_title('RC4')

#color x labels
for label in ax1.get_xticklabels():
    label.set_color('green')
#color y labels
for label2 in ax1.get_yticklabels():
    label2.set_color('green')



show()
