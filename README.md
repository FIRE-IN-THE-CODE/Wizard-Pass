# Wizard Pass
Wizard Pass is an all in one password strength analyzer, password generator, and .zip file password cracker.


## Requirements
Requires Python to be installed on computer.


### Usage Guide
Wizard Pass uses a commandline interface to work. <br>
Format: main.py &#60;command&#62; [zip file name when cracking]

<pre>
The syntax commands are:
-a      --analyze            analyze a password and determine it's complexity
-c      --crack              attempt to crack the password of a .zip file using word lists by Daniel Miessler
-g      --generate           generate a random and complex password
-h      --help               prints helpful information.

Wordlist dictionary options:
10k              (quick a wordlist containing only 10 thousand words to be used.
rockyou          (slow) a wordlist containing about 60 thousand words
10m              (slower) a wordlist containing 10 million words
all              (very slow) this option uses all wordlists in this program.
</pre>

The rockyou.txt, 10 million word wordlist, and 10 thousand wordlist are all files by [Daniel Miessler](https://github.com/danielmiessler). However there is also a file called "custom_wordlist.txt" which you can use to add your own words to be used to crack the zip file.


### Known Issues
1) When cracking a zip file, some files may not be extracted properly when using the large wordlists because of a bug in the ZipFile module.

Read more [here](https://github.com/python/cpython/pull/12242)