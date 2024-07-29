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
    query = '''SELECT Username FROM accounts WHERE Banned = 0'''
    row = execute_query(query)

    if row is not None:
        print(f"New account chosen: {row[0]} \n")
        return row[0]
    else:
        print("Unable to get an unbanned user!")
        quit()
        
def get_streamkey(username):
    print("Getting Stream key...")
    query = '''SELECT Stream_key FROM accounts WHERE username = ?'''
    row = execute_query(query, (username, ))
    if row is not None:
        print(f"Streamkey found: {row[0]} \n")
        return row[0]
    else:
        print("Unable to get streamkey for user {username}!")
        quit()
        
def add_account(username, password, streamkey):
    print("Adding account...")
    query = '''INSERT INTO accounts (Username, Password, Stream_key) VALUES (?, ?, ?)'''
    execute_query(query, (username, password, streamkey))
    

def set_banned(username):
    print("Setting account banned...")
    query = '''UPDATE accounts SET Banned = 1 WHERE Username = ?'''
    execute_query(query, (username, ))