#This program is to copy any binary files such as an image

def main():
    infile = open('berlin.jpg', 'rb') #this is an image we want to copy , we opened in read binary-mode
    outfile = open('berlin-copy.jpg', 'wb') #this is an output image , we opened in write binary-mode
    while True:
        buf = infile.read(11240) #buffer means the size of the image 
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.') #this means the process is done 

if __name__ == '__main__': main()
