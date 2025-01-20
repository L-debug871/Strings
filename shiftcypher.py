'''Lerato Moholo 24 August 2024
this code takes each letter in the original message and replacing it with one that is a set number of places further along 
the alphabet 
The number by which each letter is to be "shifted" is called the key.'''



message = input("Enter the message:\n") .split() # aaa bbb
key=eval(input("Enter the key:\n"))               #eg key = 3
new_str=''
new_list=[]
for word in message:              #extract 'aaa'
    count = len(word)               # len(aaa) = 3                
    for m in word:                 # extract 'a' from 'aaa'
        if 'a'<=m<='z' and count!=0 :
            uni_mail = ord(m) +key
            if uni_mail>122:
                uni_mail = ord(m)+key-26

            mail = chr(uni_mail)
            new_str+=mail
            count-=1
            if count == 0:
                new_str+=' '
                

result = " "
for i in new_str:
    result+= i 
    
print(f"Result:{result}",end=" ")
