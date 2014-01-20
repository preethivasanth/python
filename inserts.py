import mysql.connector
cn=mysql.connector.connect(user="root",database="student",password="root")
cr=cn.cursor()
cr.execute("insert into mark(reg no,name,tamil,english)values({0},'{1}',{2},{3})".format(3,'sam',90,95}
cn.connect()
print("record inserted")
cr.close()
cn.close()
