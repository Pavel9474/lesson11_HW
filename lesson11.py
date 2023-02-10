import matplotlib.pyplot as plt
import numpy
import random

# Задача 1. Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.
def task1():
    x=numpy.linspace(-10,10, num=50)
    y=5*x**2+10*x-30
    plt.plot(x,y,color='blue')
    plt.ylim(-40,5)
    plt.grid(color='black', linewidth=1)
    plt.show()
# y отрицательно при x от -3.65 до 1,65

# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра 
# меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра 
# каждого дома и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. 
# метров, цены от 3 до 20 
def task2():
    area=numpy.random.randint(100,300,15)
    price=numpy.random.randint(3*10**6,20*10**6,15)
    price_meter=list(price/area)
    price_sorted=sorted(price_meter)
    index_list=[]
    for i in price_sorted: 
        index_list.append(price_meter.index(i))
    for i in price_sorted:
        plt.bar([i for i in range(1,16)],price_sorted, tick_label=index_list, color='blue')
    plt.show()
    house_list=[]
    for i in price_sorted: 
        if i<=50000:
            house_list.append(price_meter.index(i)) 
    print(f'Список домов со стоимостью кв.м. меньше 50000: {house_list}')