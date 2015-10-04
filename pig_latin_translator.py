print 'Welcome to the Pig Latin Translator!'
original = raw_input('Enter a word: ')
pyg = 'ay'
word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_word[1:len(new_word)]
if len(new_word) > 0 and new_word.isalpha():
    print new_word
else:
    print 'I\'m sorry, please try again.'
