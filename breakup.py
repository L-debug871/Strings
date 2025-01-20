#Lerato Moholo
# A program to covert input to lower case then put commas after each word and a fullstop at end
#25/08/2024-28/08/2024

# definition of how to convert to lowercase
def lowercase(s):
    lower_case = ''
    for m in s:  
        if 'A' <= m <= 'Z': 
            lower = ord(m) - ord('A') + ord('a')  #use unicode numbers
            lower_case += chr(lower)  
        else:
            lower_case += m  
    return lower_case  

# definition of how to add commas and full stop to a sentence
def add_commas_and_full_stop(sentence):
    words = sentence.split()             #split the string
    sentence_with_commas = ', '.join(words)  #add commas and space 
    sentence_with_full_stop = sentence_with_commas + '.'  
    return sentence_with_full_stop


shout = input("Enter a sentence:\n")
small_letters = lowercase(shout)


sentence = small_letters
result = add_commas_and_full_stop(sentence)
print(f"The word list: {result}")
