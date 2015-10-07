print ('How hot is the tea?')
temperature = input('Enter a value between 206 and 212: ')
while temperature > 205:
    print (temperature)
    temperature = temperature - 1
    print ('Let\'s add an ice cube.')
print ('The tea is cool enough to drink now.')
