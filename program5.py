#wap 
def ajib_fun(sanki):
    if sanki==1:
        return 1
    if sanki==2:
        return 2
    if sanki==0:
        return 100
    
    else :
        return 1000

if __name__=="__main__"  : 
    print("Enter Desired Number")
    user_input = int(input("desired number : "))
    result=ajib_fun(user_input)

    print(result)
