# This file is for reading data from the db/ directory
import sqlite3


# parses text files (only) found in the db directory
def parse_text(filename):
    FILE_PATH = "data/" + filename
    with open(FILE_PATH,"r") as f:
        data = f.read()
        f.close()
    processed_data = data.split("\n\n\n")
    return processed_data

def connect():
    FILE_PATH="data/tables.db"
    db = sqlite3.connect(FILE_PATH) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    return (c, db)

def disconnect(db):
    db.commit() #save changes
    db.close()  #close database

def add_entry_cite(website,apa):
    c,db = connect()
    c.execute(f"INSERT INTO CITATIONS (WEBSITE, APA) VALUES(?,?)",(website,apa))
    disconnect(db)

def add_entry_resource(link,name,description,category):
    c,db = connect()

    if category == None:
        c.execute(f"INSERT INTO RESOURCES (LINK,NAME,DESC) VALUES(?,?,?)",(link,name,description))
    else:
        c.execute(f"INSERT INTO RESOURCES (LINK,NAME,DESC,CATEGORY) VALUES(?,?,?,?)",(link,name,description,category))

    disconnect(db)

def get_citations():
    c,db = connect()
    citations = c.execute(f"SELECT * FROM citations").fetchall()
    disconnect(db)
    return citations

def get_resources():
    c,db = connect()
    resources = c.execute(f"SELECT * FROM resources").fetchall()
    disconnect(db)
    return resources

if __name__ == "__main__":

    # print(get_citations())
    # print(get_resources())

    add_entry_resource("whoasked6.com","who asked","this is description","pos")
    add_entry_resource("whoasked1.com","who asked","this is description","pos")
    add_entry_resource("whoasked2.com","who asked","this is description","pos")
    add_entry_resource("whoasked3.com","who asked","this is description","pow")
    add_entry_resource("whoasked4.com","who asked","this is description","pow")
    add_entry_resource("whoasked5.com","who asked","this is description","pow")


    print(get_citations())
    print(get_resources())




