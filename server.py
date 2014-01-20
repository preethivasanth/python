#!/python33/python
import cgi,cgitb
cgitb.enable()
print("content_type:test/html")
print(" ")
f=cgi.Fieldtorage()
n=f.getvalue("uname")
print("hi{0},welcome for puthon".format(n))
