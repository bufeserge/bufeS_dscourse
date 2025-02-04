# L01T06 : Control Structures - While Loop


# INSTRUCTIONS : Write program that always asks user to enter a number
#                When user enters -1 the program shoupd stop requesting the user to enter a number
#                Program must then calc average of numbers entered excluding the -1
#                Program must make use of while loop

# make var nums_entered = 0
# make i_nums = 0
# make i = 0
# make ask_questions = true
# while ask_questions, ask the user to enter a number
# if user entered number above -1, then in while loop we increment nums_entered by i[entered number] and increment i_nums by 1
# else user entered -1, then we break the while loop, not adding i to nums_entered and not increment i_nums by 1
# when while loop is broken, we divide nums_entered by i_nums to get average and print this


nums_entered = 0
i_nums = 0
i = 0
ask_questions = True

while ask_questions:
    i = int(input("Please enter a number : "))
    if i == -1:
        break
    nums_entered += i
    i_nums += 1

print(f"Average of all {i_nums} number(s) entered : {int(nums_entered / i_nums)}")
