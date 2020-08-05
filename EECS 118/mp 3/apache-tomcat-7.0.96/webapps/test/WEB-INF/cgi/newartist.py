#EECS 118 mp3
#Mohammed Haque
#62655407
#11/15/19
import pymysql
from datetime import datetime
import cgi

db = pymysql.connect(host='localhost',
user='gallery',
passwd='eecs118',
db= 'gallery')
cur = db.cursor()
form = cgi.FieldStorage()

art_name = form.getvalue('art_name')
art_birth = form.getvalue('art_birth')
art_country = form.getvalue('art_country')
art_desc = form.getvalue('art_desc')

print("""Content-Type:text/html\r\n\r\n
<head>
<title>Mini Project 3</title>
</head>""")

#6.
sql = """INSERT IGNORE INTO artist(name, birth_year, country, description)
        VALUES(%s, %s, %s, %s)"""
val = (art_name, art_birth, art_country, art_desc)
cur.execute(sql,val)
db.commit()

print("""<html>
<body>
<form action = "gallerypage.py" method = "post">
<h1>Artists updated</h1>
<input type = "submit" value = "Return" />
</body>
</html>""")
