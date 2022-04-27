import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

dots = int(input('Введите количество точек в разбиении: '))
type = int(input('Способ выбора оснащения (0 - слева, 1 - по центру, 2 - справа): '))
s = 0

y = lambda x:(3**x) # задаём график показательной функции
x = np.linspace(-1, 0, 1000)


def plotSum(n, t):
    global s
    weight = 1 / n # ширина каждого из прямоугольников
    for i in range(n):
        if t == 0:
            height = 3**(i/n-1)
        elif t == 1:
            height = 3**((2*i+1)/(2*n)-1)
        elif t == 2:
            height = 3**((i+1)/n-1)
        rect = patches.Rectangle((i / n - 1, 0), weight, height, linestyle="-.", edgecolor='black', fill=None,
                                 linewidth=1.5) # создаём объект прямоугольника
        s += weight*height
        plt.gca().add_patch(rect) # рисуем его
        plt.gca().set_axisbelow(True)


plotSum(dots, type)

# настройка конечного вида графика и прямоугольников под ним
plt.plot(x, y(x), label='y=3^x') # плот показательной функции
plt.legend()
plt.grid() # cетка
plt.title('График зависимости y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.show() # показываем сам график

print("Значение суммы:", "%.8f" % s)
print("Погрешность:", "%.10f" % (2/(3*np.log(3)) - s)))
