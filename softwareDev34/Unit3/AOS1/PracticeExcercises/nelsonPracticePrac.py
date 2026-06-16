

class BankAccount:
    def DisplayMenu(self):
        decision = input('Choose operation: 1. Deposit 2. Withdraw 3. Check Balance 4. Exit: ')

        if decision == '1':
            self.deposit()
        elif decision == '2':
            self.withdraw()
        elif decision == '3':
            self.checkBalance()
        elif decision == '4':
            print("Thank you for using our services!")
            exit()
        else:
            print("Invalid choice. Please try again.")
            self.DisplayMenu()

    
    def deposit(self, amount):
        amount = float(input('Enter amount to deposit: '))
        self.balance += amount
        print(f"Your new balance is: ${self.balance:.2f}")

    