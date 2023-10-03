import os

from db import create_table, create_connection
from schema import *


def select_all_from_horse(conn):
    """
    Query all rows in the horse table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Horses")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def insert_to_horse(conn):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = """
        INSERT INTO Horses(name, birthdate, gender, color, breed_id, owner_id, stable_id)
        VALUES
        ('Thunderstrike', '2010-05-15', 'Male', 'Brown', 1, 1, 1),
        ('Midnight Star', '2015-03-20', 'Female', 'Black', 2, 2, 2),
        ('Silver Shadow', '2012-07-10', 'Male', 'White', 3, 3, 1),
        ('Stardust', '2014-01-25', 'Female', 'Gray', 4, 4, 3),
        ('Blaze', '2018-11-05', 'Male', 'Bay', 1, 5, 2),
        ('Amber Fire', '2013-09-08', 'Female', 'Chestnut', 2, 6, 3),
        ('Whispering Wind', '2016-04-12', 'Male', 'Palomino', 3, 7, 1),
        ('Moonlight Mirage', '2019-02-28', 'Female', 'Appaloosa', 4, 8, 2),
        ('Rusty', '2011-12-19', 'Male', 'Pinto', 1, 9, 3),
        ('Golden Gem', '2017-08-03', 'Female', 'Buckskin', 2, 10, 1)
    """

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_owners(conn):

    sql = """
        INSERT INTO Owners(first_name, last_name, email, phone)
        VALUES
        ('John', 'Doe', 'john.doe@example.com', '+1-555-123-4567'),
        ('Jane', 'Smith', 'jane.smith@example.com', '+1-555-987-6543'),
        ('Robert', 'Johnson', 'robert.johnson@example.com', '+1-555-555-5555'),
        ('Mary', 'Brown', 'mary.brown@example.com', '+1-555-777-8888'),
        ('Michael', 'Davis', 'michael.davis@example.com', '+1-555-444-3333'),
        ('Emily', 'Wilson', 'emily.wilson@example.com', '+1-555-222-1111'),
        ('David', 'Lee', 'david.lee@example.com', '+1-555-666-9999'),
        ('Lisa', 'Garcia', 'lisa.garcia@example.com', '+1-555-333-7777'),
        ('William', 'Martinez', 'william.martinez@example.com', '+1-555-888-2222'),
        ('Susan', 'Taylor', 'susan.taylor@example.com', '+1-555-999-5555')
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_stables(conn):

    sql = """
        INSERT INTO Stables(name, location, contact_person, contact_phone)
        VALUES
        ('Cheyenne', '123 Main St, City A', 'John Stablemaster', '+1-555-111-1111'),
        ('Minitonka', '456 Oak St, City B', 'Jane Stablemanager', '+1-555-222-2222'),
        ('Mt Nebo', '789 Elm St, City C', 'Robert Stableboss', '+1-555-333-3333')
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_breeds(conn):
    sql = """
         INSERT INTO Breeds(name, description)
        VALUES
        ('Thoroughbred', 'Known for speed and agility.'),
        ('Quarter Horse', 'Versatile breed, often used in western riding.'),
        ('Arabian', 'Elegant and spirited breed.'),
        ('Appaloosa', 'Distinctive coat patterns and coloration.')
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_training_records(conn):

    sql = """
        INSERT INTO TrainingRecords(horse_id, trainer_id, training_date, training_type, duration_minutes, notes)
        VALUES
        (1, 1, '2023-01-10', 'Dressage', 60, 'Excellent progress.'),
        (2, 2, '2023-02-15', 'Jumping', 45, 'Needs more practice on hurdles.'),
        (3, 3, '2023-03-20', 'Racing', 30, 'Fast sprint during training.'),
        (4, 4, '2023-04-25', 'Dressage', 75, 'Good posture during maneuvers.'),
        (5, 5, '2023-05-30', 'Jumping', 60, 'Impressive jump height.'),
        (6, 6, '2023-06-15', 'Racing', 40, 'Needs more stamina training.'),
        (7, 7, '2023-07-20', 'Dressage', 50, 'Steady progress in movements.'),
        (8, 8, '2023-08-25', 'Jumping', 55, 'Working on precision in jumps.'),
        (9, 9, '2023-09-10', 'Racing', 35, 'Improving speed and agility.'),
        (10, 10, '2023-10-15', 'Dressage', 70, 'Impressive flexibility and control.')
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def main():
    database = "./horse.db"

    # create a database connection
    conn = create_connection(database)
    create_table(conn, sql_create_horse_table)
    insert_to_horse(conn)
    create_table(conn, sql_create_breed_table)
    insert_to_breeds(conn)
    create_table(conn, sql_create_owner_table)
    insert_to_owners(conn)
    create_table(conn, sql_create_stable_table)
    insert_to_stables(conn)
    create_table(conn, sql_create_training_record_table)
    insert_to_training_records(conn)

    print("Database build successful!")

if __name__ == "__main__":
    main()


