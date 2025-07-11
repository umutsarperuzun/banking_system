from customer_account import *
from admin import Admin
import json
import sys

accounts_list = []
admins_list = []

class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()

    
    def load_bank_data(self):

        test_file = "bank_information_storage.json"

        try:
            open(test_file)
        except FileNotFoundError:
            print("\nAttention: No information found.\n") 
            sys.exit()
        else: 
            file = test_file
   

    
 

        with open(file, "r" ) as json_file:
            my_data = json.load(json_file)
            my_customer_list = my_data["customers"]
            my_admin_list = my_data["admins"]

            for customer in my_customer_list:
                fname = customer["fname"]
                lname = customer["lname"]
                address = customer["address"]
                account_no = customer["account_no"]
                balance = customer["balance"]
                type_of_account = customer["account_type"]
                
                if customer["account_type"] == "saving_account":
                    item_of_customer = saving_account(fname, lname, address, account_no, balance,type_of_account)
                    self.accounts_list.append(item_of_customer)
                elif customer["account_type"] == "normal_account":
                    item_of_customer = normal_account(fname, lname, address, account_no, balance,type_of_account)
                    self.accounts_list.append(item_of_customer)
                else:
                    print("Bank account type not found!!!") 


            for admin in my_admin_list:
                fname = admin["fname"]
                lname = admin["lname"]
                address = admin["address"]
                user_name = admin["user_name"]
                password= admin["password"]
                full_rights= admin["full_rights"]

                item_of_admin = Admin (fname,lname,address,user_name,password,full_rights)
                self.admins_list.append(item_of_admin)
            
        
    def update_bank_data(self):

        new_bank_data = { "customers":[], "admins":[] }

        for customer_object in self.accounts_list:
            fname = customer_object.get_first_name()
            lname = customer_object.get_last_name()
            address = customer_object.get_address()
            account_no = customer_object.get_account_no()
            balance = customer_object.get_balance()
            type_of_account = customer_object.get_account_type()

            customer = {
                        "fname": fname ,
                        "lname": lname,
                        "address": address,
                        "account_no": account_no,
                        "balance": balance,
                        "account_type": type_of_account
                    }
            
            new_bank_data["customers"].append(customer)

        for admin_object in self.admins_list:
            fname = admin_object.get_first_name()
            lname = admin_object.get_last_name()
            address = admin_object.get_address()
            user_name = admin_object.get_username()
            password =  admin_object.get_password()
            full_rights = admin_object.has_full_admin_right()

            admin = {
                        "fname": fname ,
                        "lname": lname,
                        "address": address,
                        "user_name":user_name,
                        "password": password,
                        "full_rights": full_rights
                    }
            
            new_bank_data["admins"].append(admin)
            

        

        with open("updated_bank_info.json", mode="w") as file:
            json.dump(new_bank_data, file, indent=4)
        

    def search_admins_by_name(self, admin_username):
        
        found_admin = None
        for a in self.admins_list:
            username = a.get_username()

            if username == admin_username:
                found_admin = a
                break
        if found_admin == None:
            print("\n The Admin %s does not exist! Try again ...\n"%admin_username)
        return found_admin
         
        
    def search_customers_by_name(self, customer_lname):
        
        found_customer = None
        for b in self.accounts_list:
            c_lastname = b.get_last_name()
            if c_lastname.title() == customer_lname.title():
                found_customer = b
                break
        if found_customer == None:
            print("\n The Customer %s does not exist! Try again...\n"%customer_lname)
        return found_customer
                
        

    def main_menu(self):
        
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Quit Python Bank System")
        print (" ")
        wrong_login_attempt = True
        while wrong_login_attempt:

            option = input ("Choose your option: ")
            if option in ("1","2"):
                return int(option)
            else:
                print("invalid option, try again")   
                return self.main_menu()


    def run_main_options(self):
        loop = 1
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj, passed = self.admin_login(username.strip(), password)
                print(msg)
                if admin_obj != None and passed == "pass":
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
        print ("\n Thank-You for stopping by the bank!")


    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
        
        account_sending_money = self.search_customers_by_name(sender_lname.strip())
        account_receiving_money = self.search_customers_by_name(receiver_lname.strip())
        
        if account_sending_money == None:
            print("\nSorry,there is no such account")
            return
        if account_receiving_money == None:
            print("\nSorry,there is no such account")
            return
        
        if account_sending_money == account_receiving_money:
            print("\nsender account cant be receiver account!")
            return

        if account_sending_money.get_balance() < amount:
            print("\nThere is not enough money in the account")
            return
        
        if amount > 0:
            account_sending_money.withdraw(amount)
            account_receiving_money.deposit(amount)#
            print(f"£{amount} Sent from {account_sending_money.get_first_name()} {account_sending_money.get_last_name()} to {account_receiving_money.get_first_name()} {account_receiving_money.get_last_name()} successfully")
        else: 
            print("\nPlease make sure that the value you enter is a positive number.")

    def admin_login(self, username, password):
        
        found_admin = self.search_admins_by_name(username)
        msg = "\nUnsuccessful login attempt"
        passed = "Unsuccessful"
        if found_admin != None:
            if found_admin.get_password()==password:
                msg = "\n Access to the system has been achieved"
                passed = "pass"
            else:
                passed = "Unsuccessful"
        return msg,found_admin,passed
        

    def admin_menu(self, admin_obj):
        
        print (" ")
        print ("Welcome Admin %s %s : Avilable options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Transfer money")
        print ("2) Customer account operations & profile settings")
        print ("3) Delete customer")
        print ("4) Print all customers detail")
        print ("5) Change to Admin name")
        print ("6) Change to Admin address")
        print ("7) Management Report")
        print ("8) Sign out")        
        print (" ")
        
        
        try: 
            option = int(input ("Choose your option: "))
            if option >=9:
                print("\n INVALID INPUT, SELECT AVAILABLE OPTIONS!")
            else:
                return option
        except: print("\n INVALID INPUT, SELECT AVAILABLE OPTIONS")


    def run_admin_options(self, admin_obj):                                
        loop = 1
        while loop == 1:

            self.update_bank_data()
            choice = self.admin_menu(admin_obj)


            if choice == 1:
                sender_lname = input("\nPlease input sender surname: ")

                try:
                    amount = float(input("\nPlease input the amount to be transferred: "))
                except ValueError:
                    print("invalid input")
                else:                
                    receiver_lname = input("\nPlease input receiver surname: ")
                    receiver_account_no = None
                    self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)                    
            
            elif choice == 2:
                
                customer_name = input("\nPlease input customer surname: ")
                customer_account = self.search_customers_by_name(customer_name)
                if customer_account != None:
                    customer_account.run_account_options()
            
            elif choice == 3:
                if admin_obj.has_full_admin_right():
                    deposit_customer_name = input("Please enter the surname of the account you want to delete: ")
                    deposit_customer_account = self.search_customers_by_name(deposit_customer_name)
                    if deposit_customer_account !=None:
                        self.accounts_list.remove(deposit_customer_account)
                        print(f"{deposit_customer_account.get_first_name()} {deposit_customer_account.get_last_name()} Successfully deleted from the system")
                    else:
                        print("Account not found.")                
                else:
                    print("You do not have the necessary permissions.")
                
                
            
            elif choice == 4:
                self.print_all_accounts_details()
            
            elif choice == 5:
                new_first_name = input("Please write the new first name of the admin: ")
                admin_obj.update_first_name(new_first_name)
                new_last_name = input("Please write the new last name of the admin: ")
                admin_obj.update_last_name(new_last_name)
                
    
            elif choice == 6:
                updated_address = []
                number_of_the_house = input("Please write to the house number: ")
                name_of_the_street = input("Please write to the street name: ")
                name_of_city = input("Please write to the city name: ")
                number_of_postcode = input("Please write to postcode: ")

                updated_address = [number_of_the_house,name_of_the_street,name_of_city,number_of_postcode]
                admin_obj.update_address(updated_address)
                print("")
                print(f"Your new address is: {updated_address} ")

                
            elif choice == 7: 
                print(f"There are totaly {len(self.accounts_list)} customers.")
                
                total_money = []

                for customer in self.accounts_list:
                    money = customer.get_balance()
                    total_money.append(money)
                
                print(f"There is £{sum(total_money)} in this banking system.")
                

                total_money = []

                for customer in self.accounts_list:
                    if customer.get_account_type() == "saving_account":
                        money = customer.get_balance()
                        total_money.append(money)

                total_interest = sum(total_money)*(3.5/100)
                    
                print(f"Total of interest is £{total_interest:.2f} in this banking system ")

                overdraft_money = []

                for customer in self.accounts_list:
                    if customer.get_account_type() == "normal_account" and customer.get_balance() <= 0:
                        money = customer.get_balance()
                        overdraft_money.append(money)
                
                total_overdraft_money = sum(overdraft_money)
                
                print(f"Total of overdraft money is £{(-1)*total_overdraft_money:.2f} in this banking system ")


                        
                        
                        
            
                





            elif choice == 8:

                loop = 0
                print ("\n Exit account operations")  
            

    def print_all_accounts_details(self):
           
            i = 0
            for c in self.accounts_list:
                i+=1
                print('\n %d. ' %i, end = ' ')
                c.print_details()
                print("------------------------")


app = BankSystem()
app.run_main_options()
