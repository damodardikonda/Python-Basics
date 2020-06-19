import sqlite3
from emp_sql import Employee
conn=sqlite3.connect(':memory:')# here weare creating a connection

def insert_emp(emp):
    with conn: # nowit doesnt required commit() function
       c.execute("INSERT INTO employee VALUES (:first,:last,:pay)" , {'first':emp.first, 'last':emp.last,'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employee  where last=:last",{'last':emp_1.last})
    return c.execute



def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})





emp_1=Employee('Damodar','Dikonda',6000000)
emp_2=Employee('Aditya','Mali',5000000)

insert_emp(emp_1)

get_obj=get_emps_by_name(emp_1)
print(get_obj)

update_pay(emp_2)
remove_emp(emp_1)

get_obj=get_emps_by_name(emp_1)
print(get_obj)


conn.close()
