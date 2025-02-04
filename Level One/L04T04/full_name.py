# L01T04 : Control Structures - If, Elif, Else and the Boolean Data type


# INSTRUCTIONS : Ask user for their name and save such as var
#                Perform validation checks that would output the following if not met:
#     “You haven’t entered anything. Please enter your full name."; “You have entered less than 4 characters. Please make sure that you have entered your name and surname.”;
#    “You have entered more than 25 characters. Please make sure that you have only entered your full name."; “Thank you for entering your name."


# receive user name and store as var
# create var based on len(user's name)
# check if this var is equal to 0, elif its less than 4, elif its more than 25, else its fine.

user_name = input("Please enter your full name : ")
leng_name = len(user_name)

if leng_name == 0:
    print("You haven’t entered anything. Please enter your full name.")
elif leng_name < 4:
    print(
        "You have entered less than 4 characters. Please make sure that you have entered your name and surname."
    )
elif leng_name > 25:
    print(
        "You have entered more than 25 characters. Please make sure that you have only entered your full name."
    )
else:
    print("Thank you for entering your name.")
