# Wizard-Pass
Wizard Pass is an all in one password strength analyzer, generator, and .zip file password cracker.

## Requirements
Requires Python to be installed on computer.

### How to use
Wizard Pass uses a commandline interface to work. The syntax options are: 

-a      --analyze            analyze a password and determine it's complexity
-c      --crack              attempt to crack the password of a .zip file using word lists by Daniel Miessler
-g      --generate           generate a random and complex password
-h      --help               prints helpful information.

Wordlist dictionary options:
10k              [quick] a wordlist containing only 10 thousand words to be used.
rockyou          [slow] a wordlist containing about 60 thousand words
10m              [slower] a wordlist containing 10 million words
all              [very slow] this option uses all wordlists in this program.
