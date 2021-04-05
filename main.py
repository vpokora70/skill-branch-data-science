import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
#%matplotlib notebook

'''Задание 1
Посчитать значений производной функции:
$y=\cos(x) + 0.05x^3 + \log_2{x^2}$ 
в точке x = 10.

Производная функции y:
$\dot{y}=-\sin(x) + 0.15x^2 +\frac{2x}{{x^2ln2}}$ 
'''
'Функция у задаию 1'
def F(x):
    y = np.cos(x) + 0.005*x**3 + np.log2(2)
    return y
'Производная функция у задаию 1'
def DF(x):
    y = -1*np.sin(x) + 0.15*x**2 + (2*x)/(x**2*np.log(2))
    return y

''' Производные функции к заданию 2'''
#функция частноой производной по x1
def dif_x1(x1, x2):
    pr_dif_x1 = 2*x1*np.cos(x2)+9*x1**2*np.log2(x2**2)
    return pr_dif_x1
#функция частноой производной по x2
def dif_x2(x1, x2):
    pr_dif_x2 = -1*x1**2*np.sin(x2)+0.15*x2**2+(6*x1**3*x2)/(x2**2*np.log(2))
    return pr_dif_x2

''' Занаие 3 Найти точку минимуму для функции  𝑌=cos(𝑥)+0.05𝑥3+log2𝑥2 .'''

def F3(x):
    #Оригинальная функция
    func_y = np.cos(x) + 0.05*(x**3)+ np.log2(x**2)
    return func_y
def DF3(x):
    #Производная йункции F3
    dif_y= -1*np.sin(x)+0.15*(x**2)+(2*x)/(x**2*np.log(2))
    return dif_y

''' Задание 4 
найти точку минимуму для функции  𝑥21cos(𝑥2)+0.05𝑥32+3𝑥31log2𝑥22 . 
Зафиксировать параметр  𝜖=0.001 , начальные значения весов принять равным [4, 10].
'''
def F4(x1, x2):
    f4= x1**2*np.cos(x2)+0.005*x2**3+3*x1**3*np.log2(x2**2)
    return f4

#функция частноой производной по x1
def Dif4_x1(x1, x2):
    pr_dif4_x1 = 2*x1*np.cos(x2)+9*x1**2*np.log2(x2**2)
    return pr_dif4_x1
#функция частноой производной по x2
def Dif4_x2(x1, x2):
    pr_dif4_x2 = -1*x1**2*np.sin(x2)+0.15*x2**2+(6*x1**3*x2)/(x2**2*np.log(2))
    return pr_dif4_x2

x = 10
print("Задание 1")
print('Значение функции F(x) в точке 10:', F(x))
print('Значение значенеи производной функции DF(x) в точке 10:', DF(x))

# x_ar = np.linspace(0.01, 30, 1000)
# y_ar = list(map(F, x_ar))
#
# x_ar = np.linspace(0.01, 30, 1000)
# y_ar = list(map(F, x_ar))
#
# plt.figure(figsize=(5,5))
# plt.plot(x_ar, y_ar,'--', color='red')
# plt.ylabel("Y")
# plt.xlabel("X")
# plt.scatter([x], [F(x)], lw=3)
# plt.show()

'''Задание 2
Посчитать значение градиента функции $x_1^2\cos(x_2) + 0.05x_2^3 + 3x_1^3\log_2{x_2^2}$ в точке $(10, 1)$'''



in_x1= 10
in_x2 = 1
print('Задание 2 Посчитать значение градиента функции  10, 1')
print('Значение частная  производная Z по x1: ', dif_x1(in_x1, in_x2))
print('Значение частная производная Z по x2: ', dif_x2(in_x1, in_x2))


'Задание 3'

n = 2000 # число итераций
xn = 10 #Начальное значение
eps = 0.001 #шаг сходимости 0.1, 0.2, 0.9, 1

#Рисуем график функции
x_plt = np.arange(-10, 10.0, 0.1)
f_plt = [F3(x) for x in x_plt]

plt.ion() # включаем интерактивный режим отображения графиков
fig, ax = plt.subplots() # Создаем окна и осей для графика
ax.grid(True) #Отображение сетки на графике
ax.plot(x_plt, f_plt, '--', color='green') # отображение графика фунукиции на интервале x_plt
point = ax.scatter(xn, F3(xn), c ='red') #Отображение точки красным цветом

# программируем алгоритм
mn = 300  # ограничим значение знаменателя нормирующего коефициента)

for i in range(n):
    eps = 1 / min(i + 1, mn)  # проведем нормиарование градиента
    # xn= xn - eps*DF3(xn) #изменение аргумента на текущей итерации
    xn = xn - eps * np.sign(DF3(xn))  # изменение аргумента на текущей итерации
    point.set_offsets([xn, F3(xn)])  # Отображение нового положения точки

    # Перерисовка графика и задержка на 20нс
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.001)

plt.ioff() # Выключение интерактивного режима отображения графиков
print('Задание 3.')
print('Функция достигаем минимум в точке x:',xn)
ax.scatter(xn, F3(xn), c='blue')
plt.show()
print('i=', i)

#Задание 4

n = 2000  # число итераций по a

in_a = 4  # начальные значения
in_b = 10  # начальные значения
in_aс = 4  # константа
in_bc = 10  # константа
eps = 0.001  # шаг сходимости

print('Задание 4')
print('Начальные значения функции Z')
print('Z=', F4(in_a, in_b))
print('Za=', Dif4_x1(in_a, in_bc))
print('Zb=', Dif4_x2(in_aс, in_b))

# программируем алгоритм
mn = 300  # ограничим значение знаменателя нормирующего коефициента

for i in range(n):
    eps = 1 / min(i + 1, mn)  # проведем нормирование градиента
    in_a = in_a - eps * np.sign(Dif4_x1(in_a, in_bc))  # изменение аргумента на текущей итерации
    z_a = Dif4_x1(in_a, in_bc)
    in_b = in_b - eps * np.sign(Dif4_x2(in_aс, in_b))  # изменение аргумента на текущей итерации
    z_b = Dif4_x2(in_aс, in_b)

print('Найденые минимальные значения функции Z')
print('Z=', F4(in_a, in_b), 'in_a=:', in_a, 'in_b=', in_b)
print('z_a=', z_a, 'z_b=', z_b)