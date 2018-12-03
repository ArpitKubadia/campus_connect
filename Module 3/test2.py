import cx_Oracle
con=cx_Oracle.connect("ARPIT/arpit123@localhost/xe")
cur=con.cursor()
results=cur.execute("SELECT * FROM Arpit")
for result in results:
    print(result)
con.close()