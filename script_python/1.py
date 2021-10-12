
import os
# with open (r'/Users/jieli/Desktop/python\ projects') as f:

for dirpath, dirname, filename in os.walk('/Users/jieli/Desktop/python projects'):
    for name in dirname:
        print(name)
        print()