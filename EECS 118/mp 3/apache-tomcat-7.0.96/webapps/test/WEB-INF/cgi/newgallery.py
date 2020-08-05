#EECS 118 mp3
#Mohammed Haque
#62655407
#11/10/19
import pymysql
from datetime import datetime
import cgi

db = pymysql.connect(host='localhost',
user='gallery',
passwd='eecs118',
db= 'gallery')
cur = db.cursor()
form = cgi.FieldStorage()

gallery_name = form.getvalue('gallery_name')
gallery_desc = form.getvalue('gallery_desc')

print("""Content-Type:text/html\r\n\r\n
<head>
<title>Mini Project 3</title>
</head>""")

#5.
sql = """INSERT IGNORE INTO gallery(name, description) VALUES(%s, %s)"""
val = (gallery_name, gallery_desc)
cur.execute(sql,val)
db.commit()

print("""<html>
<body>
<form action = "gallerypage.py" method = "post">
<h1>Gallery updated</h1>
<input type = "submit" value = "Return" />
</body>
</html>""")


