# L01T07 : Control Structures - For Loops


# INSTRUCTIONS : Output * on seperate lines, consecutively getting one more *;
#                Until 5 *, then back down to 1
#                Do so using an if-else statement in combo with a single for loop
#                Pattern: 
#                   *
#                   **
#                   ***
#                   ****
#                   *****
#                   ****
#                   ***
#                   **
#                   *

# start off with initialising a var for both the pattern marker and the counter when it comes to removing characters
# initialise for loop in the range of 1 to 10.
#   initialise an ifelse statement, stating that if the for counter (i) is lower or equal to the number 5, then;
#   increment the pattern_marker var with "*", and print such
#   next initialise the else part of ifelse statement, stating that if i is higher than 5, then;
#   restate remove_counter as to whatever the last number of the range set in the if statement (which is 10) minus i
#   print such.


#Created pattern_mark and set as empty string var, this is so in the first loop of the for statement we can just increment
#such with "*".
pattern_mark = ""

#Created remove_counter and set to zero for safety as well as to be able to count to the correct character in the string
#pattern_mark when it comes to the other portion of the pattern to print
remove_counter = 0

#Initialise for loop saying for counter i in the range of 1-10, meaning it will count to 9
for i in range(1,10):
    #Initialise if statement, saying if for counter i is within range of 1-5 + equal to 5 then;
    if i <= 5:
        #Utilise pattern_mark var and increment such by one "*"
        pattern_mark += "*"
        #Print pattern_mark on a new line
        print(pattern_mark)
    #Intialise else so as for any for loop counter i over 5 and not equal to it then;
    else:
        #Utilise remove_counter var and set to the length of the range(10) minus the value of for loop counter i
        remove_counter = 10 - i
        #Print pattern_mark with str manipulation, starting at character 0 and moving through to the vale of remove_counter var
        #i.e. if i = 8 then remove_counter should be 2, so only the first two characters of pattern_mark are printed
        print(pattern_mark[0:remove_counter])

#In this way, I'm able to count back from 5 when 5 is reached, so pattern_mark at the end of this should be
#"*****", but we begin to print such as "****", "***", and so on back down to "*"