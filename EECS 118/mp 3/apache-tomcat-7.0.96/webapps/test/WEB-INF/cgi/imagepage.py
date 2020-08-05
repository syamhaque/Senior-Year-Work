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

numofimages = 0
form = cgi.FieldStorage()
gallery_id = form.getvalue('gallery_id')

print("""Content-Type:text/html\r\n\r\n
<html>
<head>
<title>Mini Project 3</title>
</head>
<h1>Gallery {}:</h1>
</html>""".format(gallery_id))

#2.
sql = """SELECT * FROM image WHERE gallery_id = '%s'"""%(gallery_id)
cur.execute(sql)
for row in cur.fetchall():
    numofimages += 1
    print("""<html>
    <body>
    <h3>Image {} title: {}</h3>
    <p>Link: {}</p>
    </body>
    </html>""".format(row[0],row[1],row[2]))


print("""<html>
<body>
<h2>{} Images in total</h2>
<form action = "detailpage.py" method = "post">
<h1>List details of an image:</h1>
Image number: <input type = "text" name = "img_id">
<h1></h1>
<input type = "submit" value = "Submit" />
</form>
<form action = "newimage.py" method = "post">
<h1>Add a new image:</h1>
Title: <input type = "text" name = "img_title">
<h1></h1>
Link: <input type = "text" name = "img_link">
<h1></h1>
<input type = "hidden" name = "gallery_id" value = "{}">
<h3>Artist:</h3>
Name: <input type = "text" name = "art_name">
Birth Year: <input type = "text" name = "art_birth">
Country: <input type = "text" name = "art_country">
Description: <input type = "text" name = "art_desc">
<h3>Details:</h3>
Year: <input type = "text" name = "det_year">
Type: <input type = "text" name = "det_type">
Width: <input type = "text" name = "det_width">
Height: <input type = "text" name = "det_height">
Location: <input type = "text" name = "det_loc">
Description: <input type = "text" name = "det_desc">
<h1></h1>
<input type = "submit" value = "Submit" />
</form>
<form action = "delimage.py" method = "post">
<h1>Delete an image:</h1>
Image number: <input type = "text" name = "img_id">
<h1></h1>
<input type = "submit" value = "Submit" />
</form>
<form action = "gallerypage.py" method = "post">
<input type = "submit" value = "Return to galleries" />
</form>
</body>
</html>""".format(numofimages,gallery_id))
