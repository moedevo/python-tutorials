
#We basically floor-divide the number by 10 until it is zero and add one to the count each time. 
#So 123 becomes 12, which becomes 1, then 0, giving you a digit count of 3. 
#Lines 7 and 10 initialize and increment that counter

def Counting(Number):
    Count = 0
    while(Number > 0):
        Number = Number // 10   
        Count = Count + 1    
    print("Number of Digits in a Given Number:", Count)
Counting(3543)

#Another Way

Number = "4454765"
digitCount = len(str(Number))
print(digitCount)