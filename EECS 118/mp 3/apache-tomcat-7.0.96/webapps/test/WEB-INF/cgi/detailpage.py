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
img_id = form.getvalue('img_id')
img_title = ''
img_link = ''
det_year = 0
det_type = ''
det_width = 0
det_height = 0
det_loc = ''
det_desc = ''
artist_id = 1
art_name = ''


sql = """SELECT * FROM image WHERE image_id = '%s'"""%(img_id)
cur.execute(sql)
for row in cur.fetchall():
    img_title = row[1]
    img_link = row[2]
    artist_id = row[4]

sql = """SELECT * FROM detail WHERE image_id = '%s'"""%(img_id)
cur.execute(sql)
for row in cur.fetchall():
    det_year = row[2]
    det_type = row[3]
    det_width = row[4]
    det_height = row[5]
    det_loc = row[6]
    det_desc = row[7]

sql = """SELECT * FROM artist WHERE artist_id = '%s'"""%(artist_id)
cur.execute(sql)
for row in cur.fetchall():
    art_name = row[1]
    
#3.
print("""Content-Type:text/html\r\n\r\n
<html>
<head>
<title>Mini Project 3</title>
</head>
<body>
<h1>{}</h1>
<img src = {}>
<h1></h1>
<form action = "artistpage.py" method = "post">
<input type = "hidden" name = "artist_id" value = "{}">
<input type = "submit" value = "Artist {}" />
</form>
<p>Year: {} Type: {}</p>
<p>Width: {} Height: {}</p>
<p>Location: {} Description: {}</p>
</body>
</html>""".format(img_title, img_link, artist_id, art_name, det_year, det_type,
                  det_width, det_height, det_loc, det_desc))

print("""<html>
<body>
<button onclick="returnImages()">Return to images</button>

<script>
function returnImages() {
  window.location.replace(document.referrer);
}
</script>
<form action = "gallerypage.py" method = "post">
<h1></h1>
<input type = "submit" value = "Return to galleries" />
</form>
</body>
</html>""")

