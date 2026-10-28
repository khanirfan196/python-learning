

class DatabaseConn:

    def __init__(self):
        pass 

    __HOST = "19.0.0.244.0"
    __PORT = "1227"
    __SERVICENAME = "test"

    def __connect_db(self):
        return "its a private method" 

    def connect_db(self):
        print(self.__connect_db())



conn = DatabaseConn()

# below call will throw error
# conn.__connect_db()

# accessing private method through instance method.
print(conn.connect_db())
