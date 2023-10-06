import sqlite3

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
