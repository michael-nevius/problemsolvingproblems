best_football_team = 'packers'
for character in best_football_team:
    print(character)

def peanutbutterjellytime():
     user_input = 'n'
     while user_input.lower() == 'n':
            user_input = input(f'Would you like to see something really cool? y/n: ')
            if user_input.lower() == 'n':
                print('Well I didnt want to show you anyhow')
               
            else:
                print(f'Congrats you now get to see what I wanted to show you')

     return user_input
def secret_sauce():     
    for number in range(0,101):
        print(number)
    if (number%15 == 0):
        print('peanut butter jelly')
    if (number%5 == 0):
        print('jelly')
    if (number%3 == 0):
        print('peanut')

user_input = peanutbutterjellytime()
print(f'{secret_sauce}')

    
