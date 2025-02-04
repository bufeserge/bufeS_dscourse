# L01T03: The String and Numerical Data Type


# INSTRUCTIONS : Take name of user's fav restaurant and store in var string_fav
#                Below write statement to take user's favourtie number and use casting to store as int_fav
#                Print out using separate print statements below this
#                Try casting string_fav to an integer. Why does this happen? Explain in comments

# take in string_fav and int_fav, with casting int_fav as int
# print both vars seperately
# try casting string_fav as int and see what errors arise

string_fav = input("Please enter the name of your favourite restaurant : ")
int_fav = int(input("Please enter your favourite number : "))

print("Your favourite restaurant is : " + string_fav)
print(f"Your favourite number is : {int_fav}")

string_fav = int(string_fav)
# ValueError: invalid literal for int() with base 10: 'Wok This Way'
# This ValueError: invalid literal for int() happens when attempting to convert a non-numeric value into an integer
