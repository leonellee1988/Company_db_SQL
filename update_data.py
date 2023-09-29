import sqlite3

conection = sqlite3.connect("/home/bruce/Escritorio/Python/Kaggle/SQL_learning/data_base.db")

try:
    conection.execute(
    """
    UPDATE employee
    SET education = "Bachelor's degree"
    WHERE code = 25
    """
    )
    print("The data has been changed successfully.")

except sqlite3.OperationalError:
    print("There was a problem, the data could not be changed.")

conection.commit()
conection.close()