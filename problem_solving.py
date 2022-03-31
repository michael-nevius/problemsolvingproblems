def get_first_last_letter (string):
    first_letter = string[0]
    last_letter = string[-1]
    first_and_last = first_letter + last_letter
    return first_and_last

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

ingredients = ['pepperoni', 'anchovies', 'mushrooms', 'pineapple', 'green peppers', 'sausage']
def search():
    user_input = input(f'What ingredient would you like to add to your pizza?: ')
    ingredient = ''
    while user_input != ingredient:
        for ingredient in ingredients:

            if user_input == ingredient:
                print('That sounds like a good pizza!')
                
            else:
                input(f'Umm how about no try again: ')    
                 
pizza_time = search()

def Reverse(list):
    new_lst = list[::-1]
    return new_lst
list = ['toyota', 'dodge', 'fiat', 'chevy', 'ford', 'porche', 'bicycle']     


print(Reverse(list))


def nametool():
    names = ['Rebecca', 'Sam', 'Bob', 'Dante', 'Monica', 'Brad']
    for i in names:
        if(len(i)) > 4:
            print(i)
nametool()