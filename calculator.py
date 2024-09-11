#Basic Calculator
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

#Get User Choice
a=input("Enter your choice[1,2,3,4]:-")
if a in ['1','2','3','4']:
    num1=float(input("Enter first number:-"))
    num2=float(input("Enter second number:-"))
    
#Perform the choosen operation

    if a =='1':
        print(num1+num2)
    elif a =='2':
        print(num1-num2)
    elif a =='3':
        print(num1*num2)
    elif a =='4':
        print(num1/num2)
    else:
        print("Invalid selectioon")
        
        
