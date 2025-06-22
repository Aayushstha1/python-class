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



a = int(input("Enter a Mark: "))
b = int(input("Enter b Mark: "))
c = int(input("Enter c Mark: "))
d = int(input("Enter d Mark: "))
e = int(input("Enter e Mark: "))
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

      