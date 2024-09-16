from modules.obfuscator import Obfuscator as Ob
from modules.brute import BruteForce as Brf
list = ['Ant','Blue','Sky']
target_word = Ob('Sky','sha256').hash()
print(f'target is {target_word}')
compare = Brf('words.txt',target_word).compare_hash()
print(compare)