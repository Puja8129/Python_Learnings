#wap find factorial of a number

def factorial(number_value):
    if number_value <= 0 :
        return 1
    
    else :
        result = 1
        for i in range(number_value,1,-1):
            result= result*i
        return result
   
if __name__=="__main__":
    user_input = int(input("give your input : "))
    val =factorial(user_input)
    print(val)