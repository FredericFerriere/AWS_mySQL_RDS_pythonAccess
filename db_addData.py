import mysql.connector
import sys

if __name__ == '__main__':
    if len(sys.argv) > 2:
        firstName = sys.argv[1]
        lastName = sys.argv[2]
        cnx = mysql.connector.connect(user='test_user', password='Test_user_1', host='dbi1.xxx.us-east-1.rds.amazonaws.com', database='db_users')

        cursor = cnx.cursor()
        add_user = "INSERT INTO tbl_users (firstName, lastName) VALUES (%s, %s)"
        data_user = (firstName, lastName)

        cursor.execute(add_user, data_user)
        cnx.commit()

        cursor.close()
        cnx.close()
    else:
        print("please provide first name and last name as arguments")
