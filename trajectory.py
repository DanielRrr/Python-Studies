from math import *

v0 = float(input('Введите начальную скорость: '))
theta = radians(float(input('Введите градус направления полета: ')))
x = float(input('Введите координату: '))
y0 = float(input('Позиция объекта: '))
g = 9.81

y = x*tan(theta)-1/(2*v0**2)*(g*x**2)/(cos(theta)**2)+y0
print('Траектория объекта %g m.' %y)
