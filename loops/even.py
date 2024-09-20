def even_list(n):
    even =[]
    for i in range(1,n+1):
        if i%2==0:
            even.append(i)
    return even


if __name__=="__main__":
    n = int(input("enter here"))
    print(even_list(n))