# L01T09 : String Handling


# INSTRUCTIONS : Create a program that takes a string and;
#                   Makes each alternate character an uppercase character and each other alternate character a lowercase character
#                   Make each alternative word lower and upper case


input_string = input("Please input a string: ")  # receive input as input_string
alternate_char = list()  # create empty list alternate_char
words = list(input_string.split())
i = 0  # state i as 0

# While the counter is less than or equal to the length of input_string - 1
while i <= (len(input_string) - 1):
    if (
        i % 2 == 0
    ):  # if counter divided by 2 is equal to 0, that means index is either 0 or a round number
        alternate_char.append(
            input_string[i].upper()
        )  # add capitalised character from the position i of input_string to alternative_char list
        i += 1  # increment counter by 1
    else:  # if counter divided by 2 is NOT equal to 0, that means index is an odd number
        alternate_char.append(
            input_string[i].lower()
        )  # add lowercase character from the position i of input_string to alternative_char list
        i += 1  # increment counter by 1

i = 0
alternate_words = []

for i, word in enumerate(words):
    if i % 2 == 0:
        alternate_words.append(word.lower())
    else:
        alternate_words.append(word.upper())


print(
    "".join(alternate_char)
)  # print alternate_char list as a string of characters using join() function

print(" ".join(alternate_words))


# index = 0
# range = len(alternate_word)

# while index <= range:
#     if index % 2 == 0:
#         alternate_word.insert(alternate_word[index].upper(), index)

# while i <= (len(input_string.split()) - 1):
#     if i % 2 == 0:
#         alternate_word.append(input_string.lower())
#         i += 1
#     else:
#         alternate_word.append(input_string.upper())
#         i += 1
