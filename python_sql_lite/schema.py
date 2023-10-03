import sqlite3
# sql_create_category_table = """
#     CREATE TABLE categories (
#     category_id INT PRIMARY KEY,
#     category_name TEXT
#     );
# """

# sql_create_menu_table = """
#     CREATE TABLE menu (
#         menu_id INT PRIMARY KEY ,
#         menu_name TEXT,
#         category_id INT,
#         unit_price REAL,
#         FOREIGN KEY (category_id) references categories(category_id)
#     );
# """

# sql_create_customers_table = """
#     CREATE TABLE customers (
#     customer_id INT PRIMARY KEY ,
#     firstname TEXT,
#     Lastname TEXT,
#     city TEXT
# );
# """

# sql_create_employee_table = """
#     CREATE TABLE employee (
#         emp_id INT PRIMARY KEY ,
#         firstname TEXT,
#         Lastname TEXT,
#         hiredate TEXT,
#         branch TEXT );
# """

# sql_create_orders_table = """
#     CREATE TABLE Orders(
#         orderid INT,
#         orderdate TEXT,
#         menu_id INT,
#         quantity INT DEFAULT 0,
#         customer_id INT,
#         delivery_platform TEXT,
#         emp_id INT,
#         FOREIGN KEY (menu_id) references menu(menu_id)
#         FOREIGN KEY (customer_id) references customers(customer_id)
#         FOREIGN KEY (emp_id) references employee(emp_id)
#     );
# """


# Connect to the SQLite database (or create one if it doesn't exist)
# conn = sqlite3.connect('horse_database.db')
# cursor = conn.cursor()

# Create the Horses table
sql_create_horse_table = '''
    CREATE TABLE IF NOT EXISTS Horses (
        horse_id INTEGER PRIMARY KEY,
        name TEXT,
        birthdate DATE,
        gender TEXT,
        color TEXT,
        breed_id INTEGER,
        owner_id INTEGER,
        stable_id INTEGER,
        FOREIGN KEY (breed_id) REFERENCES Breeds(breed_id),
        FOREIGN KEY (owner_id) REFERENCES Owners(owner_id),
        FOREIGN KEY (stable_id) REFERENCES Stables(stable_id)
    );
'''

# Create the Owners table
sql_create_owner_table = '''
    CREATE TABLE IF NOT EXISTS Owners (
        owner_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        phone TEXT
    )
'''

# Create the Stables table
sql_create_stable_table = '''
    CREATE TABLE IF NOT EXISTS Stables (
        stable_id INTEGER PRIMARY KEY,
        name TEXT,
        location TEXT,
        contact_person TEXT,
        contact_phone TEXT
    )
'''

# Create the Breeds table
sql_create_breed_table = '''
    CREATE TABLE IF NOT EXISTS Breeds (
        breed_id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT
    )
'''

# Create the Training Records table
sql_create_training_record_table = '''
    CREATE TABLE IF NOT EXISTS TrainingRecords (
        training_id INTEGER PRIMARY KEY,
        horse_id INTEGER,
        trainer_id INTEGER,
        training_date DATE,
        training_type TEXT,
        duration_minutes INTEGER,
        notes TEXT,
        FOREIGN KEY (horse_id) REFERENCES Horses(horse_id)
    )
'''

def get_schema():
    schema = f"{sql_create_horse_table}{sql_create_stable_table}{sql_create_breed_table}{sql_create_owner_table}{sql_create_training_record_table}"
    return schema
