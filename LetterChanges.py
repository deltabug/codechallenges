def LetterChanges(str): 
    index=0
    endstr=""
    vowels=("a","e","i","o","u")
    while index < len(str):
        letter = str[index]
        x = chr(ord(letter) + 1)
        if x in vowels:
            endstr += x.upper()
        else:
            endstr += x
        index = index + 1
    return endstr
# keep this function call here  
print LetterChanges(raw_input())
