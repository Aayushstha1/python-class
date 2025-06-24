# a= "Aayush".upper()
# print(a.islower())

# a = int(input("Enter the A mark: "))
# b = int(input("Enter the B mark: "))
# c = int(input("Enter the C mark: "))
# d = int(input("Enter the D mark: "))
# e = int(input("Enter the E mark: "))

# if not all(0 <= mark <= 100 for mark in [a, b, c, d, e]):
#     print("Please enter valid marks between 0 and 100 for all subjects.")
# else:
#     total = a + b + c + d + e
#     avg = total / 5
#     percentage = (total / 500) * 100
#     print("Percentage:", percentage)

#     if percentage >= 90:
#         print("Grade: A")
#     elif percentage >= 80:
#         print("Grade: B")
#     elif percentage >= 70:
#         print("Grade: C")
#     elif percentage >= 60:
#         print("Grade: D")
#     elif percentage >= 50:
#         print("Grade: E")
#     else:
#         print("Grade: F")








        # chowim /        half/full       veg? 130full half 80 .........


full = 140
half = 80
fullmomo= 100
halfmomo=50

print("Menu: Chowmin or Momo")
choice = input("What would you like to order? (chowmin/momo): ")
if choice == "chowmin":
    size = input("choose size(full/half): ")
    order = input("veg or non-veg?(veg/non-veg): ")
    price = 0
    if size == "full":
        price = full
    elif size == "half":
        price = half
    else:
        print("Invalid order")
    if order == "non-veg":
        price += 50
        print("Please wait, your order is being prepared...")
        print("You ordered " + size + " " + order + " chowmin. Price: Rs." + str(price))

elif choice == "momo":
    size = input("choose size(full/half): ")
    order = input("veg or non-veg?(veg/non-veg): ")
    price = 0
    if size == "full":
        price = fullmomo
    elif size == "half":
        price = halfmomo
    else:
        print("Invalid order")
    if order == "non-veg":
        price += 50
        print("Please wait, your order is being prepared...")
        print("You ordered " + size + " " + order + " momo. Price: Rs." + str(price))

