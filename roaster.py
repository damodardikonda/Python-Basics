import json
import sqlite3

conn=sqlite3.connect("roaster.sqlite")
c=conn.cursor()

c.executescript('''
DROP TABLE IF EXIST User;
DROP TABLE IF EXIST Member;
DROP TABLE IF EXIST Course;

CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
  );

CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
    title TEXT UNIQUE
  );

CREATE TABLE Member(
   user_id INTEGER,
   course_id INTEGER,
   role INTEGER,
   PRIMARY KEY(user_id,course_id)
);

''')

fname=input("Enter The File Name :\t")
if (len(fname)<1): fname='roaster_data.json'

str_d=open(fname).read()
loader=json.loads(str_d)

for i in loader:
    name=i[0];
    title=i[1];
    print((name,title))


c.execute('''INSERT OR IGNORE INTO User(name) VALUES ( ? )''' , (name,))
c.execute('SELECT id FROM User WHERE name =? ', (name,))
user_id=c.fetchone()[0]

c.execute('''INSERT OR IGNORE INTO Course (title,)
        VALUES ( ?)''', ( title, ) )
c.execute('SELECT id,roleFROM Course WHERE title = ? ', (title, ))
course_id = c.fetchone()[0]
role=c.fetchone()[1]

c.execute('''INSERT OR REPLACE INTO Member(user_id,course_id,role) VALUES (?,?,?)''',
(user_id,course_id,role))

conn.commit()
