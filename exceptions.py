# Create a program that asks for a number between 10 - 101.
# If the user enters anything that is not a number, or is less than 10 or greater than 101 throw some sort of insult.
# If the number is 42 print a very positive message.
# If the number -1 disregaurd the first point and print a message about being a smart person.
# Any other print a message that includes the number given.

# number = input("Please enter a number between 10 and 101!\n")
# try:
#     if int(number) == -1:
#         print("Hey, Smarty Pants!")
#     elif int(number) < 10 or int(number) > 101:
#         print("What were you thinking? That's not between 10 and 101!")
#     elif int(number) == 42:
#         print("FANTASTIC! I LOVE 42")
#     else:
#         print("Nice! %s is your number!" % number)
# except ValueError:
#     print('This is wrong! Please enter only numbers!')
#     exit()


# Create a program that ask for 2 numbers and then divides the first number from the second number.
# Handle any possible errors without using any 'if'.
# If the result is a valid option, print "The result is X" where X is the value.
# Otherwise give an error that describes the issue.
# (challange) Still without using if. Let the user know which value is causing and exemption.
# (Extra Challange) Still without using ifs, If the first or second value is not a valid integer,
# have the program keep asking UNTIL the user supplies a valid integer. (think about the bolded word)


try:
    first_num = int(input("Number 1\n"))
    second_num = int(input("Number 2\n"))
    print("the result is %s." % (first_num/second_num))
except ValueError:
    print("Only input numbers!")
    exit()
except ZeroDivisionError:
    print("You divided by zero! OOPSY!")
    while second_num == 0:
        print("your second # was 0!")
        exit()
