import numpy as np
import matplotlib.pyplot as plt

KGS = [0.497,0.444,0.419,0.405,0.394,0.385,0.378,0.372,0.368,0.364]
Re = [50000,100000,150000,200000,250000,300000,350000,400000,450000,500000]
KGT = [0.024718,0.021217,0.019499,0.018404,0.017617,0.01701,0.016521,0.016114,0.015768,0.015469]
def func(x):
    return 1.0955-0.0562*np.log(x)

def func1(x):
    return 0.06671734-0.0039321*np.log(x)
def ksi(a,b,re):
    return a*re**b
def etta(a,b,re):
    return a*re**b

apr3 = etta(0.22383,-0.20423,np.linspace(50000,550000,1000))
apr2 = ksi(2.1194,-0.13508,np.linspace(50000,550000,1000))


plt.xlabel('Число Рейнольдса Re')
plt.ylabel('Коэффициент гидравлического сопротивления')
apr = func(np.linspace(50000,550000,1000))
plt.title('Зависимость КГС от числа Рейнольдса')
plt.scatter(Re,KGS, label = 'Точки из эксперимента')
plt.plot(np.linspace(50000,550000,1000),apr2, '--')
plt.text(310000,0.46,r'$y = aRe^b$', fontsize=10, bbox={'facecolor':'white','alpha':0.2})
plt.text(310000,0.445,r'$a = 2.1194$', fontsize=10, bbox={'facecolor':'white','alpha':0.2})
plt.text(310000,0.43,r'$b = -0.013508$', fontsize=10, bbox={'facecolor':'white','alpha':0.2})

plt.plot(np.linspace(50000,550000,1000),apr, label = r'$\beta=\alpha^25$')
plt.grid()
plt.legend()
plt.show()

apr1 = func1(np.linspace(50000,550000,1000))
plt.plot(np.linspace(50000,550000,1000), apr1, label = 'Апроксимация логарифмической функцией')
plt.plot(np.linspace(50000,550000,1000),apr3, '--')
plt.scatter(Re,KGT)
plt.title('Зависимость КГТ от числа Рейнольдса')
plt.xlabel('Число Рейнольдса Re')
plt.ylabel('Коэффициент гидравлического трения')
plt.grid()
plt.legend()
plt.show()
