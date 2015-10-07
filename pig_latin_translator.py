print 'Welcome to the Pig Latin Translator!'
original = raw_input('Enter a word: ')
word = original.lower()
while word != 'quit':
    first = word[0]
    pyg = 'ay'
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)] # can write also [1:]
    if len(new_word) > 0 and new_word.isalpha():
        print new_word
    else:
        print 'I\'m sorry, please try again.' # prepare variable or variables for the next time through the loop
    word = raw_input('Enter a word: ') #this means it will print on the same line
    word = word.lower() #this just makes it lower case so that 'Quit' becomes 'quit'
