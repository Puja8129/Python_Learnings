#wap to perform user specific operation eg: add, sub etc
def display_option(): 
    print("1. Addition\n2. Subtraction\n3. Multiplication")

def user_input():
    action_input = input("Chhose the option from above: ")
    number_input1 = int(input("enter first number"))
    number_input2 = int(input("enter second number"))
    perform_operations(action_input,number_input1,number_input2)
    
def perform_operations(operation,number_input,number_input2):
    if operation=="1":
        result = add(number_input,number_input2)  
        print(result)
        
    elif operation=="2":
        if number_input>number_input2:
            print(sub(number_input,number_input2))
        else :
            print(sub(number_input2,number_input))
           
    elif operation=="3":
        print(multi(number_input,number_input2))

    else :
        print("No Match Found")  

def add(number_input,num2):
    #print(number_input+num2)
    return number_input+num2

def sub(number_input,num2):
    #print(number_input-num2)
    return number_input-num2
def multi(number_input,num2): 
    mul= (number_input*num2)
    #print(mul)  
    return mul

if __name__=="__main__" :
    display_option()
    user_input()
    


             




