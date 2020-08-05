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
img_title = form.getvalue('img_title')
img_link = form.getvalue('img_link')
gallery_id = form.getvalue('gallery_id')
art_name = form.getvalue('art_name')
art_birth = form.getvalue('art_birth')
art_country = form.getvalue('art_country')
art_desc = form.getvalue('art_desc')
det_year = form.getvalue('det_year')
det_type = form.getvalue('det_type')
det_width = form.getvalue('det_width')
det_height = form.getvalue('det_height')
det_loc = form.getvalue('det_loc')
det_desc = form.getvalue('det_desc')

artist_id = 1
detail_id = 1

print("""Content-Type:text/html\r\n\r\n
<head>
<title>Mini Project 3</title>
</head>
<html>
<body>
<h1>Image added</h1>
<button onclick="returnImages()">Return to images</button>

<script>
function returnImages() {
  window.location.replace(document.referrer);
}
</script>
</body>
</html>""")

#7.
sql = """INSERT IGNORE INTO artist(name, birth_year, country,
        description) VALUES(%s, %s, %s, %s)"""
val = (art_name, art_birth, art_country, art_desc)
cur.execute(sql,val)
db.commit()

sql = """SELECT MAX(artist_id) FROM artist"""
cur.execute(sql)
for row in cur.fetchall():
    artist_id = row[0]

sql = """SELECT MAX(detail_id) FROM detail"""
cur.execute(sql)
for row in cur.fetchall():
    detail_id = int(0 if row[0] is None else row[0])
detail_id += 1

sql = """INSERT IGNORE INTO image(title, link, gallery_id,
        artist_id, detail_id) VALUES(%s, %s, %s, %s, %s)"""
val = (img_title, img_link, gallery_id, artist_id, detail_id)
cur.execute(sql,val)
db.commit()

sql = """SELECT MAX(image_id) FROM image"""
cur.execute(sql)
for row in cur.fetchall():
    img_id = row[0]

sql = """INSERT IGNORE INTO detail(image_id, year, type, width,
        height, location, description) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
val = (img_id, det_year, det_type, det_width, det_height, det_loc, det_desc)
cur.execute(sql,val)
db.commit()


