import sqlite3#
from emp_sql import Employee
conn=sqlite3.connect('employee.db')# here weare creating a connection

#cursor is an control structure used to traverse and fetch from database
#all command is execute using cursor only.

c=conn.cursor()

#c.execute(""" CREATE TABLE employee(

#                   first text,
#                   last text,
#                   pay int
#      )""")

emp_1=Employee('Corey','schafer',9000)
emp_2=Employee('jane','schafer',40000)


#print(emp_1.first)
#print(emp_1.last)
#print(emp_1.pay)

#c.execute("INSERT INTO employee VALUES ('{}','{}','{}')".format(emp_1.first, emp_1.last, emp_1.pay))
#it will lead to sql injection attack

#eb API placehoder
#c.execute("INSERT INTO employee VALUES (?,?,?)" , (emp_1.first, emp_1.last, emp_1.pay))
#conn.commit()

#print("second Way is")
#c.execute("INSERT INTO employee VALUES (:first,:last,:pay)" , {'first':emp_2.first, 'last':emp_2.last,'pay': emp_2.pay})
#conn.commit()


c.execute("INSERT INTO employee VALUES ('Damodar' , 'Dikonda' ,1000000)")
c.execute("INSERT INTO employee VALUES ('Aditya' , 'Mali' ,900000)")
#c.execute("INSERT INTO employee VALUES ('Niket' , 'Jadhav' ,800000)")
#c.execute("INSERT INTO employee VALUES ('Tanmay' , 'Mali' ,700000)")
#c.execute("INSERT INTO employee VALUES ('Aadesh' , 'Mali' ,700000)")

#c.execute("SELECT * FROM employee ")
c.execute("SELECT * FROM employee where last=? ",('Mali',))

c.execute("SELECT * FROM employee  where last=:last",{'last':emp_1.last})


#print(c.fetchone())
#print(c.fetchmany(6))
print(c.fetchall())

conn.commit() # it commits the statements

conn.close()
