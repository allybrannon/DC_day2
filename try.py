droids = '100'

try:
    print(3-droids)
except TypeError:
    print("what is wrong with droids...is it a string or a number?")

try:
    print(int(droids) / 0)
except ZeroDivisionError:
    print("You casted droids into int...but you divided by 0!")
