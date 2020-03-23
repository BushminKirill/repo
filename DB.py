import pyodbc


class DBConnect():
    con = pyodbc.connect('DRIVER={SQL Server};SERVER=KIRILL\SQLEXPRESS;DATABASE=taskbd')
    cursor = con.cursor()

    cursor.execute("select * from taskbd.dbo.Task")
    row = cursor.fetchone()
    if row:
        print(row)
