#EECS 118 mp3
#Mohammed Haque
#62655407
#11/15/19
import pymysql
from datetime import datetime
import cgi
import cgitb

cgitb.enable()

db = pymysql.connect(host='localhost',
user='gallery',
passwd='eecs118',
db= 'gallery')
cur = db.cursor()

form = cgi.FieldStorage()
#9. Modifying image
img_id = form.getvalue('img_id')
img_title = form.getvalue('img_title')
img_link = form.getvalue('img_link')
det_year = form.getvalue('det_year')
det_type = form.getvalue('det_type')
det_width = form.getvalue('det_width')
det_height = form.getvalue('det_height')
det_loc = form.getvalue('det_loc')
det_desc = form.getvalue('det_desc')
imgart_name = form.getvalue('imgart_name')
imgart_birth = form.getvalue('imgart_birth')
imgart_country = form.getvalue('imgart_country')
imgart_desc = form.getvalue('imgart_desc')
#10. Modifying artist
art_id = form.getvalue('art_id')
art_name = form.getvalue('art_name')
art_birth = form.getvalue('art_birth')
art_country = form.getvalue('art_country')
art_desc = form.getvalue('art_desc')
#11. Modifying gallery
gallery_id = form.getvalue('gallery_id')
gallery_name = form.getvalue('gallery_name')
gallery_desc = form.getvalue('gallery_desc')

print("""Content-Type:text/html\r\n\r\n
<head>
<title>Mini Project 3</title>
</head>
""")

#9.
if(img_id):
    sql = """SELECT * FROM image WHERE image_id = '%s'"""%(img_id)
    cur.execute(sql)
    for row in cur.fetchall():
        imgart_id = row[4]
    sql = """UPDATE image SET title = '%s', link = '%s' WHERE image_id = '%s'"""%(img_title, img_link, img_id)
    cur.execute(sql)
    db.commit()
    sql = """UPDATE detail SET year = '%s', type = '%s', width = '%s', height = '%s', location = '%s', description = '%s' WHERE image_id = '%s'"""%(det_year, det_type, det_width, det_height, det_loc, det_desc, img_id)
    cur.execute(sql)
    db.commit()
    sql = """UPDATE artist SET name = '%s', birth_year = '%s', country = '%s', description = '%s' WHERE artist_id = '%s'"""%(imgart_name, imgart_birth, imgart_country, imgart_desc, imgart_id)
    cur.execute(sql)
    db.commit()
    print("""<html>
    <body>
    <h1>Image modified</h1>
    <form action = "findormodifypage.py" method = "post">
    <input type = "submit" value = "Return" />
    </form>
    </body>
    </html>""")
#10.
elif(art_id):
    sql = """UPDATE artist SET name = '%s', birth_year = '%s', country = '%s', description = '%s' WHERE artist_id = '%s'"""%(art_name, art_birth, art_country, art_desc, art_id)
    cur.execute(sql)
    db.commit()
    print("""<html>
    <body>
    <h1>Artist modified</h1>
    <form action = "findormodifypage.py" method = "post">
    <input type = "submit" value = "Return" />
    </form>
    </body>
    </html>""")
#11.
elif(gallery_id):
    sql = """UPDATE gallery SET name = '%s', description = '%s' WHERE gallery_id = '%s'"""%(gallery_name, gallery_desc, gallery_id)
    cur.execute(sql)
    db.commit()
    print("""<html>
    <body>
    <h1>Gallery modified</h1>
    <form action = "findormodifypage.py" method = "post">
    <input type = "submit" value = "Return" />
    </form>
    </body>
    </html>""")
else:
    print("""<html>
    <body>
    <h1>Nothing Inputted</h1>
    <form action = "findormodifypage.py" method = "post">
    <input type = "submit" value = "Return" />
    </form>
    </body>
    </html>""")

