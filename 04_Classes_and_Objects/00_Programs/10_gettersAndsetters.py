
# We can use only @property decorator to just fetch the attribute.
# If we want to set a new value to the attribute then 'setter' is required.
# The idea of using 'setter' is to perform validation on the data.
# When only @property is used, the attribute cannot be modified unless 'setter' is use.


class UserProfile:

    def __init__(self, name, email, city):
        self.name = name 
        self._email = email 
        self.city = city 

    @property
    def email(self):
        return self._email 

    @email.setter 
    def email(self, email):
        # here we can write email validation code
        # ex: a regex to properly check if the string is email
        self._email = email


if __name__ == "__main__":
    user01 = UserProfile("irfan", "irfan@gmail.com", "okc")

    print(f"Current user's email is: {user01.email}")

    print("Setting new email id....")

    user01.email = "irfankhan@gmail.com"

    print(f"Updated user's email is: {user01.email}")