from flask_app.config.database import database
from flask import flash
import re

allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Login:
    
    def __init__(self, user_dict):
        self.first_name = user_dict['first_names']
        self.last_name = user_dict['last_names']
        self.email =  user_dict['emails']
        self.id = user_dict['id']
        self.password = user_dict['passwords']
    
    @classmethod
    def acquire_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        person = database().start_query(query, data)
        result = []
        for user_dictionary in person:
            user_obj = cls(user_dictionary)
            result.append(user_obj)
        return result[0]

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"
        users = database().start_query(query)
        result = []
        for user_dictionary in users:
            user_obj = Login(user_dictionary)
            result.append(user_obj)
            print (result)
        return result
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE emails = %(Email)s;"
        result = database().start_query(query, data)
        print(result)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @staticmethod
    def validate_order(data):
        val_first= set((data["Fname"]))
        val_last= set((data["Lname"]))
        # val_email= set((data["email"]))
        # val_password= set((data["password"]))
        is_valid = True
        query = "SELECT * FROM users WHERE emails = %(Email)s;"
        result = database().start_query(query, data)
        if len(data["Fname"]) < 2:
            flash("Please make sure the first name is at least 2 letters", "register")
            is_valid = False
        if not val_first.issubset(allowed_chars):
            flash("Only use Alphabet characters for First Name", "register")
            is_valid = False
        if len(data["Lname"]) < 2:
            flash("Please make sure the last name is at least 2 letters", "register")
            is_valid = False
        if not val_last.issubset(allowed_chars):
            flash("Only use Alphabet characters for Last Name", "register")
            is_valid = False
        if not EMAIL_REGEX.match(data['Email']): 
            flash("Invalid email address!", "register")
            is_valid = False
        if len(result) >= 1:
            flash("Email is already in use! Please choose another one!", "register")
            is_valid = False
        if len(data["Password"]) < 8:
            flash("Please make sure the password is at least 8 letters", "register")
            is_valid = False
        if data["Password"] != data["ConPassword"]:
            flash("Passwords do not match!", "register")
            is_valid = False
        return is_valid
    
    @classmethod
    def register(cls, data):
        query = "INSERT INTO users (first_names, last_names, emails, passwords) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return database().start_query(query, data)
    
    # # @classmethod
    # def get_orders_with_cookies(cls):
    #     query = "SELECT * FROM cookie_orders.order  LEFT JOIN cookie_orders.cookies on order.cookies_id = cookies.id;  "
    #     result = database().start_query(query)
    #     print("B",result)
    #     orders = []
    #     for row in result:
    #         this_order = Cookie(row)
    #         order_data = {
    #             "id": row['id'],
    #             "Name": row['Name'],
    #             "box_count": row['box_count']
                
    #         }
    #         cookies.order.append(order.Order(order_data))
    #         orders.append(cookies)
    #     return orders

    @classmethod
    def get_orders_with_cookies(cls):
        query = "SELECT * FROM cookie_orders.order  LEFT JOIN cookie_orders.cookies on order.cookies_id = cookies.id;  "
        result = database().start_query(query)
        print("A",result)
        orders = []
        for graph in result:
            for key in graph.keys():
                print(key)
            this_order = order.Order(graph)
            cookie_data = {
                "id": graph['cookies.id'],
                "cookie": graph['cookie'],
                "created_at": graph["cookies.created_at"],
                "updated_at": graph["cookies.updated_at"]
            }
            this_order.cookie = cls(cookie_data)
            orders.append(this_order)
        return orders



