def lowercase(s):
    lower_case = ''
    for m in s:  
        if 'A' <= m <= 'Z': 
            lower = ord(m) - ord('A') + ord('a')  
            lower_case += chr(lower)  
        else:
            lower_case += m  
    return lower_case  

shout = input("Enter a shouty sentence:")
small_letters = lowercase(shout)
print(small_letters)