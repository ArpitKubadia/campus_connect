import cx_Oracle
con=cx_Oracle.connect("system/arpit123@localhost/xe")
cur=con.cursor()
results=cur.execute("SELECT * FROM Employer")
for result in results:
    print(result)
con.close()