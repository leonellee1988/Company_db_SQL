import sqlite3

conection = sqlite3.connect("/home/bruce/Escritorio/Python/Kaggle/SQL_learning/data_base.db")

try:
    conection.execute(
    #"DROP TABLE employee"
    )
    print("The table has been deleted.")

except sqlite3.OperationalError:
    print("There was a problem, the table could not be deleted.")