from flask_app.config.mysqlconnection import connectToMySQL

class Ninjas:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]


    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def get_ninjas(cls): 
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print(results)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    
    @classmethod
    def delete_ninja(cls,data): 
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    @classmethod
    def update_ninja(cls,data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(age)s WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    @classmethod
    def show_ninja(cls,data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return results
    
    @classmethod
    def insert_ninja(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return results
    
    @classmethod
    def get_ninjas_dojo(cls,data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        ninjas_dojo = []
        for ninja in results:
            ninjas_dojo.append(cls(ninja))
        return ninjas_dojo