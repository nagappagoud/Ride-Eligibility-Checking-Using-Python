print("check the Ride Eligibility")
hight=int(input("enter your hight"))
age=int(input("enter your age"))
if hight>=120:
    print("you are Eligibil for Ride")
    if age<=12:
        print("pleas pay $5")
    elif 12<age<=18:
        print("pleas pay $7")
    else:
        print("pleas pay $12")
else:
    print("you are not Eligibil for Ride")


 
