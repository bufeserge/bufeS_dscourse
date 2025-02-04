# L01T04 : Control Structures - If, Elif, Else and the Boolean Data type


# INSTRUCTIONS : Design program determining award person competing in triathlon receives.
#                   Should accept three user inputs, in minutes, in swimming, cycling and running
#                   With this calc the total time take to complete triathlon : "Total time taken for the triathlon: "
#                   With this check for which award is given to said person:
#                       *Within qualifying time -                0-100 minutes      -   Provincial colours
#                       *Five minutes off from qualifying   -    101-105 minutes    -   Provincial half colours
#                       *10 minutes off from qualifying -        106-110 minutes    -   Provincial scroll
#                       *More than 10 minutes off qualitfying -  111+ minutes       -   No award
#                   Output award or "No award"; e.g. "Award: Provincial scroll"


# I need to explain to user and receive times for SWIMMING, CYCLING and RUNNING in minutes and store as s, c, and r
# create if statement, if vars for each event in triathlon are numbers then calc and store total time in minutes taken to complete triathlon;
#   elif this total time var is less than or equal to 100 then award Provincial colours;
#   elif total time is greater than or equal to 101 and less than or equal to 105 then award Half Provincial Colours;
#   elif total time is greater than or equal to 106 and less than or equal to 110 then award Provincial Scroll;
#   else print that the user has received no awards
# else print the user has entered in their times wrong, as the check for numbers in vars s, c, and r has failed



print(
    '''
Congradulations! I'm here to award you one of the following awards based on your performance in the triathlon!
Qualifying time is anywhere between 0 minutes and 100 minutes for the triathlon.

The awards are as followings:    
    Provincial Colours, received if you are within qualifying time.    
    Provincial Half Colours, received if you are 5 minutes or less off qualifying time.    
    A Provincial Scroll, received if you are 10 minutes or less off qualifying time. 
    or nothing! This is if you are more than 10 minutes off qualifying time.
    '''
)


s = input("Please input the time it took you to complete the SWIMMING portion of the triathlon in minutes : ")
c = input("Please input the time it took you to complete the CYCLING portion of the triathlon in minutes : ")
r = input("Please input the time it took you to complete the RUNNING portion of the triathlon in minutes : ")


if s.isnumeric() and c.isnumeric() and r.isnumeric():
    tot_time = int(s) + int(c) + int(r)
    print(f"Total time taken for the triathlon : {tot_time} minutes")
    if tot_time <= 100:
        print("You have received Provincial Colours!")
    elif tot_time >= 101 and tot_time <= 105:
        print("You have received Provincial Half Colours!")
    elif tot_time >= 106 and tot_time <= 110:
        print("You have received a Provincial Scroll!")
    else:
        print("You have received nothing!")
else:
    print("You may have entered your minutes wrong! Please re-run the programme and remember to add just your minutes!")
