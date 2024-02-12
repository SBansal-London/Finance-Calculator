import math
print("investment- to calculate the amount of interest you'll earn on your investment")
print("bond- to calculate the amount you'll have to pay on a home loan ") 
select_anyone = input("Enter either 'investment' or 'bond' from the menu above to proceed:")
if select_anyone.lower() == "investment" :
    # taking inputs from user
    p = int(input("Enter the amount of money you are depositing : "))
    r = int(input("Enter the Interest (in number without %) : ")) 
    t = int(input("Enter the number of years : "))
    interest = input("Enter : simple or compound : for respective interest :")
    #calculate simple interest
    if interest == "simple":
        a= p*(1+r/100*t)
        print(f" The total amount is {a}")
    # calculate compound interest
    if interest == "compound" :
        a = p * math.pow((1+r/100),t)
        print(f" The total amount is {a}")
# user select bond option
if select_anyone.lower() == "bond" :
     p = int(input("Enter present value of house : "))
     i = int(input("Enter the Interest (in number without %) : ")) 
     n = int(input("Enter the number of months for repayment : "))
     i=i/12/100
    #calculate monthly repayment amount
     a = (i*p)/(1-(1+i)**(-n))
     print(f" The repayment amount each month is {a}")
    

       




