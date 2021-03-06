<h1 align='center'>Wizard Pass</h1>

![Build](https://img.shields.io/badge/Build_Status-Complete-green)
![Python](https://img.shields.io/badge/Python-3-blue)

Wizard Pass is an all in one password strength analyzer, password generator, and file password cracker for PDF and zip 
files.


## Requirements
1) Python3 must be installed.
2) The Pip module pikepdf needs to be installed.
3) The Pip module pyperclip needs to be installed.

<b>Note:</b> Pyperclip makes use of the pbcopy and pbpaste commands on MacOS and the xclip or xsel commands in Linux 
all of which should be installed by default.


## Usage Guide
Wizard Pass uses a terminal interface. <br>
Syntax: &#60;command&#62; [file name when cracking or password for analysis]

<pre>
The commands are:
-a      --analyze            analyze a password and determine it's complexity
-g      --generate           generate a random and complex password
-h      --help               print helpful information
-p      --pdf                attempt to crack the password of a PDF file by brute force
-z      --zip                attempt to crack the password of a zip file by brute-force

Wordlist dictionary options:
10k              (quick a wordlist containing only 10 thousand words to be used
rockyou          (slow) a wordlist containing about 60 thousand words
10m              (slower) a wordlist containing 10 million words
all              (very slow) this option uses all wordlists in this program
</pre>

The rockyou.txt, 10 million word wordlist, and 10 thousand wordlist are all files obtained from 
[Daniel Miessler](https://github.com/danielmiessler). However there is also a file called "custom_wordlist.txt" in which
you can add your own words to be used in cracking the targeted file.


## Changes
8/12/2020 - Added a PDF password crack feature


## Known Issues
1) When cracking a zip file and using the large wordlists, some files may not be extracted properly and would
return an error because of a bug in the ZipFile module. Read more [here](https://github.com/python/cpython/pull/12242).
