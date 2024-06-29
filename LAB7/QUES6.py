''' Take a sentence as input and reverse the order of words in the sentence. Display the original 
and the reversed sentences. '''


input_sentence = input("Enter a sentence: ")


words = input_sentence.split()


reversed_words = list(reversed(words))

reversed_sentence = ' '.join(reversed_words)


print("Original sentence:", input_sentence)
print("Reversed sentence:", reversed_sentence)
