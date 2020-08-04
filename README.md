<h1 align='center'>Wizard Pass</h1>

![Build](https://img.shields.io/badge/Build_Status-Complete-green)
![Python](https://img.shields.io/badge/Python-3-blue)

Wizard Pass is an all in one password strength analyzer, password generator, and .zip file password cracker.


## Requirements
1) Requires Python and Pip to be installed on computer.
2) The Pip module pyperclip is used in this program which makes use of the pbcopy and pbpaste commands on MacOS and 
the xclip or xsel commands in Linux.


## Usage Guide
Wizard Pass uses a commandline interface to work. <br>
Syntax: &#60;command&#62; [zip file name when cracking]

<pre>
The commands are:
-a      --analyze            analyze a password and determine it's complexity
-c      --crack              attempt to crack the password of a .zip file using wordlists by Daniel Miessler
-g      --generate           generate a random and complex password
-h      --help               prints helpful information.

Wordlist dictionary options:
10k              (quick a wordlist containing only 10 thousand words to be used.
rockyou          (slow) a wordlist containing about 60 thousand words
10m              (slower) a wordlist containing 10 million words
all              (very slow) this option uses all wordlists in this program.
</pre>

The rockyou.txt, 10 million word wordlist, and 10 thousand wordlist are all files by [Daniel Miessler](https://github.com/danielmiessler). However there is also a file called "custom_wordlist.txt" which you can use to add your own words to be used to crack the zip file.


## Known Issues
1) When cracking a zip file and using the large wordlists, some files may not be extracted properly and return an error because of a bug in the ZipFile module. Read more [here](https://github.com/python/cpython/pull/12242)
