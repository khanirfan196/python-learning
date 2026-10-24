

class User:

    user_count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password 
        User.user_count += 1 

    def display_user(self):
        return f"User name is {self.name}, email: {self.email}."


user1 = User("irfan", "irfan@gmail.com", "123@hello")
user2 = User("rayyan", "rayyan@gmail.com", "rayyan@hello")

print(user1.display_user())
print(user2.display_user())
# User.user_count
print("Total users: ", str(User.user_count))
# trying to access class attribute through instance
print(f"Attribute call from instance 1 - {user1.user_count}")
print(f"Attribute call from instance 2 - {user2.user_count}")
# Class attribute can be access from instances too but 
# it is conventional to not call them, instead call only through class itself.

        

    