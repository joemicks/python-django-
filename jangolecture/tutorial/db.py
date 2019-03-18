import sqlite3
conn=sqlite3.connect('employee.db')
c=conn.cursor()
c.execute("insert into employee values('nirmal',12)")
conn.commit()
conn.close()