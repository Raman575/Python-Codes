""" 
SQL
create table Customer(
    cid int primary key auto_increment,
    name text,
    phone text, 
    email text
);
COMMANDS FOR SQL

create database mydatabase;
show database;
use mydatabase(create table Customer(
    cid int primary key auto_increment,
    name text,
    phone text, 
    email text);
show tables;
describe Customer;
insert into Customer values(null, 'Raman', '+91 9874563219', 'raman@gmail.com');
 select * from Customer;
 
 DATABASE CONNECTIVITY
 import mysql.connector as db
 #step1 - create connection with database 
 connection = db.connect(user = 'root',
                         password = ' ',
                         host = '127.0.0.1',
                         database= 'mydatabase'
             )
#step-2 Obtain cursor to perform sql opertions
cursor = connection.cursor()
#Step-3 Create sql statement
sql = "insert into Customer values"\
"(null, 'Raman', '+91 9874563219', 'raman@gmail.com');".format_map(vars(Customer))
#Step-4 Excute SQL command
cursor.excute(sql)
connection.commit()
print("Customer inserted")

    """
import mysql.connector as db

class Customer:
    def __init__(self):
        self.name = input("Enter customer name:")
        self.phone = input("Enter customer phone:")
        self.email = input("Enter customer email:")

def main():
    customer = Customer()
    print(vars(customer))

    connection = db.connect(user='root', password='Ramanjot@575', host='127.0.0.1', database='mydatabase')
    cursor = connection.cursor()
    sql = "insert into Customer values"\
"(null, 'Raman', '+91 9874563219', 'raman@gmail.com');".format_map(vars(Customer))
    data = (customer.name, customer.phone, customer.email)
    cursor.execute(sql, data)
    connection.commit()
    print("Customer inserted")

if __name__ == "__main__":
    main()