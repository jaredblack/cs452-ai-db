import argparse
from db import create_connection


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

def select_from_table(conn, query):
    """
    Query all rows in the horse table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

if __name__ == "__main__":
    database = "./horse.db"
    conn = create_connection(database)

    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, help="SELECT * FROM Horses where stable_id = 3")
    args = parser.parse_args()
    print(f"Executing query: {args.query}")
    select_from_table(conn, args.query)