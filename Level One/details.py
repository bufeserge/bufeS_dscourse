# L02T01 : Your First Computer Program and Using Variables


# INSTRUCTIONS : Use an input() command to get the following information from the user: Name, age, House number, Street name.
#               Print this all out in a single string
#               e.g. This is John Smith. He is 28 years old and lives at house number 42 on Hamilton Street.


# print all constant wording plus inputted information from user using f-string
# no need for variables right now as there is no continuation or manipulation like formating neccessary


print(
    f"This is {input('Please enter your full name : ')}. He is {input('Please enter your age : ')} years old and lives at house number {input('Please enter your house number : ')} on {input('Please enter your stree name : ')}."
)
