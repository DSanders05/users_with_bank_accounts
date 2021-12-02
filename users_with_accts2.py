class User():
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
        self.access = BankAccount()


    def make_deposit(self, amount):
        print(f'{self.name} asks the teller to deposit ${amount}')
        self.access.execute_deposit(self.name,amount)
        return self

    def make_withdrawal(self,amount):
        print(f'{self.name} asks the teller to withdraw ${amount}')
        self.access.withdraw(self.name,amount)
        return self

    def request_check_bal(self):
        self.access.get_balance(self.name)
        return self

    def check_interest_total(self):
        self.access.apply_interest(self.name)
        return self

    def transfer_money(self,second_user,amount):
        self.access.execute_transfer(self.name, second_user, amount)
        return self


#indicate checking vs savings

class BankAccount():
    bank_name = 'The Big Bank'

    def __init__(self,account_name = 'checking'):
        self.name = account_name
        self.balance = 0
        

    def execute_deposit(self,name,amount):
        self.balance += amount
        print(f'The teller deposited ${amount} into {name}\'s account.')
        

    def withdraw(self,name,amount):
        self.balance -= amount
        print(f'The teller withdrew ${amount} from {name}\'s account.')
        

    def apply_interest(self,name):
        total_interest_applied = self.balance * .02
        self.balance *= 1.02
        print(f'After applying interest, {name}\'s account now has a balance of ${self.balance}')
        print(f'{name}\'s account has accrued ${total_interest_applied} thus far.\n')

    def get_balance(self,name):
        print(f'{name}\'s account balance is now ${self.balance}')


    def execute_transfer(self,account_name,second_user,amount):
        print(f'{account_name} elects to transfer money to {second_user.name}\'s bank account.')
        self.withdraw(account_name,amount)
        second_user.make_deposit(amount)
        

drake = User('Drake', 'drake@dojo.com')
mac = User('Mac','mac@dojo.com')

drake.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(200).check_interest_total().request_check_bal()
mac.make_deposit(400).make_deposit(600).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).check_interest_total()

# mac.make_deposit(800).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200).make_withdrawal(300).request_check_bal()
# drake.make_deposit(500).make_deposit(500).make_deposit(500).make_withdrawal(200).request_check_bal().check_interest_total()


