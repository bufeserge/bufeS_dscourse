# L01T03 : The String and Numerical Data Types


# INSTRUCTIONS : Save "The!quick!brown!fox!jumps!over!the!lazy!dog." as a single string and then replace all "!" with " "
#                Reprint that sentence using upper()
#                Then print that sentence in reverse


# collect "The!quick!brown!fox!jumps!over!the!lazy!dog." as a string
# replace all "!" with " " in this string and replace the variable with its new self
# print string
# print string with use of upper() function to capitalize the sentence
# print string with use of extended slicing in order to reverse its order


string = "The!quick!brown!fox!jumps!over!the!lazy!dog."
string = string.replace("!", " ")

print(string)
print(string.upper())
print(string[::-1])
