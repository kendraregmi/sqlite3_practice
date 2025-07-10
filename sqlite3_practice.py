import sqlite3 # build in sqlite3 module 

# connect to the database (file will be created id doesnot exist )
conn= sqlite3.connect('students.db')

# create a cursor to execute a sql 
cursor= conn.cursor()

cursor.execute("""
create table if not exists students (
    id integer primary key autoincrement, 
    name text not null, 
    grade integer 
    address text 
) """
)
conn.commit()

