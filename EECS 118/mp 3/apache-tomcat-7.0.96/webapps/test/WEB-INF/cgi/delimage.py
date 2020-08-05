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
img_id = form.getvalue('img_id')
det_id = 0

print("""Content-Type:text/html\r\n\r\n
<head>
<title>Mini Project 3</title>
</head>""")

sql = """SELECT * FROM image WHERE image_id = '%s'"""%(img_id)
cur.execute(sql)
for row in cur.fetchall():
    det_id = row[5]

#8.
sql = """DELETE FROM image WHERE image_id = '%s'"""%(img_id)
cur.execute(sql)
db.commit()
sql = """DELETE FROM detail WHERE detail_id = '%s'"""%(det_id)
cur.execute(sql)
db.commit()

print("""<html>
<body>
<h1>Image deleted</h1>
<button onclick="returnImages()">Return to images</button>

<script>
function returnImages() {
  window.location.replace(document.referrer);
}
</script>
</body>
</html>""")
