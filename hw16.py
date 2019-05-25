import sqlite3 as lite
import sys

def first():
    try:
        con = None
        con = lite.connect('news_api.sqlite')
        query_invoice = '''
            CREATE TABLE IF NOT EXISTS
             News(
               ID INTEGER PRIMARY KEY AUTOINCREMENT       NOT NULL,
               TEXT           CHAR(200)      NOT NULL
            );
            CREATE TABLE IF NOT EXISTS
             Users(
               ID INTEGER PRIMARY KEY AUTOINCREMENT       NOT NULL,
               Name           CHAR(100)      NOT NULL,
               email          CHAR(100)      NOT NULL
            );
            CREATE TABLE IF NOT EXISTS
             History(
               ID INTEGER PRIMARY KEY AUTOINCREMENT       NOT NULL,
               UserID       INTEGER      NOT NULL,
               NewsID       INTEGER      NOT NULL,
               CONSTRAINT Users_History_fkey
                    FOREIGN KEY (UserID)
                    REFERENCES Users(id),
               CONSTRAINT News_History_fkey
                    FOREIGN KEY (NewsID)
                    REFERENCES News(id)
            );
            CREATE TABLE IF NOT EXISTS
             Keys(
               ID INTEGER PRIMARY KEY AUTOINCREMENT       NOT NULL,
               Text           CHAR(100)      NOT NULL
            );
            CREATE TABLE IF NOT EXISTS
             News_Keys(
               ID INTEGER PRIMARY KEY AUTOINCREMENT       NOT NULL,
               KeysID       INTEGER      NOT NULL,
               NewsID       INTEGER      NOT NULL,
               CONSTRAINT NK_Keys_fkey
                    FOREIGN KEY (KeysID)
                    REFERENCES Keys(id),
               CONSTRAINT NK_News_fkey
                    FOREIGN KEY (NewsID)
                    REFERENCES News(id)
            );
            CREATE TABLE IF NOT EXISTS
             Category(
               ID INTEGER PRIMARY KEY AUTOINCREMENT       NOT NULL,
               Text           CHAR(100)      NOT NULL
            );
            CREATE TABLE IF NOT EXISTS
             News_Category(
               ID INTEGER PRIMARY KEY AUTOINCREMENT       NOT NULL,
               CategoryID       INTEGER      NOT NULL,
               NewsID       INTEGER      NOT NULL,
               CONSTRAINT NewsCat_Category_fkey
                    FOREIGN KEY (CategoryID)
                    REFERENCES Category(id),
               CONSTRAINT NewsCat_News_fkey_fkey
                    FOREIGN KEY (NewsID)
                    REFERENCES News(id)
            );
            '''
        curID = con.cursor()
        curID.executescript(query_invoice)
        print(curID.fetchall())
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        if con is not None:
            con.close()

first()
