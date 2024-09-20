def vowels(e):
    list_even =[]
    for i in e:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            list_even.append(i)
    return list_even

def elegant_vowles(e):
    vowel_list =["a","e","i","o","u"]
    list_even =[]
    for i in e:
        if i in vowel_list:
            list_even.append(i)
    return list_even

def one_line(e):
    vowel_list =["a","e","i","o","u"]
    result_vowel =[i for i in e if i in vowel_list]
    return result_vowel

if __name__=="__main__":
    e= input("name")
    print(elegant_vowles(e))
    print(one_line(e))

    