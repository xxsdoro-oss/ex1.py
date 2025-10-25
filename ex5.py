weight = float(input('Enter your weight'))
unit = input('kilograms or pounds? (K or L)')

if unit == 'K':
    weight = weight * 2.205
    unit = 'Lbs.'
elif unit == 'L':
    weight == weight / 2.205
    unit = 'Kgs.'
else:
    print(f'{unit} is not valid.')

print(f'Your weight is: {round(weight, 1)} {unit}')
