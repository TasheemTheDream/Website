from flask_app.config.database import database

class User:
    def __init__(self, user_dict):
        self.id = user_dict["id"]
        self.email = user_dict["email"]
        self.user_name = user_dict["user_name"]
        self.password = user_dict["password"]
        self.files = []

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email=%(email)s"
        result = database().start_query(query)
        if len(result) < 1:
            return False
        return cls(result[0])


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        result = database().start_query(query)
        users = []
        for user_dict in result:
            users.append(cls(user_dict))

        return users
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (email, user_name, password) VALUES (%(email)s, %(user_name)s, %(password)s)"
        result = database().start_query(query)
        return result
        