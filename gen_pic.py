import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
#from pylab import *

filepath = '/nvme/nnUNetFrame/DATASET/nnUNet_raw/nnUNet_raw_data/Task506_Oct/infer/summary.json'

dice =


dice1 = b[:,0]
dice2 = b[:,1]
dice3 = b[:,2]

fig = plt.figure(figsize=(30, 24))
# names = ['5', '10', '15', '20', '25']
x = range(1037)
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#plt.xlim(0, 650)  # 限定横轴的范围
plt.ylim(0, 1)  # 限定纵轴的范围
x_major_locator=MultipleLocator(100)
#把x轴的刻度间隔设置为1，并存在变量里
ax=plt.gca()
#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数

plt.xlim(-0.5,1000)
#把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白

plt.plot(x, dice1, mec='r', mfc='w',label=u'图')
plt.plot(x, dice2, ms=10,label=u'图')
plt.plot(x, dice3, ms=10,label=u'图')
plt.legend()  # 让图例生效
plt.xticks(x, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
#plt.xlabel(u"time(s)邻居") #X轴标签
plt.ylabel("DICE") #Y轴标签
plt.title("dices") #标题

plt.show()

