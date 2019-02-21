def greater_number(num1,num2,num3):
    if (num1>num2):
        return(num1)
    elif (num2>num3):
        return(num2)
    else:
        return(num3)

num1 = int(input('enter the first number :'))
num2 = int(input('enter the second the number :'))
num3 = int(input('enter the third number'))
bigger = (greater_number(num1,num2,num3))
print(f'{bigger :} is  greater')##############################using f string function