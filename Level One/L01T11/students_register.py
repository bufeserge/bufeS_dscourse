# L0T11: IO Operations - Output


# INSTRUCTIONS: Write program to allow students to register for an exam venue
#               FIRST   -   Ask user how many students are registering
#               SECOND  -   Create for loop using that number of students, each loop should ask user to enter the next student ID
#               THIRD   -   Write each of the ID numbers to a text file called reg_form.txt
#               FOURTH  -   Include a dotted line after each student ID coz doc will be used as attendance register, and each student should sign this
#                           when they arrive to the exam venue

# ill make an input variable to gather the amount of students which need to be registered. Ill also declare an empty list reg_form_list;
# ill create a for loop, with this input variable as the amount of times to loop through
# inside this for loop, ill append reg_form_list with an inputted value, along with a dotted line.

reg_form_list = []  # declare empty list
i_count = int(
    input("Enter the number of students you'd wish to add to the addentance register: ")
)

for i_count in range(1, i_count + 1):
    reg_form_list.append(input(f"Enter valid student ID for student {i_count} : "))


with open("reg_form.txt", "w") as file:
    for i, line in enumerate(reg_form_list):
        file.write(f"{line}")
        file.write("\t........" + "\n")
