import mysql.connector

if __name__ == '__main__':
    cnx = mysql.connector.connect(user='test_user', password='Test_user_1', host='dbi1.xxx.us-east-1.rds.amazonaws.com', database='db_users')
    cursor = cnx.cursor()
    select_users = "SELECT * FROM tbl_users"
    cursor.execute(select_users)
    for el in cursor:
        print("ID: {} ; FirstName: {}; LastName: {}".format(el[0], el[1], el[2]))

    cursor.close()
    cnx.close()
