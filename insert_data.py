import sqlite3

conection = sqlite3.connect("/home/bruce/Escritorio/Python/Kaggle/SQL_learning/data_base.db")

try:
    
    conection.execute(

    #"INSERT INTO department(name, number_employees, manager, location) VALUES(?, ?, ?, ?)",("Human Resources", 2, "Paola Lee", "A")
    #"INSERT INTO department(name, number_employees, manager, location) VALUES(?, ?, ?, ?)",("IT", 2, "Bruce Hernández", "A")
    #"INSERT INTO department(name, number_employees, manager, location) VALUES(?, ?, ?, ?)",("Sales", 5, "Noemi Guzmán", "B")
    #"INSERT INTO department(name, number_employees, manager, location) VALUES(?, ?, ?, ?)",("Marketing", 3, "Johanan Hernández", "B")
    #"INSERT INTO department(name, number_employees, manager, location) VALUES(?, ?, ?, ?)",("Data analytics", 3, "Marcos Miranda", "B")
    #"INSERT INTO department(name, number_employees, manager, location) VALUES(?, ?, ?, ?)",("Procurement", 2, "Leonel Tiño", "A")
    #"INSERT INTO department(name, number_employees, manager, location) VALUES(?, ?, ?, ?)",("Accounting", 3, "Fabiola Lee", "A")
    #"INSERT INTO department(name, number_employees, manager, location) VALUES(?, ?, ?, ?)",("Management", 7, "Rodolfo Estrada", "C")
    
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Ricardo González", 35, 5, "Bachelor's degree", "Analyst", 5500.00, 1)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Paola Scholes", 25, 1, "High School", "Analyst Jr.", 3500.00, 1)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Luis Orozco", 28, 8, "Bachelor's degree", "Analyst", 6500.00, 2)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Ana Ordoñez", 20, 2, "High School", "Analyst Jr", 4000.00, 2)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Carolina Pellecer", 31, 6, "Bachelor's degree", "Sales agent", 8000.00, 3)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("José Azurdia", 29, 3, "Bachelor's degree", "Sales agent", 8000.00, 3)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Julio Sulecio", 40, 8, "Bachelor's degree", "Sales agent", 10000.00, 3)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Mario López", 25, 4, "Bachelor's degree", "Sales agent", 8000.00, 3)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Brenda Jimenez", 42, 10, "Bachelor's degree", "Sales agent", 11000.00, 3)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Moises Chiquito", 24, 1, "High School", "Analyst", 3500.00, 4)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Rocio Solorzano", 22, 2, "High School", "Analyst", 3500.00, 4)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Raúl Pérez", 35, 6, "Bachelor's degree", "Analyst", 5500.00, 4)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Manolo Miranda", 25, 3, "Bachelor's degree", "Analyst Jr.", 4500.00, 5)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Andrea Hernández", 19, 3, "High School", "Analyst Jr.", 3500.00, 5)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Karen Girón", 42, 8, "Bachelor's degree", "Analyst", 7500.00, 5)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Gerardo Corado", 26, 4, "Bachelor's degree", "Analyst Jr.", 7500.00, 6)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Juan Chiquita", 36, 7, "Bachelor's degree", "Analyst Jr.", 7500.00, 6)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Wendy Solorzano", 25, 2, "Bachelor's degree", "Analyst Jr.", 3500.00, 7)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Marielos Girón", 41, 2, "Bachelor's degree", "Analyst", 8500.00, 7)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Boris Cardoza", 33, 8, "High School", "Analyst", 9000.00, 7)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Paola Lee", 53, 12, "Ph.D.", "Manager", 25500.00, 8)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Bruce Hernández", 45, 9, "Bachelor's degree", "Manager", 20000.00, 8)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Noemi Guzmán", 50, 17, "Ph.D.", "Manager", 35500.00, 8)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Johanan Hernández", 43, 11, "Ph.D.", "Manager", 20000.00, 8)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Marcos Miranda", 45, 5, "Bacherlor's degree", "Manager", 31000.00, 8)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Leonel Tiño", 61, 21, "Ph.D.", "Manager", 30500.00, 8)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Fabiola Lee", 51, 6, "Ph.D.", "Manager", 20500.00, 8)
    #"INSERT INTO employee(name, age, time_in_company, education, position, salary, department_code) VALUES(?, ?, ?, ?, ?, ?, ?)",("Rodolfo Estrada", 65, 20, "Ph.D.", "Manager", 40500.00, 8)
    
    )
    print("The data was successfully recorded.")

except sqlite3.OperationalError:
    print("There was a problema, the data could not be recorded.")

conection.commit()
conection.close()