
#writing a program to calculate the balance after withdraw.

def withdraw_money(current_balance , amount): #we create the function #current_balance and amount are parameters 
    if  current_balance >= amount: #if statement 
        current_balance = current_balance - amount
        print("the balance is", current_balance)
withdraw_money(100,80)


