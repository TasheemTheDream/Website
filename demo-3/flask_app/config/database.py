import pymysql

class database:
    def __init__(self):
        self.connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "website",
            cursorclass= pymysql.cursors.DictCursor
        )

    def start_query(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
    
                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
