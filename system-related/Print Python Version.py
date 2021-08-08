#A program to get the python version you are using

import sys

def main():
    v = sys.version_info
    print('Python Version : {}.{}.{}'.format(*v))
    
if __name__ == '__main__': main()