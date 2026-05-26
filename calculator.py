num1 = int(input("Enter the 1st number :"))
num2 = int(input("Enter the 2nd number : "))

operator = input("Enter the operation : ")

match operator:
    case '+':
        print("the sum of numbers is : ",num1+num2)
    case '-':
         print("the subtraction of numbers is : ",num1-num2)    
    case '*':
        print("the multiplication of numbers is : ",num1*num2)  
    case '/':
        print("the division of numbers is : ",num1/num2) 
    case '//':
        print("the division of numbers is : ",num1//num2) 
    case '**':
        print("the division of numbers is : ",num1**num2)         
    case default:
        print("Enter valid operation ")