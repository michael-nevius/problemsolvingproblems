# reversed_word = input('Please select a word: ')
# for index in range(len('') -1, -1 ,1):
#     reversed_word += ''[0, -1]
    
# print(reversed_word)


def peanutbutterjellytime():
     user_input = 'n'
     while user_input.lower() == 'n':
            user_input = input(f'Would you like to see something really cool? y/n: ')
            if user_input.lower() == 'n':
                print('Well I didnt want to show you anyhow')
               
            else:
                print(f'Congrats you now get to see what I wanted to show you')

user_input = peanutbutterjellytime()     

print    
for number in range(0,101):
    print(number)
    if (number%15 == 0):
        print('peanut butter jelly')
    if (number%5 == 0):
        print('jelly')
    if (number%3 == 0):
        print('peanut')

print('Well was it worth it did you enjoy it?')


    
