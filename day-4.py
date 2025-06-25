years= int(input("Enter the years"))
if years%4 == 0 :
    if years%100==0:
        if years%400==0:
            print("leap years")
        else: ('not a leap years')
    else: ( "Leap years")
else:("Not a laep years")
  
