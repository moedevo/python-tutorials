#This is a program to copy lines from file to file

def main():
    infile = open('lines.txt', 'rt') #this is the infile opened in read text-mode.
    outfile = open('lines-copy.txt', 'wt') #this is the outfile opened in write text-mode.
    for line in infile:
        print(line.rstrip(), file=outfile)  #rstrip() is used to remove any whitespaces
        print('.', end='', flush=True) #flush is used to disable writing at the end of lines
    outfile.close()
    print('\ndone.') #to show the process is done 

if __name__ == '__main__': main()