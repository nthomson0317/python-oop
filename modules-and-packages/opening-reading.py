f = open('practice.txt','w+')
f.write('This is a test string')
f.close()


import os

print(os.getcwd())
#/Users/nicholas.thomson/Desktop/Development/python/modules-and-packages

print(os.listdir())
#['collections-module.py', 'errors-and-exceptions.py', 'pip-pypi.py', 'opening-reading.py', 'setdefault.py', 'practice.txt', 'errors-hw.py']

import shutil

shutil.move('practice.txt','/Users/nicholas.thomson')

os.listdir('/Users/nicholas.thomson')
#['collections-module.py', 'errors-and-exceptions.py', 'pip-pypi.py', 'opening-reading.py', 'setdefault.py', 'practice.txt', 'errors-hw.py']

