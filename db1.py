import mysql.connector
from mysql.connector import Error


# def create_connection(host_name, user_name, user_password, db):
def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='Saumya',
        password='Saumya@13',
        database='codevs')

    return connection


# query = "insert into cal(First,Second,Addition,substraction,multiply,division) values({},{},{add},{sub},{mult},{div})".format(
#    a, b, **result)


def execute_query(connection, query):

    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


#connection = create_connection()
#query = 'insert into cal(First,Second,Addition,substraction,multiply,division) values(1,7,8,-6,7,.33)'

#execute_query(connection, query)
