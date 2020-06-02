COUNTDOWN_TIME = 100

id_message = """
Greetings:
Please enter Galactic ID Username
"""

ship_message = """
Please state the name of you ship:
"""

accepted_message = """
Welcome %s your ID has been accepted.
The %s's docking has been logged and credits will be withdrawn your account.
"""

star_wars_name = input(id_message)

name_length = len(star_wars_name)

if star_wars_name:
    if name_length > 12 or name_length <= 3:
        print('Galatic IDs must be between 4 and 12 characters long')
    else:
        ship_name = input(ship_message)
        if not ship_name:
            print("You must enter your ship name to proceed!")
        elif len(ship_name) >= 6 and star_wars_name != ship_name:
            print("Processing. Please Wait.")
            countdown = COUNTDOWN_TIME
            while countdown >= 0:
                print("%s%% ...\n" % countdown)
                countdown -= 10

            print(accepted_message % (star_wars_name, ship_name))

        else:
            print(
                'The ship name cannot be less than 6 charecters and must not be the same as the Galatic Id.')
else:
    print("You must enter an ID to proceed!")

print("End of Transmission >>>")
