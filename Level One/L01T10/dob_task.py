# L01T10 : String Handling - Input


# INSTRUCTIONS : Write a program which reads data from textfile DOB.txt and prints out two sections;
#                   Name (in bold)
#                   Orville Wright
#                   Rogelio Holloway
#                   Marjorie Figueroa
#                   …etc
#
#                   Birthdate (in bold)
#                   21 July 1988
#                   13 September 1988
#                   9 October 1988
#                   …etc


list_name = []  # declare list_name as an empty list
list_birthdate = []  # declare list_birthdate as an empty list
singleline = ""  # declare singleline as an empty str variable

with open(
    "DOB.txt", "r"
) as file:  # open DOB.txt file in r mode (no need to write to it) using with/as block
    for line in file:  # read each line of data in the file one by one, allowing us to operate on each line
        singleline = (
            line  # use singleline variable to store the current line of the file
        )

        for i in range(
            len(singleline)
        ):  # for i in the range of 0 to the length of the current line
            if singleline[
                i
            ].isdigit():  # using isdigit() function to determine if the character at i of singleline is a digit
                list_name.append(
                    singleline[:i]
                )  # add characters of singline up to index i to list_name, now being
                list_birthdate.append(
                    singleline[i : (len(singleline) - 1)]
                )  # add characters of singleline from counter i to the max length of singleline - 1, as to avoid new line entered
                break  # break if loop as intented purpose has been carried through, now moving to the next line in DOB.txt

print(
    "\n\033[1mName \n" + "\033[0m" + "\n".join(list_name)
)  # print out heading using "\n", to add new line, "\033[1m" to bolden and
# then "\033[0m" to return to normal weight font, finally joining list_name with "\n" as to print each name onto consecutive lines
print(
    "\n\033[1mBirtdate \n" + "\033[0m" + "\n".join(list_birthdate)
)  # print out heading using "\n", to add new line, "\033[1m" to bolden and
# then "\033[0m" to return to normal weight font, finally joining list_birthdate with "\n" as to print each name onto consecutive lines
