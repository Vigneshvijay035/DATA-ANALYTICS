import pyodbc
import pandas as pd
from tabulate import tabulate

# SQL Server Connection Details
server = r'DESKTOP-TL5RR8B\SQLEXPRESS'  # Replace with your actual server
database = 'master'

# Connection string
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

# Establish connection
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Connected to SQL Server Successfully")
except pyodbc.Error as e:
    print(f"Connection Error: {e}")
    exit()


def insert():
    """Insert new data into FOOD_MENU table"""
    # ITEM_CODE = int(input("Item_code: "))  # item code is given as identity so 2 parameters passed
    FOOD_ITEM = input("Food_item: ")
    PRICE = int(input("Price: "))
    # DATED = input("Enter DATE (YYYY-MM-DD): ")

    sql = "INSERT INTO FOOD_MENU (FOOD_ITEM, PRICE) VALUES (?, ?)"
    values = (FOOD_ITEM, PRICE)
    cursor.execute(sql, values)
    conn.commit()
    print("Data Inserted Successfully")


def update():
    """Update existing record in sales_data table"""
    # ID = input("Enter ID to Update: ")
    ITEM_CODE = input("Enter ITEM_CODE where the Menu to be updated: ")
    FOOD_ITEM = input("Enter New FOOD_ITEM: ")
    PRICE = input("Enter New PRICE: ")
    # DATED = input("Enter New DATE (YYYY-MM-DD): ")

    # sql = "UPDATE sales_data SET MATERAL = ?, QTY = ?, MATERIAL_TYPE = ?, DATED = ? WHERE ID = ?"
    sql = "UPDATE FOOD_MENU SET FOOD_ITEM = ?, PRICE = ? where ITEM_CODE=?"
    values = (FOOD_ITEM,PRICE,ITEM_CODE)
    cursor.execute(sql, values)
    conn.commit()
    print("Data Updated Successfully")


def view():
    """Fetch and display all records from sales_data table"""
    sql = "SELECT ITEM_CODE, FOOD_ITEM, PRICE FROM FOOD_MENU"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        print(tabulate(result, headers=[ "ITEM_CODE", "FOOD_ITEM", "PRICE"], tablefmt="grid"))
    else:
        print("No records found")


def delete():
    """Delete a record from sales_data table"""
    ITEM_CODE = input("Enter ITEM_CODE to Delete: ")
    sql = "DELETE FROM FOOD_MENU  where ITEM_CODE = ?"
    cursor.execute(sql, (ITEM_CODE,))
    conn.commit()
    print("Data Deleted Successfully")


def exit_program():
    """Close connection and exit"""
    conn.close()
    print("Database Connection Closed")
    exit()


# *Menu-Driven Execution*
while True:
    print("\n--- SQL Server Database Operations ---")
    print("1. INSERT DATA")
    print("2. UPDATE DATA")
    print("3. VIEW DATA")
    print("4. DELETE DATA")
    print("5. EXIT DATABASE")

    action = input("Enter your choice: ")

    if action == "1":
        insert()
    elif action == "2":
        update()
    elif action == "3":
        view()
    elif action == "4":
        delete()
    elif action == "5":
        exit_program()
    else:
        print("Invalid Choice, Try Again!")