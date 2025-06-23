# #control flow
# a = 10
# b = 20
# if a > b:
#     print(a)
# else:
#     print(b)


# a = int(input("Enter a Num: "))
# b = 2
# if a % b == 0:
#     print("Even")
# else:
#     print("Odd")



# a=10
# if a < 0:
#     print("Negative")
# elif a >0:
#     print("Positive")
# else:
#     print("Zero")


a = int(input("Enter the A mark: "))
b = int(input("Enter the B mark: "))
c = int(input("Enter the C mark: "))
d = int(input("Enter the D mark: "))
e = int(input("Enter the E mark: "))

# if not all(0 <= mark <= 100 for mark in [a, b, c, d, e]):
#     print("Please enter valid marks between 0 and 100 for all subjects.")

# a = int(input("Enter a Mark: "))
# if a <=100 and a >=0 :
#  b = int(input("Enter b Mark: "))
#  elif b <=100 and b>=0:
#   c = int(input("Enter c Mark: "))
# if c <=100 and c>=0:

# d = int(input("Enter d Mark: "))
# if d <=100 and d>=0:

# e = int(input("Enter e Mark: "))
# if e <=100 and e>=0:
# if (0>=a<=100 and 0>=b<=100 and 0>=c<=100 and 0>=d<=100 and 0>=e<=100):
if(0>=(a and b and c and d and e)<=100):
    total = a + b + c + d + e
    avg = total / 5
    percentage = (total / 500) * 100
    print("Percentage:", percentage)
    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 80:
        print("Grade: B")
    elif percentage >= 70:
        print("Grade: C")
    elif percentage >= 60:
        print("Grade: D")
    elif percentage >= 50:
        print("Grade: E")
    else:
        print("Grade: F")
else:
    print('invalid')



# # 


# name = input("Enter a Name: ")
# if name == "Aayush":
#     print("Hello, Aayush")

# palace . 4 doors .... wait the boat is never come . and End  if it swims then there is a 4 doors . 1st door= tiger . 2nd = lion . 3rd= tresure . u won   4th door u're in the hole . u lost . 

# name = input(" Enter the direction" )
# if name == "left":
#     print("u're in wrong direction")
# elif name =="Right":
#     print ("U're in wrong direction") 
# elif name == "stright":
#     print ("you are in right way ")
#     action = input("choose your action (wait/swim)")
#     if action == "wait":
#         print ("the boat never come ")
#     elif action == "swim":
#         print (" U find the way  ")
#         choose = input (" U are in Right path Now choose the right door")
#         if choose == "1":
#             print ("Tiger eat u . Game over")
#         elif choose == "2":
#             print ("Snake Bite u ")
#         elif choose =="3":
#             print ("u got the tressure ")
            





