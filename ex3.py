import math

radius = float(input('Enter the radius of a circle:'))
circumference = 2 * math.pi * radius
print(f'The circumference of the circle is {circumference}cm.')

area = math.pi * pow(radius, 2)
print(f'The area of the circle is {area}cm^2.')

a = float(input('Enter side A :'))
b = float(input('Enter side B :'))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f'Side c = {c}')
