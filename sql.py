import mysql.connector
cn=mysql.connector.connect(user="root",database="student",password="root")
cr=cn.cursor()
cr.execute("select * from mark")
for(r,n,t,e)in cr: 
 print("{0:<5}|{1:^20}|{2:5}|{3:>10}|".format(r,n,t,e))
cr.close()
cn.close()
