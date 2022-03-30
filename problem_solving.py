def reversed_word_tool():
    word = input('Please type a word that you would like to see reversed: ')
    for index in range(len(word) -1, -1 ,1):
            print(word[index])

    reversed_word = ''    
    for index in range (len(word) -1, -1, -1):
        reversed_word += word[index]

    print(reversed_word)

user_input = reversed_word_tool()


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

word = input("Please input a word you would like to have indexed.: ")

def final_word(word):
    for number in range(len(word)):
        print(number)
        print(word[number])

user_input = final_word(word)

    
