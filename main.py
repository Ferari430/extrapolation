import csv
import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
coord = []
press = []
left_grid = []
right_grid = []
left_press = []
right_press = []
with open('B:\MPEI\Programming\interpolation\p500000.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        coord.append(float(row[0]))
        press.append(float(row[1]))
grid = []
with open('B:\MPEI\CFD\coordsofgrid.csv', newline='') as File1:
    reader1 = csv.reader(File1)
    for each in reader1:
        grid.append(int(each[0])/1000) ## in mm

print(f'Растояния дистанционирующих решеток {grid}')

for i in range(0,len(grid),2):
    left_grid.append(grid[i])

for i in range(1,len(grid),2):
    right_grid.append(grid[i])
print(f'Левые стенки ДР {left_grid}')
print(f'Правые стенки ДР{right_grid}')

for i in range(len(left_grid)):
    left_press.append(left_grid[i] - 0.01)
    right_press.append(right_grid[i] + 0.01)

for i in range(len(left_grid)):
    plt.axvline(x = left_grid[i], color = 'red')
    plt.axvline(x = right_grid[i], color = 'black')
print(f'Точки перед ДР {left_press}')
print(f'Точки за ДР {right_press}')

## Добавление точек +- 10мм c давлением
with open('B:\MPEI\CFD\ppp.csv', newline='') as File:
    reader = list(csv.reader(File))
coord1 = []
press1 = []
for i in range(0,len(reader[0]),2):
    coord1.append(float(reader[0][i]))
for i in range(1, len(reader[0]), 2):
        press1.append(float(reader[0][i]))
coord1.sort()
press1.sort()
press1 = press1[::-1]
# print(f'Координаты точек на расстоянии +- 10мм от ДР {coord1}')
# print(f'Давление в точках на расстоянии +- 10мм от ДР{press1}')

# for i in range(len(press1)):
#     press.append(press1[i])
#     coord.append(coord1[i])
#
plt.scatter(coord,press)
# plt.scatter(coord1,press1, c = 'red')

###############################################################################
# Поиск точек по границам
edge_left = [1.94,2.011] # поиск точек по левой границе от ДР
edge_right = [2.11, 2.192] # поиск точек по правой границе от ДР
pressure_left = [] # давление в найденных точках слева от ДР
pressure_right = [] # давление в найденных точках справа от ДР
coord_left = [] # точные координаты точек слева от ДР
coord_right = [] # точные координаты точек справа от ДР
# координаты ищем в массиве coord
# Поиск точек для экстраполяции для левой стороны
linear_extra_coords_left = []
linear_extra_press_left = []

for i in range(len(coord)):
    if coord[i] > edge_left[0] and coord[i] < edge_left[1]:
        print('Найдены точки по левой стороне')
        linear_extra_coords_left.append(coord[i])
        linear_extra_press_left.append(press[i])
        coord_left.append(coord[i])
        pressure_left.append(press[i])
print(f'coord_left = {coord_left}')
print(f'pressure_left = {pressure_left}')
plt.scatter(coord_left,pressure_left, color ='r')
# Поиск точек для экстраполяции для правой стороны
linear_extra_coords_right = []
linear_extra_press_right = []

for i in range(len(coord)):
    if coord[i] > edge_right[0] and coord[i] < edge_right[1]:
        print('Найдены точки по правой стороне')
        linear_extra_coords_right.append(coord[i])
        linear_extra_press_right.append(press[i])
        coord_right.append(coord[i])
        pressure_right.append(press[i])
plt.scatter(coord_right,pressure_right, color ='r')
print(f'coord_right = {coord_right}')
print(f'pressure_right = {pressure_right}')

# starting extrapolation. Нужно указать длину экстраполирующей кривой. Создаем массив через np c маленьким шагом
# LEFT
s_left = interpolate.InterpolatedUnivariateSpline(coord_left,pressure_left)
extra_coord_left = np.arange(2.0256,2.066,0.0001)
extra_press_left = s_left(extra_coord_left)
plt.plot(extra_coord_left,extra_press_left, '--')

# Linear extrapolation
linear_s_left = np.poly1d(np.polyfit(linear_extra_coords_left, linear_extra_press_left,deg=1))
xx1 = np.linspace(1.94,2.065,1000)
yy1 = linear_s_left(xx1)
plt.plot(xx1,yy1)




# RIGHT
s_right = interpolate.InterpolatedUnivariateSpline(coord_right,pressure_right)
extra_coord_right = np.arange(2.065,2.183,0.0001)
extra_press_right = s_right(extra_coord_right)
plt.plot(extra_coord_right,extra_press_right, '--')
# Поиск вертикальной прямой. Необходимо знать положение центра ДР
grid_cente = 2.065
grid_cente_plot = [grid_cente,grid_cente]
delta = 0.00001
left_index_of_cener = 0
right_index_of_cener = 0

linear_s_right = np.poly1d(np.polyfit(linear_extra_coords_right, linear_extra_press_right,deg=1))
xx2 = np.linspace(2.065,2.183,1000)
yy2 = linear_s_right(xx2)
plt.plot(xx2,yy2)
plt.scatter(xx1[-1],yy1[-1], color = 'green')
plt.scatter(xx2[0],yy2[0], color = 'green')

vert = [extra_press_left[left_index_of_cener], extra_press_right[right_index_of_cener]]
plt.plot(grid_cente_plot,vert)

pressureold = extra_press_left[left_index_of_cener] - extra_press_right[right_index_of_cener]
pressure_linear = yy1[-1] - yy2[0]
print(f'Перепад давления на ДР№7  =  {pressureold}')
print(f'Перепа давления на ДР№7 при линейной экстраполяции = {pressure_linear}')

plt.show()


