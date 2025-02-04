# L01T03 : The String and Numerical Data Types


# INSTRUCTIONS : ask user to enter three different ints
#                print out : The sum of all the numbers; The first number minus the second number;
#        The third number multiplied by the first number; The sum of all three numbers divided by the third number

# receive input three times from user to get integers as vars
# create var as sum of all three inputed integers as vars
# print sum of all with casting var for sum of all as string
# print first minus second with casting first var minus second var as string
# print third times first with casting third var * first var as string
# print sum of all divided by third with casting var for sum of all / third var as string


int_one = int(input("Please input an integer [1/3] : "))
int_two = int(input("Please input an integer [2/3] : "))
int_three = int(input("Please input an integer [3/3] : "))
int_all = int_one + int_two + int_three

print("Sum of all integers entered : " + str(int_all))

print("     [1/3] - [2/3] : " + str(int_one - int_two))

print("     [3/3] * [1/3] : " + str(int_three * int_one))

print("Sum of all integers entered / [3/3] : " + str(int_all / int_three))
