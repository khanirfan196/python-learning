

class UserProfile:

    def __init__(self, name, email, city):
        self.name = name 
        self._email = email 
        self.city - city 

    @property
    def email(self):
        return self._email 
