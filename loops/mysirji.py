# 1st program
def char(x):
    if x>0:
        print("positive")
    else:
        print("Non Positive")

"""2nd program- write a program to print grade obtained in a test. Take marks obtained from user and display the grade.
90<marks<= 100 A
80<marks<= 90  B
70<marks<= 80  C
60<marks<= 70  D
50<marks<= 60  E
below 50       F """

def score_card(mark):
    if mark>90 and mark<=100:
        print("A")
    elif mark>80 and mark<=90:
        print("B")
    elif mark>70 and mark<=80:
        print("C")
    elif mark>60 and mark<=70:
        print("D")
    elif mark>50 and mark<=60:
        print("E")
    else :
        print("F")

""" 3rd program write a program to check wheater a given number is even or odd"""
def oddeve(number):
    if number%2==0:
        print("Even")
    else:
        print("Odd")


if __name__=="__main__":
    number= int(input("Enter a number"))
    oddeve(number)


