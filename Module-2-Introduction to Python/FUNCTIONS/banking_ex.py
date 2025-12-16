def inp():
    print("ENTER 1, 2, 3")
    print("1 IS FOR WITHDRAWAL")
    print("2 IS FOR CHECK REMAINING BALANCE")
    print("3 IS FOR EXIT")
wid=5000
def res():
    a = int(input("ENTER NUMBER AS PER YOUR REQUIREMENT :"))
    if a==1:
        global b
        b=int(input("ENTER THE VALUE YOU WANT TO WITHDRAW :"))
        print("CONGRATS YOUR WITHDRAWAL WAS SUCCESSFULL")
    elif a==2:
        # b = int(input("HOW MUCH DID YOU WITHDRAW RECENTLY ? :"))
        print("YOUR REMAINING BALANCE IS :",wid-b)
    elif a==3:
         print("THANK YOU FOR BANKING WITH US")
         
    
   