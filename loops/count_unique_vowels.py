def vowels(v):
    vowel_count ={}
    for i in v:
        if i in ["a","e","i","o","u"]:
            vowel_count[i]=i
    print(vowel_count)
    return len(vowel_count)

if __name__=="__main__":
    v=input("write")
    print(vowels(v))

