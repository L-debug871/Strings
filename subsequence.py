#define subsequence
#Lerato Moholo
#24/08/2024

def subsequence(original,new):
    j = 0 
    for char in original:
        if j<len(new) and char ==new[j]:
            j= j+1
        if j ==len(new):
            return True
    return j == len(new)
    
original = input("Enter the full string:\n")
new = input("Enter the subsequence to check for:\n")

if subsequence(original,new):
    print("The given substring is a subsequence of the full string.")
else:
    print("The given substring is not a subsequence of the full string.")
    