# 1. write a python script to calculate area of a rectangle.
# 2. Write a python script tp calculate simple interest.
# 3. Write a python script to remove the last digit from a given number.
# 4. Write a python script to swap data of two variables.
# 5. Write a python script to check wheather a given number is divisible by 5 or not.
# 6. Write a python script to print two given words in dictionary order.
# 7. Write a python script to check whether a given number is a three digit number or not.
# 8. Write a python script to check whether a given year is leap yaer or not. 
# 9. Write a python script to check wether a given  number is positive negative or zero.
# 10.Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part.

# 1. write a python script to calculate area of a rectangle.
def area_rec(a,b):
    area = (a*b)
    print(area)

# 2. Write a python script tp calculate simple interest.
def simple_int():
    p,r,t = int(input("enter princial")), int(input("enter rate of interest")), int(input("enter tenure"))
    si = (p*r*t)/100
    print(si)

# 3. Write a python script to remove the last digit from a given number.
def remove(num):
    sub_num = num // 10
    print(sub_num) 

# 4. Write a python script to swap data of two variables.
def swap(a,b):
    temp = a
    a=b
    b=temp
    print(a,b)

# 5. Write a python script to check wheather a given number is divisible by 5 or not.
def div(dig):
    last_char = dig[-1]
    if last_char == "0" or last_char == "5":
        print("divisible")

if __name__=="__main__":
    dig = input("enter word")
    div(dig)










