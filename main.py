import getopt
import sys
import analysis_and_generator
import file_cracker


def usage():
    print(f'Password Analyzer and File Cracker')
    print(f'\n')

    print(f'Description:')
    print(f'This program is an all in one password analyzer, generator, and file password cracker '
          + 'for ".zip" files.')
    print(f'The wordlists used in this program were obtained from Daniel Miessler. However uou can also '
          + 'add your words to the "custom_wordlist.txt" file in the Wordlist directory to be used.')
    print(f'Note: Words in the "custom_wordlist.txt" file will always be the first wordlist to be used.')
    print(f'\n')

    print(f'Syntax commands:')
    print(f'-a      --analyze            analyze a password and determine it\'s complexity')
    print(f'-g      --generate           generate a random and complex password')
    print(f'-h      --help               print helpful information')
    print(f'-p      --pdf                attempt to crack the password of a PDF file')
    print(f'-z      --zip                attempt to crack the password of a zip file')
    print(f'\n')

    print(f'Dictionary options:')
    print(f'10k              [quick] a wordlist containing only 10 thousand words to be used.')
    print(f'rockyou          [slow] a wordlist containing about 60 thousand words')
    print(f'10m              [slower] a wordlist containing 10 million words')
    print(f'all              [very slow] this option uses all wordlists in this program.')
    print(f'\n')

    print(f'Author: https://www.github.com/FIRE-IN-THE-CODE')


def main():
    opts, args = getopt.getopt(sys.argv[1:], 'a:ghp:z:', ['analyze=', 'crack=', 'generate', 'help', 'pdf=', 'zip='])

    for o, a in opts:
        if o == '-a' or o == '--analyze':
            analysis_and_generator.analyze(a)
        elif o in ('-g', '--generate'):
            analysis_and_generator.password_generator()
        elif o in ('-h', '--help'):
            usage()
        elif o in ('-p', '--pdf'):
            try:
                file_cracker.crack_pdf_file(a)
            except FileNotFoundError:
                print(f'The PDF file {a} was not found. Is it in the same directory as this program?')
                exit(0)
        elif o in ('-z', '--zip'):
            try:
                file_cracker.crack_zip_file(a)
            except FileNotFoundError:
                print(f'The zip file {a} was not found. Is it in the same directory as this program?')
                exit(0)
        else:
            print(f'Select an option.')
            print('\n')
            usage()


if __name__ == '__main__':
    main()
