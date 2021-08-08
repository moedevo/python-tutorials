#Creating a histogram from a given list of integers

def histogram (items): # We define the function
    for n in items:
        output = " " #Assign the output to empty in the begining
        times = n #Assign the times to n 
        while times > 0 : # this is to explain that times must be greater than 0
         output += "*" #Increasing the output by *
         times = times - 1 #Decrasing the n by 1
        print(output) #Shows output on the screen 
histogram([2,3,6,5]) # calling the function with numbers