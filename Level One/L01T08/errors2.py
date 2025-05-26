# L01T08 : Defensive Programming - Error Handling


# INSTRUCTIONS : Encounter, fix and add a comment where it was fixed, as well as which type of error it is with a brief explaination



# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors



####################################################################################
#ORIGINAL CODE
#animal = Lion
#animal_type = "cub"
#number_of_teeth = 16

#full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"

#print full_spec


###THERE IS A NameError ON LINE 16. This is a form of SyntaxError as well as Logical, and is fixed by putting double quotation marks surrounding 'Lion', in order to correctly state animal as a variable with the string 'Lion' as its variable
###There IS LocigalErrors ON LINE 20. The string will include things like {} as well as whatever word is inside them due to incorrect casting. To cast using {} one must place an f preceeding the string or format. proceeding, along with the variable names in order of {}
###This is fixed by placing an f for proper casing preceeding the string. I've kept to casting the string variables as this is a shorter way to write code
###THERE IS A LogicalError on line 20. When building the string full_spec, animal_type and number_of_teeth should be swapped to eachothers positions, as originally full_spec would be  'This is a Lion. It is a 16 and it has cub teeth';
###This is fixed by replacing number_of_teeth with animal_type and visa versa
###THERE IS A SyntaxError ON LINE 22. This is due to lack of parentheses surrounding full_spec that are necessary in using the print() function. Where there is an empty space I have placed parentheses which surround the variable full_spec


# CODE WITH INDICATIONS OF CHANGE
#animal = ["]Lion["]
#animal_type = "cub"
#number_of_teeth = 16
#full_spec = [f]"This is a {animal}. It is a {[animal_type]} and it has {[number_of_teeth]} teeth"
#print[(]full_spec[)]

# THE CORRECT CODE
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

print(full_spec)
####################################################################################







