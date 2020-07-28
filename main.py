import getopt
import sys
import analysis_and_generator
import file_cracker


def manual():
    print('Password Analyzer and File Cracker')
    print('\n')

    print('Description:')
    print('This program is an all in one password analyzer, generator, and file password cracker '
          + 'for ".zip" files.')
    print('The wordlists used in this program were obtained from Daniel Miessler. However uou can also '
          + 'add your words to the "custom_wordlist.txt" file in the Wordlist directory to be used.')
    print('\n')

    print('Syntax:')
    print('-a      --analyze            analyze a password and determine it\'s complexity')
    print('-c      --crack              attempt to crack the password of a .zip file using word lists by Daniel '
          + 'Miessler')
    print('-g      --generate           generate a random and complex password')
    print('-h      --help               prints helpful information.')
    print('\n')

    print('Dictionary options:')
    print('10k              [quick] a wordlist containing only 10 thousand words to be used.')
    print('rockyou          [slow] a wordlist containing about 60 thousand words')
    print('10m              [slower] a wordlist containing 10 million words')
    print('all              [very slow] this option uses all wordlists in this program.')
    print('Note: Words in the "custom_wordlist.txt" file will always be the first wordlist to be used.')
    print('\n')

    print('Author: www.github.com/FIRE-IN-THE-CODE')


def main():
    opts, args = getopt.getopt(sys.argv[1:], 'a:c:ghs:', ['analyze=', 'crack=', 'generate', 'help', 'select='])

    for o, a in opts:
        if o == '-a' or o == '--analyze':
            analysis_and_generator.analyze(a)
        elif o in ('-c', '--crack'):
            file_cracker.crack_zip_file(a)
        elif o in ('-g', '--generate'):
            analysis_and_generator.password_generator()
        elif o in ('-h', 'help'):
            manual()
        else:
            print('Select an option.')
            print('\n')
            manual()


if __name__ == '__main__':
    main()
