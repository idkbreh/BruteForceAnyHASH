
# BruteF0rc3ANYHASH !

*⚠️ disclaimer this project create for education how brute force work*


## Features

Obfuscate a text with sha256 , md5 or sha1

```py
from modules.obfuscator import Obfuscator 
""" method we have sha256 md5 sha1"""
# How to use 
target_word = Ob('Sky','sha256').hash()
print(target_word)

```

Compare and brute force

```py
# Create words.txt and put some word in there 

from modules.obfuscator import Obfuscator
from modules.brute import BruteForce 
list = ['Ant','Blue','Sky']
target_word = Obfuscator('Sky','sha256').hash()
print(f'target is {target_word}')
compare = BruteForce('words.txt',target_word).compare_hash()
print(compare)

```


## Authors

- [@BelloStick.ME](https://www.github.com/idkbreh)


## Badges



![Static Badge](https://img.shields.io/badge/BruteF0Rc3ANYHA5H-8A2BE2)

![MIT License](https://img.shields.io/badge/License-MIT-green.svg)



