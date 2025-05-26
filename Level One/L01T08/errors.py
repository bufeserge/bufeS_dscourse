# L01T08 : Defensive Programming - Error Handling


# INSTRUCTIONS : Encounter, fix and add a comment where it was fixed, as well as which type of error it is with a brief explaination


# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.


####################################################################################
# ORIGINAL CODE
# print "Welcome to the error program"
#    print "\n"

###THERE IS A SyntaxError ON LINE 17 AS WELL AS 18. This is due to missing parentheses surrounding "Welcome to the error program" as well as "\n", which is necessary in utilising the print() function.
###These parentheses should replace the empty space between print and "Welcome to the error program", as well as that of print and "\n".
###The space between these two pieces of the print()function should not be there either.
###THERE IS AN IndentationError ON LINE 18 WHEN LINE 16 IS CORRECT. This is a form of a SyntaxError and is caused by the incorrect indentation of line 17.
###I have therefore fixed this by adding the necessary parentheses when using the print() funcion, as indicated by the square brackets [] in the commented out, CODE WITH INDICATIONS OF CHANGE below;
### [.] is an indication of the removal of the incorrect indentation, where . is an indication of how many indentations it was originally indented by.

# CODE WITH INDICATIONS OF CHANGE
# print[(]"Welcome to the error program"[)]
# [.]print[(]"\n"[)]

# THE CORRECT CODE
print("Welcome to the error program")
print("\n")
####################################################################################
#####################################################################################
# WHAT CODE IS SUPPOSED TO DO : # Variables declaring the user's age, casting the str to an int, and printing the result

# ORIGINAL CODE
#    age_Str == "24 years old"
#    age = int(age_Str)
#    print("I'm" + age + "years old.")

###THERE IS AN IndentationError ON LINE 39, AS WELL AS LINES 40 & 41. This is a form of a SyntaxError and is caused by the incorrect indentation of lines 39, 40 and 41. Removal of such is indicated.
###THERE IS A NameError ON LINE 40. This is caused by the lack of defining and is caused by a LogicalError, as saying age_Str == "24 years old" means the string "24 years old" is compared to age_Str(undefined);
###Removing the second = will now define age_Str as the string "24 years old".
###I've also kept the capital S in "age_Str" as it can serve as a could differential to the str() function.
###THERE IS A ValueError ON LINE 40. This is a form of a SyntaxError (as well as LogicalError) and is caused by trying to cast a string with characters that are not numeric into an integer.
###I have thus added to line 40, seen under THE CORRECT CODE below, 'int(age_Str[0:1])'. Doing this will grab only the first two characters of age_Str, being "24". This ensures only numeric characters are present in the integer casting process
###THERE IS A TypeError ON LINE 41. This is a form of SyntaxError and is caused by the incorrect usage of integers and strings during the print() function.
###This is fixed by casting age as a str() during the print() function, as well as correcting the syntax of output by adding empty spaces at the end and begininning of the respective strings "I'm" & "years old."
###This can also be changed to 'print(f"I'm {age} years old.")'

# CODE WITH INDICATIONS OF CHANGE
# [.]age_Str =[= removed] "24 years old"
# [.]age = int(age_Str[[0:2]])
# [.]print("I'm[ ]" + [str(age)] + "[ ]years old.")

# THE CORRECT CODE
age_Str = "24 years old"
age = int(age_Str[0:2])
# print(f"I'm {age} years old.")
print("I'm " + str(age) + " years old.")
#####################################################################################
######################################################################################
# WHAT CODE IS SUPPOSED TO DO : # Variables declaring additional years and printing the total years of age

# ORIGINAL CODE
#   years_from_now = "3"
#   total_years = age + years_from_now

# print "The total number of years:" + "answer_years"

###THERE IS AN IndentationError ON LINES 68 & 69. This is a form of SyntaxError, and is caused by the incorrect indentation of lines 68 & 69. This is fixed by removing these indentations
###THERE IS A SyntaxError ON LINE 71. This is caused by the lack of parentheses surround '"The total number of years:" + "answer_years"' where it is necessary for the print() function
###THERE IS A TypeError ON LINE 71. This is a RuntimeError and is caused by stating years_from_now as a string, and then trying to add age(an integer) to this variable (a string) to create the value for total_years
###THERE IS A LogicalError ON LINE 71. Line 71, instead of outputting the total_years calculated in line 70, '"answer_years"' is printed following '"The total number of years:"';
###This can be fixed by changing these double qoutation marks to {}, and casting the total_years variable as a string in the place of '"answer_years"'
###In addition, I've added the line 'print("Years from now : " + years_from_now)' to add clarification


# CODE WITH INDICATIONS OF CHANGE
# [.]years_from_now = "3"
# [print("Years from now : " + years_from_now)]
# [.]total_years = age + [int(]years_from_now[)]
# print[(f]"The total number of years[ ]:" + {total_years}

# THE CORRECT CODE
years_from_now = "3"
print("Years from now : " + years_from_now)
total_years = age + int(years_from_now)

print(f"The total number of years : {total_years}")
######################################################################################
#######################################################################################
# WHAT CODE IS SUPPOSED TO DO : # Variable to calculate the total amount of months from the total amount of years and printing the result

# ORIGINAL CODE
# total_months = total * 12
# print "In 3 years and 6 months, I'll be " + total_months + " months old"

###THERE IS A LogicalError ON LINE 99 caused by the lack of defining total as a variable before using such in the calculations of total_months. This is fixed by replacing total with total_years
###THERE IS A SyntaxError ON LINE 100 caused by missing parentheses surrounding the print() function. This is fixed by adding parentheses
###THERE IS A TypeError ON LINE 100 caused by incorrectly printing a combination of strings and an integer together in the print() function. This is fixed by casting total_months as a string
###THERE IS A LogicalError ON LINE 100. The program is to output how many months old the user will be in 3 years and 6 months. The 3 years has already been added to totaL_years previously;
###But there is no addition of the 6 months in order for this statement to be correct. Therefore I'll cast using f and add 6 to total_months.


# CODE WITH INDICATIONS OF CHANGE
# total_months = total[_years] * 12
# print[(f]"In 3 years and 6 months, I'll be [] [total_months + 6] [] months old"

# THE CORRECT CODE
total_months = total_years * 12
print(f"In 3 years and 6 months, I'll be {total_months + 6} months old")

# HINT, 330 months is the correct answer
