# Lab_02.py
# Хімчинський Орест
# Лабораторна робота No 2.1
# Лінійні програми
# Варіант 15

b = int(input(f'Введіть значення b:\n'))
print(f'b:{b}')

z1 = ((2*b+2*((b**2-4)**0.5))**0.5)/(((b**2-4)**0.5)+b+2)
z2 = 1/((b+2)**0.5)

print(f'''
z1:{z1}\n
z2:{z2}\n
''')
