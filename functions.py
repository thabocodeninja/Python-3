#def greet(name,time):
#   print(f'Good {time}{name},hope you are well')

# greet('Thabo','morning')

def area(radius):
    return 3.142 * radius * radius

def vol(area,length):
    print(area * length)

radius = int(input('enter a radius:'))
length = int(input('enter a length :'))

vol(area(radius),length)

