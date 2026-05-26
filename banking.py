class banks:
    def __init__(self,listoftask) -> None:
        self.task=listoftask
    def depositamount(self):
        print("Enter the amount you want to deposit: ")
        for cash in self.cash:
            print(" *"+cash)
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

class Account:
    def savingaccount(self):
     balance = self.balance
     totalbalance = self.balance
     self.savingbalance =(( balance/totalbalance)*100)/12
     return self.savingbalance

    def currentaccount(self):
        balance = self.balance
        totalbalance = self.balance
        


class customer:
    def depositamount(self):
       self.cash = int(input("Enter the amount: "))
       return self.cash
    def withdraw(self):
        self.balance = int(input("Enter the amount: "))
        return self.balance
    
if __name__== "__main__":
    customer = customer()
    Account = Account()
    
      

