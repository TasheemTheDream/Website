from flask_app.config.database import database

class File:
    def __init__(self, file_dict):
        self.id = file_dict["id"]
        self.file_name = file_dict["file_name"]
        self.size = file_dict["size"]
        self.extension = file_dict["extension"]
        self.name = file_dict["names"]
        self.studio = file_dict["studios"]
        self.producer = file_dict["producers"]
        self.air_date = file_dict["air_dates"]
        self.episode_count = file_dict["episode_count"]
        self.description = file_dict["descriptions"]

    
    @classmethod
    def save(cls, data):
        query = """INSERT INTO animes (file_name, size, extension, names, studios, producers, air_dates, episode_count, descriptions)
        VALUES (%(file_name)s, %(size)s, %(extension)s, %(anime_name)s, %(studio)s, %(producer)s, %(air_date)s, %(episode_count)s, %(description)s )"""
        result = database().start_query(query, data)
        return result
        
    @classmethod
    def get_all(cls, page):
        query = "SELECT * FROM animes LIMIT 6 OFFSET %(page)s "
        data = {
            "page": page
        }
        results = database().start_query(query, data)
        files = []
        for file in results:
            file_obj = File(file)
            files.append(file_obj)
            print(files)

        return files
    
    @classmethod
    def get_all_with_user(cls, user_id):
        query = "SELECT * FROM animes WHERE user_id=%(user_id)s"
        data = {
            "user_id": user_id
        }
        results = database().start_query(query, data)
        files = []
        for file in results:
            files.append(cls(file))

        return files
    
    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM animes WHERE id= %(id)s "
        data = {
            "id": id
        }
        results = database().start_query(query, data)
        files = []
        for file in results:
            file_obj = File(file)
            files.append(file_obj)
            print(files)

        return files[0]