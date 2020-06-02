# Create a program that prints 1 - 10 using a while loop.
# Print a seperator like '-----' in between each number.

# number = 1
# seperator = '-----'

# while number <= 10:
#     print(number)
#     print(seperator)
#     number += 1

# --------------------------------------------
# Create a program that counts down from 100 to 0 by 10s.
# Each line needs to print "D% downloaded R% remaining. Where D is the current curent value  divided by 100 and R is the current value.
# Skip 50 and 30. (Do not print thoses)

number = 100
decrement = 10

while number >= 0:
    if number != 50 and number != 30:
        print('%s%% downloaded %s%% remaining.' % (100-number, number))
    number -= decrement
