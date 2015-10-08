import hashlib
import sys
import os

def calc_md5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash

print(calc_md5('function.py'))
raw_input("\nPress any key to exit.")
