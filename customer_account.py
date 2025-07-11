from person import Personal_details

class CustomerAccount(Personal_details):
    def __init__(self, fname, lname, address, account_no, balance,type_of_account):
        super().__init__(fname,lname,address)
        self.account_no = account_no
        self.balance = float(balance)
        self.type_of_account = type_of_account
    
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
        else:
            print("\n invalid input\n")
            

        
    def withdraw(self, amount):

        if self.balance >= amount:
            self.balance-=amount
            print("Operation is succesful")
        else:
            print("\n insufficient balance\n")
        
        
        
        
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def get_account_type(self):
        return self.type_of_account
    
    def account_menu(self):
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Back")
        print (" ")
    
        option = input ("Choose your option: ")

        if option not in  ('1','2','3','4','5','6','7'):
             print("Please choose one of the selectable options.")
        else:
            return int(option)

    def print_details(self):
        
        print("First name: %s" %self.fname) 
        print("Last name: %s" %self.lname) 
        print("Account No: %s" %self.account_no)
        print("Account type: %s" %self.type_of_account)
        print("Address: %s" %self.address[0]) 
        print(" %s" %self.address[1])
        print(" %s" %self.address[2])
        print(" %s" %self.address[3]) 
        print(" ")
            
   
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                

                try:
                    amount = float(input("\nPlease enter amount to be deposited:  "))
                    if amount > 0:
                        self.deposit(amount)
                        self.print_balance()
                    else:
                        print("Incorrect Input!")
                    
                except ValueError:
                    print("\ninvalid input, Transaction failed! ")



            elif choice == 2:
                
                try:
                    self.print_balance()
                    amount_of_withdraw = float(input("\nPlease enter the amount of money you want to withdraw: "))
                    if amount_of_withdraw<0:
                        print("\ninvalid input, Transaction failed! ")
                    else:                    
                        self.withdraw(amount_of_withdraw)
                        self.print_balance()
                        
                except ValueError:
                    print("\ninvalid input, Transaction failed! ")
            
            elif choice == 3:
                
                self.print_balance()
                pass
            
            elif choice == 4:
                

                invalid = True
                while invalid:
                    fname = input("\n Enter new customer first name:  ")
                    fname = fname.strip()
                    if fname != '':
                        invalid = False
                        self.update_first_name(fname)
                    else:
                        print("field cant be blank!")


                invalid = True
                while invalid:
                    sname = input("\n Enter new customer last name:  ")
                    sname = sname.strip()
                    if sname != '':
                        invalid = False
                        self.update_last_name(sname)
                    else:
                        print("field cant be blank!")

            elif choice == 5:
                update_address = []
                number_of_house = input("Please enter your house number: ")
                name_of_street = input("Please enter your name of street: ")
                name_of_city = input("Please enter your name of city: ")
                number_of_post_code = input("Please enter your number of postcode: ")
                update_address.append(number_of_house)
                update_address.append(name_of_street)
                update_address.append(name_of_city)
                update_address.append(number_of_post_code)
                self.update_address(update_address)
                print(f"Your current address is: {update_address}")
                
                pass
            elif choice == 6:
                self.print_details()
                
            elif choice == 7:
                loop = 0
        print ("\n Exit account operations")


class saving_account(CustomerAccount):
    def __init__(self,*arg,**kwarg):
        super().__init__(*arg,**kwarg)
        self.interest_rate = 3.5 
        
    def get_interest_rate(self): 
        return self.interest_rate 
    

class normal_account(CustomerAccount):
    def __init__(self,*arg,**kwarg):
        super().__init__(*arg,**kwarg)
        self.overdraft = -750 
    
    def withdraw(self,amount):
        if (self.balance - amount) < self.overdraft:
            print("\nUnsuccesful action!")  
            print("You do not have enough money") 
        else:
            self.balance-=amount 
            