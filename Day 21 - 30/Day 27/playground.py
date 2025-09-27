def add(*args):
    return sum(args)

print(add(1, 2, 3, 4, 5))

def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['mul']
    print(n)

calculate(2, add=3, mul=4)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.year = kwargs.get('year')
        self.miles = kwargs.get('miles')
        self.year_change = kwargs.get('year_change')
        self.colors = kwargs.get('colors')
        self.colors_change = kwargs.get('colors_change')
        self.seats = kwargs.get('seats')

car = Car(make='Ford', model='Mustang')
print(car.make)
print(car.model)