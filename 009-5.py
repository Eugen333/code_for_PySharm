

print('Завдання 9-3')
print()
def quadratic_equation(a,b,c):

    def calc_rezult(a,b,c):
        # розрахунок дискримінанту
        dcr = b ** 2 - (4 * a * c)
        print('значення дискримінанту:', dcr)
        return dcr


    x1=None
    x2=None
    dcr = calc_rezult(a,b,c)
    if dcr < 0:
        print('Коренів немає')
    elif dcr == 0:
        x1 = list([-b / (2 * a)])
        return x1
    else:
        x2 = list([(-b - dcr ** 0.5) / (2 * a)])
        x2.append((-b + dcr ** 0.5) / (2 * a))
        return x2


a=float(input("введіть перше число:"))
b=float(input("введіть друге число:"))
c=float(input("введіть трете число:"))
print('перелік значень коренів квадратного рівняння:', quadratic_equation(a,b,c))
