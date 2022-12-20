import mysql.connector

from mysql.connector import connect, Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='1380@Dmin1380',
                                         database='telegram',
                                         auth_plugin='mysql_native_password')
    # cursor = connection.cursor()
    # show_db_query = "SHOW DATABASES"
    # cursor.execute(show_db_query)
    # for db in cursor:
    #     print(db)
except Error as e:
    print("Error while connecting to MySQL", e)

def main(client_sent):

    if client_sent == "i need user names":
        return get_user_names()
    
    if client_sent[:6] == "INSERT":
        return insert_delete(client_sent)

    if client_sent[:8] == "password":
        return send_password(client_sent)

    if client_sent[:22] == "SELECT * FROM MESSAGES":
        return get_all_messages(client_sent)

    if client_sent[:20] == "SELECT * FROM BLOCKS":
        return block_check(client_sent)
    
    if client_sent[:6] == "DELETE" :
        return insert_delete(client_sent)


def get_user_names():

    query = "SELECT * FROM USERS;"
    all_user_names = []
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        all_user_names.append(row[0])
    
    return all_user_names

def insert_delete(query):

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    
def send_password(client_sent):
    user_name = client_sent[9:]

    query = "SELECT PASSWORD FROM USERS WHERE USER_NAME = '" + user_name + "';"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    if(len(result) == 0):
        return ("NONE")
    password = result[0][0]
    return password

def get_all_messages(query):

    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def block_check(query):

    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) == 0 :
        return 0
    return 1
    