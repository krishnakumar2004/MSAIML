# create 3 dictionaries with mapping of key to class number
# first dictionary values should be Room name
# second dictionary values should be instructor name
# third dictionary values should be time with am or pm
course_Room = {"CSC101": 3004,"CSC102": 4501,"CSC103": 6755,"NET110": 1244,"COM241": 1411}
course_Instructor = {"CSC101": "Haynes" ,"CSC102": "Alvarado" ,"CSC103": "Rich","NET110": "Burke" ,"COM241": "Lee" }
course_Meet_Time = {"CSC101": "8:00 a.m." ,"CSC102": "9:00 a.m." ,"CSC103": "10:00 a.m.","NET110": "11:00 a.m." ,"COM241": "1:00 p.m." }

# get user input to enter Course Number
user_input = input("Enter Course number?\n")

if (user_input in course_Room.keys()) :
    print("For Course Number {} - Room No is {}, ".format(user_input,course_Room[user_input]))
    print("Instructor is {}, ".format(course_Instructor[user_input]))
    print("Meeting time is {}".format(course_Meet_Time[user_input]))
else :
    print("Entered Course Number is invalid")