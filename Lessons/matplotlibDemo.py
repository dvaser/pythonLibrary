import matplotlib.pyplot as plt
import numpy

# x = [i for i in range(1,5)]
# y = [i**2 for i in x]

# plt.plot(x,y, "|")

"""
'-'
'--'
'-.'
':'
'o'
'^'
'v'
'<'
'>'
'*'
's' #square
'|'
'h' #hexagon
'd' #diamond
'x'
'b'
'r'
'g'
"""

"""
# plt.axis([0,6,0,20])

plt.title("Grafik")
plt.xlabel("x label")
plt.ylabel("y label")

x = np.linspace(0,2,100)    # dizi olusturma

plt.plot(x, x, label="linear", color="red")   # grafikte 1.cizgi
plt.plot(x, x**2, label="quadratic", color="yellow")
plt.plot(x, x**3, label="cubic", color="green")
# 3 adet cizgi tek grafikte

plt.title("Grafik")
plt.legend()  # harita bilgi kutusu (legend)

fig, axs = plt.subplots(3)  # 3 adet grafik tek figurde

axs[0].plot(x,x, color="red")
axs[0].set_title("linear")

axs[1].plot(x,x**2, color="orange")
axs[1].set_title("quadratic")

axs[2].plot(x,x**3, color="green")
axs[2].set_title("cubic")

plt.legend()
plt.tight_layout()  # cikitlarin birbiri uzerine gecmesini engelliyo



x = np.linspace(0,2,100)

fig, axs = plt.subplots(2,2)  # 3 adet grafik tek figurde
fig.suptitle("Grafik")

axs[0,0].plot(x,x, color="red")
axs[0,1].plot(x,x**2, color="green")
axs[1,0].plot(x,x**3, color="yellow")
axs[1,1].plot(x,x**4, color="blue")
"""

yil = [2001,2002,2003,2004,2005]
oyuncu1= [8,10,12,7,9]
oyuncu2= [7,12,5,15,21]
oyuncu3= [18,20,22,25,19]

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors=['y','r','b'], labels=['oyuncu1','oyuncu2', 'oyuncu3'])
plt.legend(loc=2)
plt.show()

"""
goal_types = ['Penalti', 'Kaleye Atilan Sut', 'Serbest Vurus']
goals = [12,35,7]
colors = ['y','r','b']

plt.pie(goals, labels=goal_types, colors=colors, shadow=True, explode=(0.05,0.05,0.05), autopct="%1.1f%%")
plt.show()
"""

"""
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW", width=.5, color='r')
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="AUDI", width=.5, color='b')

plt.legend(loc=4)
plt.show()
"""

"""
yaslar = [20,40,45,12,13,84,74,95,14,23,56,22,43,51,50,30,21,61,51,23,45,47,85,95,74,47,14,12,10,5,9,7,61,45,13,72]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90]

plt.hist(yaslar, yas_gruplari, histtype="bar")

plt.show()
"""