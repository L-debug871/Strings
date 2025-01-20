'''Lerato Moholo
messageframe.py
this code ecoporates functions
 draw a frame (made of the characters ‘+’, ‘-‘, and 
‘|’) around a message that has been repeated on consecutive lines. '''

def print_box(width,lenth,thickness):

    lenth = repeat_count + thickness * 2
    width = len(message)+ thickness * 2
    
    for a in range(thickness):
        print("|"*a + "+" + "-"*(width-2*a)+"+"+a*"|")
        
    for b in range(repeat_count):
        print("|"*thickness + " "+message + " "+thickness*"|")
    
    for c in range(thickness-1,-1,-1):
        print("|" * c + "+" + "-" *(width-2*c)+ "+"+ c*"|")
    
message= input("Enter the message:\n")
repeat_count= int(input("Enter the message repeat count:\n"))
thickness= int(input("Enter the frame thickness:\n"))

print_box(message,repeat_count,thickness)