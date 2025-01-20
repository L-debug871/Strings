def add_commas_and_full_stop(sentence):
    words = sentence.split()  
    sentence_with_commas = ', '.join(words)  
    sentence_with_full_stop = sentence_with_commas + '.'  
    return sentence_with_full_stop


sentence = input("Enter a sentence: ")
result = add_commas_and_full_stop(sentence)
print(result)
    