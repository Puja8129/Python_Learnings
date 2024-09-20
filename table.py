#wap for 2 table
import math

def table(n):
    result = 1
    finalresult = []    
    for i in range(1,11,1):
        result = n*i
        finalresult.append(result)
    print(finalresult)
    #return finalresult

#def display():
    table()


#if __name__=="__main__":
    #user_input=int(input("enter"))
    #val=table(user_input)
    #print(val)        

