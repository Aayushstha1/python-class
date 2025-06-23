# a= "Aayush".upper()
# print(a.islower())

a = int(input("Enter the A mark: "))
b = int(input("Enter the B mark: "))
c = int(input("Enter the C mark: "))
d = int(input("Enter the D mark: "))
e = int(input("Enter the E mark: "))

if not all(0 <= mark <= 100 for mark in [a, b, c, d, e]):
    print("Please enter valid marks between 0 and 100 for all subjects.")
else:
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








        # chowim /        half/full       veg? 130full half 80 .........