import json
# class is like blueprint, object is final product
# eg plant class, cactus object

# create an interactive banking based system in which a client can keep track of their transactions


class Transaction:
    # init means initialize, means start
    # these are the params
    def __init__(self, title, amount, type, note=""):
        self.title = title
        self.amount = amount
        self.type = type
        self.note = note
        # these are the properties for the params(just a variable in a class)
        
    def display_info(self):
        return f"Transaction:\n Expense:{self.title} Amount{self.amount} Type{self.type} Note{self.note}\n"


class Bank:
    def __init__(self):
        self.wallet = []
    
    # Add
    def add_transaction(self,transaction):
        self.wallet.append(transaction)
    
    # Remove
    
    def remove_transaction(self,title):
        for transaction in self.wallet:
            if transaction.title == title:
                self.wallet.remove(transaction)
                return f"{title} has been removed"
            return f"{title} not found"
            
        
        
    # Display
    def display_transactions(self):
        #checking if wallet is empty
        if not self.wallet:
            return f"empty wallet"
        return f"\n".join([transaction.display_info() for transaction in self.wallet])
    # Search
    
    def search_wallet(self,query):
        found = [trans for trans in self.wallet if query.lower() in trans.title.lower() or query.lower() in trans.type.lower()]
        if not found:
            return f"no wallet transaction found"
        return "\n".join([transaction.display_info() for transaction in found])
        
        
    # Save
    def save_file(self,filename="wallet.json"):
        data = [{'Expense': transaction.title, 'Amount': transaction.amount, 'Type': transaction.type, 'Notes': transaction.note} for transaction in self.wallet]
        with open(filename,"w") as f:
            json.dump(data, f)

    
    # Load
    def load_file(self,filename="wallet.json"):
        try:
            with open(filename,"r") as f:
                data = json.load(f)
                self.wallet = [Transaction(trans['Expense'],
                trans['Amount'], trans['Type'], trans['Notes']) for trans in data] 
        except FileNotFoundError:
            print( "File not found")
            
          
def main():
    wallet = Bank()
    while True:
        print('Bank')
        print('1. Add a new transaction')
        print('2. Remove a transaction')
        print('3. Display a transaction')
        print('4. Search a transaction')
        print('5. Save transactions to file')
        print('6. Load transactions from file')
        print('7. Exit')
        choice = input('Enter a choice(1-8):')
        
        
        if choice == "1":
            title=input('enter title')
            amount= float(input('enter amount'))
            type=input('enter type(deposit expense)')
            transaction = Transaction(title, amount,type)
            wallet.add_transaction(transaction)
            print('Added')
            
        elif choice == "2":
            title=input('enter title')
            print(wallet.remove_transaction(title))
            
        elif choice == "3":
            print(wallet.display_transactions())
            
        elif choice == "4":
            query = input("Enter a title")
            print(wallet.search_wallet(query))
        
        elif choice == "5":
            wallet.save_file()
            print("saved")
            
        elif choice == "6":
            wallet.load_file()
            print("loaded")
            
            
        elif choice == "7":
            print('exiting')
            break
        
       
        else:
            print('error')
            
if __name__ == "__main__":
    main()