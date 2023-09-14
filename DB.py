#Creating New DB file
import sqlite3
conn=sqlite3.connect('Custumor_Database.db')
cursor=conn.cursor()
cursor.execute("create table Customer_Details(Accno long int,fullname text,type text,DOB int,mobileno int,gender text,nationality text,KYC text,PIN int)")
conn.commit()
conn.close()
