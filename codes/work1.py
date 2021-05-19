import matplotlib.pyplot as plt
import numpy as np #导包
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)#生成一个序列，从0到3π，一共100个点
y = np.sin(x)#依据x序列的值，生成对应sin的y序列
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)#subplot(m,n,i):把图形窗口分为m×n个子图,并在第i个子图中画图
#此处为切成为两个横的子图，在第一个子图中画图
plt.title(r'$f(x)=sin(x)$')#设置第一个子图的title，f(x)=sin(x)
#前缀r或R表示“自然字符串”，使特殊字符失去意义，一般用于转义字符‘/’
#一对‘$’作用是将文本加粗斜体
plt.plot(x, y) #依据x,y在一个子图中画图，第一个参数是横轴，第二个参数是竖轴
x1 = [t*0.375*np.pi for t in x]#依据x序列的值，生成对应3πx/8的x1序列
y1 = np.sin(x1)#依据x1序列的值，生成对应sin的y1序列
plt.subplot(1,2,2)#此处为切成为两个横的子图，在第二个子图中画图
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$')
#设置title，\omega显示w，\frac显示分数，\pi显示π
plt.plot(x1, y1)#依据x1,y1在一个子图中画图
plt.show()#将图显示出来