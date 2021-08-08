
#writing a program to know if your balance is enough to withdraw

def withdraw_money(current_balance , amount): #we create the function #current_balance and amount are parameters 
    if  current_balance >= amount: #if statement 
        current_balance = current_balance - amount
        return current_balance

balance = withdraw_money(100,80)

if balance <= 50:
  print("Insufficent Balance!")
  print("You have to deposit enough money")
else:
  print("processing your withdrawal request")