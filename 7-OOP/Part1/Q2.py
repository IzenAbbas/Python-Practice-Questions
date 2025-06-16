class BankAccount():
    def __init__(self,acNum,n,b):
        if type(acNum)!= int or type(n)!=str or (type(b)!=int and type(b)!=float) or b<0:
            raise TypeError('Invalid arguments for BankAccount()')
        self.accountNumber=acNum
        self.name=n
        self.balance=b
    
    def Deposit(self,amount):
        if (type(amount)==int or type(amount)==float) and amount>=0:
            self.balance+=amount
    
    def Withdrawal(self,amount):
        if (type(amount)==int or type(amount)==float) and amount>=0 and self.balance>=amount:
            self.balance-=amount

    def bankFees(self):
        self.balance-=self.balance*0.05

    def display(self):
        print('Account Number:',self.accountNumber)
        print('Account Name:',self.name)
        print('Account Balance:',self.balance, '₹')

newAccount = BankAccount(2178514584, "Mandy" , 2800)

newAccount.Withdrawal(700)

newAccount.Deposit(1000)

newAccount.display()