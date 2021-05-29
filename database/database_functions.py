import sqlite3
from PIL import Image
from pathlib import Path
import csv

class Database:

    #
    def create_table():
        conn = sqlite3.connect('/home/janekkttme/Документы/FindIt/database/items.db')
    
        cur = conn.cursor()
    
        cur.execute('DELETE from items')
    
        cur.execute('''CREATE TABLE IF NOT EXISTS items(
            id TEXT PRIMARY KEY,
            gender TEXT,
            image BLOB,
            title TEXT,
            price TEXT);
        ''')
        
        conn.commit()
    
    #
    def add_rows():
        conn = sqlite3.connect('/home/janekkttme/Документы/FindIt/database/items.db')
    
        cur = conn.cursor()

        items = []
    
        #read from file
        path = Path('/home/janekkttme/Документы/FindIt/webScraping/data_HM.csv')    
        
        with path.open('r') as f:
            reader=csv.DictReader(f)
        
            for item in reader:
                tmp = [item['productId'], item['gender'], item['imageLink'], item['productName'], item['priceOriginal']]
                items.append(tmp)
        
        cur.executemany('INSERT INTO items VALUES(?, ?, ?, ?, ?);', items)
    
        conn.commit()

    #
    def update():
        conn = sqlite3.connect('/home/janekkttme/Документы/FindIt/database/items.db')
    
        cur = conn.cursor()
    
        cur.execute('DELETE from items')
    
        path = Path('/home/janekkttme/Документы/FindIt/webScraping/data_HM.csv')    
        
        with path.open('r') as f:
            reader=csv.DictReader(f)
        
            for item in reader:
                tmp = [item['productId'], item['gender'], item['imageLink'], item['productName'], item['priceOriginal']]
                items.append(tmp)
        cur.executemany('INSERT INTO items VALUES(?, ?, ?, ?, ?, ?);', items)
    
        conn.commit()
   
    #   
    def getAll():
        conn = sqlite3.connect('/home/janekkttme/Документы/FindIt/database/items.db')
    
        cur = conn.cursor()
    
        cur.execute('SELECT * from items')
    
        items = cur.fetchall()
    
        return items
    
    #
    def getBySexAndCategory(sex, category):
        conn = sqlite3.connect('/home/janekkttme/Документы/FindIt/database/items.db')
    
        cur = conn.cursor()
    
        if category == 'View All':
            cur.execute('SELECT id, image, title from items WHERE gender = ?', sex)
        else:
            cur.execute('''SELECT id, image, title from items 
                WHERE gender = ? AND category = ?''', sex, category)
    
        items = cur.fetchall()
    
        return items

    #
    def getById(identification):
        conn = sqlite3.connect('/home/janekkttme/Документы/FindIt/database/items.db')
        
        cur = conn.cursor()
    
        cur.execute('SELECT * from items WHERE id = ?', (identification, ))
    
        item = cur.fetchone()
    
        return item
    
def main():
    Database.create_table()
    Database.add_rows()
    print(Database.getById(980069002))
    
    


if __name__ == '__main__':
    main()
