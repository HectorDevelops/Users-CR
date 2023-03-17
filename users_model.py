from mysqlconnection import connectToMySQL

#  Creating a global variable to avoid making typos when connecting to MySQL
DATABASE = 'users_schema_2.0'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Creating this classmethod to get all current users in our database 
    @classmethod
    def get_all(cls):
        # Storing our MySQL queries into a ariable to query our database
        query = "SELECT * FROM users;"

        # Storing our connection and queries from the databse to begin instantiating our list of dictionaries
        results = connectToMySQL(DATABASE).query_db(query)
        # For terminal view
        print(results)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            #  instantiating each of the row results from the database list that was returned
            this_user = cls(user)
            users.append(this_user)
        return users
    
    # Creating this class method to create new users in our database 
    @classmethod 
    def create_one_user(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email)
            VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        #  Optional print statement - mainly used to see the output in the terminal 
        print(results)
        return results 




