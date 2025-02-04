# L01T03 : The String and Numerical Data Types


# INSTRUCTIONS : Ask the user to enter a sentence using the input() method. Save the user’s response in a variable called str_manip
#                Calc and display length of str_manip
#                Find last letter of str_manip and replace every occurance of this letter in str_manip with "@"
#                Print the last three characters of str_manip backwards
#                Create five letter word using first 3 characters of and two last characters of str_manip

# receive input sentence
# print str_manip and use len() function to get the number of characters in str_manip
# create last_letter var and use slicing to get -1 indexed character in str_manip
# print str_manip with use of replace() function to replace any character that is the same as last_letter with "@" DOES NOT ACCOUNT FOR DIFFERENCE IN CAPS AND LOWERCASE
# print str_manip with use of slicing to get first three characters, then with use of extended slicing as to start from -2 indexed character, then move backwards by -1 till -3 indexed character, then use last_letter var
###  *   *   *   There is a KeyboardInterrupt error coming up for line 18, I understand it has something to do with
#                CNTR+C, and that there are ways of handling the error by having another piece of code run if that error
#                where to appear
str_manip = input("Please enter a sentence of your choosing : ")


print(len(str_manip))

last_letter = str_manip[-1:]
print(str_manip.replace(last_letter, "@"))

print(str_manip[-1:-4:-1])

print(f"{str_manip[0:3]}{str_manip[-2:-3:-1]}{last_letter}")
