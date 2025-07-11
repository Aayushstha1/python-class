
# try: 
#     print("hello")
# except :
#     print("Error")


try:
    a=10
    b= "20"
    print(a+b)
    
except NameError as e:
    print("NameError:", e)
except TypeError as e:
    print("TypeError:", e)

finally:
    print("This will always execute, regardless of whether an exception occurred or not.")













