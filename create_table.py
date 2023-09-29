import sqlite3

conection = sqlite3.connect("/home/bruce/Escritorio/Python/Kaggle/SQL_learning/data_base.db")

try:
    
    conection.execute(
        
    #"""
    #CREATE TABLE department(
    #    code INTEGER PRIMARY KEY AUTOINCREMENT,
    #    name TEXT NOT NULL,
    #    number_employees INTEGER NOT NULL,
    #    manager TEXT NOT NULL,
    #    location TEXT NOT NULL
    #)
    #"""
    
    #"""
    #CREATE TABLE employee(
    #    code INTEGER PRIMARY KEY AUTOINCREMENT,
    #    name TEXT NOT NULL,
    #    age INTEGER NOT NULL,
    #    time_in_company INTEGER NOT NULL,
    #    education TEXT NOT NULL,
    #    position TEXT NOT NULL,
    #    salary FLOAT NOT NULL,
    #    department_code INTEGER NOT NULL,
    #    FOREIGN KEY (department_code) REFERENCES department(code)
    #)
    #"""
    )
    print("The table has been created successfully.")

except sqlite3.OperationalError:
    print("There was a problem, the table could not be created.")

conection.close()