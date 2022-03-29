def peanutbutterjellytime():
     user_input = 'n'
     while user_input.lower() == 'n':
            oh_yeah = secretsauce()
            user_input = input(f'Would you like to see something really cool? y/n: ')
            if user_input.lower() == 'n':
                print('Well I didnt want to show you anyhow')
               
            else:
                print('Congrats you now get to see what I wanted to show you')

     return oh_yeah
     
def secretsauce(peanut):
        for number in range(0,101):
                 print(number)
                 if (number%15 == 0):
                  print('peanut butter jelly')
                 if (number%5 == 0):
                  print('jelly')
                 if (number%3 == 0):
                  print('peanut')
user_input = peanutbutterjellytime()
    
