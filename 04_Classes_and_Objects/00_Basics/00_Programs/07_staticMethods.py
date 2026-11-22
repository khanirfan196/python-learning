
class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password 

    @staticmethod
    def staticmethod():
        method_type = "static"
        return f'This is a {method_type} method'


user = User("irfan", "irfan@gmail.com", "hello@123")

print(user.staticmethod())

print(User.staticmethod())


    