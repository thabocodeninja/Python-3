#class Planet:

#     def __init__(self):
#          self.name = 'Hoth'
#          self.radius =20000
#          self.gravity = 5.5
#          self.system = 'Hoth System'

#    def orbit(self):
#         return f'{self.name} is orbiting in the {self.system}'

# hoth = Planet()
# print(f'Name is :{hoth.name}')
# print(f'Radius is :{hoth.radius}')
# print(f'the gravity is :{hoth.gravity}')
# print(hoth.orbit())

from package.planet import Planet

from package.calc import planet_mass,planet_vol



naboo = Planet('Naboo',30000,8,'Naboo System')

naboo_mass = planet_mass(naboo.gravity,naboo.radius)
naboo_vol = planet_vol(naboo.radius)


print(f'{naboo.name} has a masss of {naboo_mass} and a volume of {naboo_vol}')

