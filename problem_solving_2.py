def reversed_word_tool():
    word = input('Please type a word that you would like to see reversed: ')
    for index in range(len(word) -1, -1 ,1):
            print(word[index])

    reversed_word = ''    
    for index in range (len(word) -1, -1, -1):
        reversed_word += word[index]

    print(reversed_word)

user_input = reversed_word_tool()

capital = 'hello hello hello hello hello'

def capitalize_first_letter(string):
    new_string = ''
    n = ''
    string_count = 0
    for letter in string:
        if string.index(letter) == 0 and string_count == 0:
            new_string += letter.upper()
            string_count += 1
        elif letter == ' ':
            n = string_count + 1
            new_string += letter
            string_count += 1
        elif string_count == n:
            new_string += letter.upper()
            string_count += 1
        else:
            new_string += letter 
            string_count += 1   
    return new_string
capital_letter = capitalize_first_letter(capital)
print (capital_letter)


user_input = input(f'Please type a word you would like to see as a palindrome: ')

def palindrome(string):
    string = string.lower().replace(' ', '')
    reversed = ''
    for i in range(len(string), 0, -1):
        reversed += string[i-1]
    return string == reversed
print(palindrome(user_input))   


string = "aaabbbbbccccaacccbbbaaabbbaaa"

def addingnumberstoletters (string):
    new_string = ''
    repeat_letter = ''
    tight_string = ''
    old_letters = string[0]
    number_in_string = 1
    for letter in string:
        if letter == old_letters and len(string) != number_in_string:
            repeat_letter += letter
            number_in_string +=1
        elif len(string) == number_in_string:
            repeat_letter += letter
            tight_string = str(len(repeat_letter)) + repeat_letter[0]
            new_string += tight_string
        else: 
            tight_string = str(len(repeat_letter)) + repeat_letter[0]
            new_string += tight_string
            repeat_letter = letter
            old_letters = letter
            number_in_string +=1
    return new_string
new_string = addingnumberstoletters(string)
print(new_string)