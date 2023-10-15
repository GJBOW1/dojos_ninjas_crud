from flask_app.config.mysqlconnection import connectToMySQL

class Dojos:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def get_dojos(cls): 
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print(results)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_dojos_group(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos[0]
    
    @classmethod
    def delete_dojo(cls,data): 
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    @classmethod
    def update_dojo(cls,data):
        query = "UPDATE users SET name = %(name)s WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    @classmethod
    def show_dojo(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(results[0])
