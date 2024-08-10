import sqlite3

DB_NAME = 'PTTV.db'


def execute_query(query, params=()):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        result = cursor.fetchone()
        print("Success")
        return result
    
    except sqlite3.Error as error:
        print('Error occurred:', error)
        return None

    finally:
        if conn:
            conn.close()
        print("")


def create_table():
    print("Creating Table...")
    query = '''
    CREATE TABLE IF NOT EXISTS accounts (
        Username VARCHAR(255) PRIMARY KEY NOT NULL,
        Password VARCHAR(255) NOT NULL,
        Stream_key VARCHAR(255) NOT NULL,
        Banned INT NOT NULL DEFAULT 0
    ); '''
    execute_query(query)


def get_acc():
    print("Getting unbanned account...")
    query = '''SELECT Username, Stream_Key FROM accounts WHERE Banned = 0'''
    row = execute_query(query)

    if row is not None:
        username = row[0]
        streamkey = row[1]
        print(f"New account chosen: {username} {streamkey}\n")
        return username, streamkey
    else:
        print("Unable to get an unbanned user!")
        raise Exception("No unbanned accounts available.")
        
                
def add_account(username, password, streamkey):
    print("Adding account...")
    query = '''INSERT INTO accounts (Username, Password, Stream_key) VALUES (?, ?, ?)'''
    execute_query(query, (username, password, streamkey))


def set_banned(username):
    print("Setting account banned...")
    query = '''UPDATE accounts SET Banned = 1 WHERE Username = ?'''
    execute_query(query, (username, ))
