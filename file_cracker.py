import zipfile
import pikepdf

password_list = []
wordlist_location = ['./Wordlists/custom_wordlist.txt', './Wordlists/10k_wordlist.txt',
                     './Wordlists/rockyou_wordlist.txt', './Wordlists/10m_wordlist.txt']


def choosing_wordlist():
    choice_condition = True

    custom_file = open(wordlist_location[0])
    for line in custom_file.read().splitlines():
        password_list.append(line)
    custom_file.close()

    while choice_condition:
        print(f'Select which dictionary to use.')
        print(f'\n')
        print(f'Dictionary options:')
        print(f'10k              [quick] a wordlist containing only 10 thousand words to be used.')
        print(f'rockyou          [slow] a wordlist containing about 60 thousand words')
        print(f'10m              [slower] a wordlist containing 10 million words')
        print(f'all              [very slow] this option uses all wordlists in this program.')
        print(f'none             uses no wordlist except the custom_wordlist.txt file')
        print(f'Note: Words in the "custom_wordlist.txt" file will always be the first wordlist to be used.')
        print('\n')

        selected_wordlist = input('Which wordlist do you want to use? ')
        print('\n')

        if selected_wordlist == '10k':
            file = open(wordlist_location[1])
            for line in file.read().splitlines():
                password_list.append(line)
            file.close()
            choice_condition = False
        elif selected_wordlist == 'rockyou':
            file = open(wordlist_location[2])
            for line in file.read().splitlines():
                password_list.append(line)
            file.close()
            choice_condition = False
        elif selected_wordlist == '10m':
            print(f'[!] This process will take some time.')
            file = open(wordlist_location[3])
            for line in file.read().splitlines():
                password_list.append(line)
            file.close()
            choice_condition = False
        elif selected_wordlist == 'all':
            print(f'[!] This process will take a lot of time.')
            for file_location in wordlist_location:
                file = open(file_location)
                for line in file.read().splitlines():
                    password_list.append(line)
                file.close()
                choice_condition = False
        elif selected_wordlist == 'none':
            print(f'[!] No wordlist was selected.')
            choice_condition = False


def crack_zip_file(zip_file):
    cracked_password = ''
    target_file = zipfile.ZipFile(zip_file)

    choosing_wordlist()

    for password in password_list:
        try:
            target_file.extractall(pwd=bytes(password, 'utf-8'))
            cracked_password = password
        except RuntimeError:
            pass

    if cracked_password == '':
        print(f'[-] The password could not be found.')
    elif cracked_password != '':
        print(f'[+] File unzipped. The cracked password is: {cracked_password}')


def crack_pdf_file(pdf_file):
    cracked_password = ''

    choosing_wordlist()

    for pass_code in password_list:
        try:
            pikepdf.open(pdf_file, password=pass_code)
            cracked_password = pass_code
        except pikepdf._qpdf.PasswordError:
            pass

    if cracked_password == '':
        print(f'[-] The password could not be found.')
    elif cracked_password != '':
        print(f'[+] The PDF file password has been cracked. The password is: {cracked_password}')
