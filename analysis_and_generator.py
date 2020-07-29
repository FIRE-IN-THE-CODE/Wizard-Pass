import random

special_characters = ['!', '@', '#', '$', '%', '&', '*', '(', ')']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'
           + 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def analyze(given_password):
    if given_password == '':
        print('[!] No password was given.')
        exit(0)
    print('[!] Analyzing password.')

    password_length = len(given_password)
    special_character_count = 0
    number_attribute = False
    upper_case_attribute = False
    lower_case_attribute = False
    strength_counter = 0

    for i in given_password:
        for x in special_characters:
            if i == x:
                special_character_count += 1
        for x in numbers:
            if i == x:
                number_attribute = True
        for x in letters:
            if i == x:
                lower_case_attribute = True
            elif i == x.upper():
                upper_case_attribute = True

    if upper_case_attribute and lower_case_attribute:
        strength_counter += 1
    if number_attribute:
        strength_counter += 1
    strength_counter += special_character_count

    if password_length < 9:
        print('[-] A password less than 8 characters in length is very weak.')
    elif password_length > 8 and strength_counter < 3:
        print('[-] Your password is weak and should be more complex.')
    elif password_length > 8 and 2 < strength_counter < 4:
        print('[+] Your password is moderately strong.')
    elif password_length > 8 and strength_counter > 4:
        print('[+] Your password is very complex.')


def password_generator():
    generated_password = ''
    password_list = []
    generated_length = 0
    selected_chance = 0
    password_length_rule = int(input('What is the desired length of your password (in a number)?: '))
    special_character_rule = input('Are special characters such as "!" and "$" allowed (y/n)?: ')

    special_character_rule = special_character_rule.lower()

    while generated_length != password_length_rule:
        if special_character_rule == 'y':
            selected_chance = random.randrange(1, 150)
        elif special_character_rule == 'n':
            selected_chance = random.randrange(1, 100)

        if 0 < selected_chance < 51:
            letter_casing_chance = random.randrange(1, 100)
            if 0 < letter_casing_chance < 51:
                password_list.append(letters[random.randrange(0, 24)].lower())
            elif 50 < letter_casing_chance < 101:
                password_list.append(letters[random.randrange(0, 24)].upper())
        elif 50 < selected_chance < 101:
            password_list.append(numbers[random.randrange(0, 9)])
        elif 100 < selected_chance < 151:
            password_list.append(special_characters[random.randrange(0, 8)])

        generated_length += 1

    for i in password_list:
        generated_password += i

    print('[+] Your generated password is: %s' % generated_password)

    analyze(generated_password)
