class Artist:
    'CLass Artist is used to define Artist Attribute'   
    def __init__(self, name, birth_of_date):
        self.name = name
        self.birth_of_date = birth_of_date
        
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def set_birth_of_date(self, birth_of_date):
        self.birth_of_date = birth_of_date
        
    def get_birth_of_date(self):
        return self.birth_of_date