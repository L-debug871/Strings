# program to tell Python to print a message a set ammount of times

def repeat(text, number):
    results = ''
    for i in range(number):
        results += text + '\n'
    return results


message = input("Enter the message:\n")
count = eval(input("Enter the message repeat count:\n"))
results = repeat(message,count)
print(f"{results}" )