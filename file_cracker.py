import zipfile

password_list = []
wordlist_location = ['./Wordlists/custom_wordlist.txt', './Wordlists/10k_wordlist.txt',
                     './Wordlists/rockyou_wordlist.txt', './Wordlists/10m_wordlist.txt']


def choosing_wordlist(selected_wordlist):
    custom_file = open(wordlist_location[0])
    for line in custom_file.read().splitlines():
        password_list.append(line)
    custom_file.close()

    if selected_wordlist == '10k':
        file = open(wordlist_location[1])
        for line in file.read().splitlines():
            password_list.append(line)
        file.close()
    elif selected_wordlist == 'rockyou':
        file = open(wordlist_location[2])
        for line in file.read().splitlines():
            password_list.append(line)
        file.close()
    elif selected_wordlist == '10m':
        print('[!] This process will take some time.')
        file = open(wordlist_location[3])
        for line in file.read().splitlines():
            password_list.append(line)
        file.close()
    elif selected_wordlist == 'all':
        print('[!] This process will take a lot of time.')
        for file_location in wordlist_location:
            file = open(file_location)
            for line in file.read().splitlines():
                password_list.append(line)
            file.close()
    elif selected_wordlist == 'none':
        print('[!] No wordlist was selected. Refer to the manual with the -h or --help option.')


def crack_zip_file(zip_file):
    choice_condition = True
    cracked_password = ''
    target_file = zipfile.ZipFile(zip_file)

    while choice_condition:
        print('Select which dictionary to use.')
        print('\n')
        print('Dictionary options:')
        print('10k              [quick] a wordlist containing only 10 thousand words to be used.')
        print('rockyou          [slow] a wordlist containing about 60 thousand words')
        print('10m              [slower] a wordlist containing 10 million words')
        print('all              [very slow] this option uses all wordlists in this program.')
        print('none             uses no wordlist except the custom_wordlist.txt file')
        print('Note: Words in the "custom_wordlist.txt" file will always be the first wordlist to be used.')
        print('\n')

        choice = input('Which wordlist do you want to use? ')
        print('\n')

        if choice == '10k' or choice == 'rockyou' or choice == '10m' or choice == 'all' or 'none':
            choosing_wordlist(choice)
            choice_condition = False

    for password in password_list:
        try:
            target_file.extractall(pwd=bytes(password, 'utf-8'))
            cracked_password = password
        except RuntimeError:
            pass

    if cracked_password == '':
        print('[-] The password could not be found.')
    elif cracked_password != '':
        print('[+] File unzipped. The cracked password is: %s' % cracked_password)
