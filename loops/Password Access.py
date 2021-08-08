secret = 'swordfish' #this the right password when we enter it shows "Authorized".
pw = ''
auth = False  #when the condition is false it continues to count
count = 0   #It ends at 0 after counts from 5 attempts to 0
max_attempt = 5 
while pw != secret:
    count += 1 #it decreases from 5 attempts to 0 by 1
    if count > max_attempt : break #Stopping th loop
    if count == 3: continue  # it will shortcut the 3 attempt
    pw = input(f"what's the password")
else : 
    auth = True #the conditon not applied
print('Authorized' if auth else 'Access Blocked!')