import pyodbc


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-LM2V9IG\SQLEXPRESS;'
                      'Database=Ferreteria;'
                      'Trusted_Connection=yes;')


    
    
    







cursor = conn.cursor()
update_query = "UPDATE articulos SET art_pre = '1000' WHERE art_cod= 'art001'"
cursor.execute(update_query)
conn.commit()






cursor = conn.cursor()
cursor.execute('select * from articulos')

for row in cursor:
	print(row)



    






cursor = conn.cursor()

val = ("art007", "Grava", 46, "GB", 16, 26, 1)
    
insert_records = "INSERT INTO articulos(art_cod,art_des,art_pre,art_uni,art_stk,art_max,art_min) VALUES(?,?,?,?,?,?,?) "
cursor.execute(insert_records,val)
conn.commit()




cursor = conn.cursor()
delete_query = "DELETE FROM articulos WHERE art_cod= 'art007'"
cursor.execute(delete_query )
conn.commit()














