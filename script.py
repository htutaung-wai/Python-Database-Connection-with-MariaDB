import mysql.connector as mariadb
import getpass

hostname = input("Enter the hostname : ")
username = input("Enter the username : ")
database = input("Enter the database name : ")
password = getpass.getpass("Enter the password : ")
print("The variable details are")
print("------------------------------------")
print("Hostname : ",hostname)
print("Username : ",username)
print("Database : ",database)
print("Password : ",password)

con = mariadb.connect(hsot=hostname,user=username,database=database,password=password)

print("Connection Established Successfully!")
con.close()