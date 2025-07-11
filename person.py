class Personal_details:
    
    def __init__(self, fname, lname, address):
        self.fname = fname
        self.lname = lname
        self.address = address

    def update_first_name(self, fname):
        self.fname = fname
    
    def update_last_name(self, lname):
        self.lname = lname
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        self.address = addr
        
    def get_address(self):
        return self.address
