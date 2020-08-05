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
artist_id = form.getvalue('artist_id')

print("""Content-Type:text/html\r\n\r\n
<head>
<title>Mini Project 3</title>
</head>""")

#4.
sql = """SELECT * FROM artist WHERE artist_id = '%s'"""%(artist_id)
cur.execute(sql)
for row in cur.fetchall():
    print("""<html>
    <body>
    <h1>Artist: {}</h1>
    <p>Birth Year: {}</p>
    <p>Country: {}</p>
    <p>Description: {}</p>
    </body>
    </html>""".format(row[1],row[2],row[3],row[4]))

print("""<html>
<body>
<button onclick="returnDetails()">Return to details</button>

<script>
function returnDetails() {
  window.history.back();
}
</script>
<h1></h1>
<button onclick="returnImages()">Return to images</button>

<script>
function returnImages() {
  window.history.go(-2);
}
</script>
<h1></h1>
<form action = "gallerypage.py" method = "post">
<input type = "submit" value = "Return to galleries" />
</form>
</body>
</html>""")
