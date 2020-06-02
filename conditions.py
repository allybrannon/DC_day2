# name = ""

# if True:
#     name = "Yoda"

# if False:
#     name = 'Jar Jar Binks'

# print("%s knows how to use a lightsaber" % name)

message = """
Greetings:
Please enter Galactic ID Username
"""
star_wars_name = input(message)

if(star_wars_name != ""):
    print("Welcome %s your ID has been accepted." % star_wars_name)
else:
    print("YOU must enter an ID to proceed!")

print("End of Transmission >>>")
