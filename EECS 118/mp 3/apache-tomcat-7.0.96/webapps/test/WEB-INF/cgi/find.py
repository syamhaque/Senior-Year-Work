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
img_id = []
art_id = []
#12. Find image by type
det_type = form.getvalue('det_type')
#13. Find image by range of creation year
det_year_1 = form.getvalue('det_year_1')
det_year_2 = form.getvalue('det_year_2')
#14. Find image by artist name
art_name = form.getvalue('art_name')
#15. Find image by location
det_loc = form.getvalue('det_loc')
#16. Find by artist by country
art_country = form.getvalue('art_country')
#17. Find by artist by birth year
art_birth = form.getvalue('art_birth')

print("""Content-Type:text/html\r\n\r\n
<head>
<title>Mini Project 3</title>
</head>
""")

#12.
if(det_type):
    sql = """SELECT * FROM detail WHERE type = '%s'"""%(det_type)
    cur.execute(sql)
    for row in cur.fetchall():
        img_id.append(row[1])
    for i in img_id:
        sql = """SELECT * FROM image WHERE image_id = '%s'"""%(i)
        cur.execute(sql)
        for row in cur.fetchall():
            print("""<html>
            <body>
            <h3>Image {} title: {}</h3>
            <p>Link: {}</p>
            </body>
            </html>""".format(row[0],row[1],row[2]))
#13.
elif(det_year_1 and det_year_2):
    sql = """SELECT * FROM detail WHERE year BETWEEN '%s' AND '%s'"""%(det_year_1, det_year_2)
    cur.execute(sql)
    for row in cur.fetchall():
        img_id.append(row[1])
    for i in img_id:
        sql = """SELECT * FROM image WHERE image_id = '%s'"""%(i)
        cur.execute(sql)
        for row in cur.fetchall():
            print("""<html>
            <body>
            <h3>Image {} title: {}</h3>
            <p>Link: {}</p>
            </body>
            </html>""".format(row[0],row[1],row[2]))
#14.
elif(art_name):
    sql = """SELECT * FROM artist WHERE name = '%s'"""%(art_name)
    cur.execute(sql)
    for row in cur.fetchall():
        art_id.append(row[0])
    for i in art_id:
        sql = """SELECT * FROM image WHERE artist_id = '%s'"""%(i)
        cur.execute(sql)
        for row in cur.fetchall():
            print("""<html>
            <body>
            <h3>Image {} title: {}</h3>
            <p>Link: {}</p>
            </body>
            </html>""".format(row[0],row[1],row[2]))
#15.
elif(det_loc):
    sql = """SELECT * FROM detail WHERE location = '%s'"""%(det_loc)
    cur.execute(sql)
    for row in cur.fetchall():
        img_id.append(row[1])
    for i in img_id:
        sql = """SELECT * FROM image WHERE image_id = '%s'"""%(i)
        cur.execute(sql)
        for row in cur.fetchall():
            print("""<html>
            <body>
            <h3>Image {} title: {}</h3>
            <p>Link: {}</p>
            </body>
            </html>""".format(row[0],row[1],row[2]))
#16.
elif(art_country):
    sql = """SELECT * FROM artist WHERE country = '%s'"""%(art_country)
    cur.execute(sql)
    for row in cur.fetchall():
        print("""<html>
        <body>
        <h3>Artist {} name: {}</h3>
        <p>Birth Year: {} Country: {}</p>
        <p>Description: {}</p>
        </body>
        </html>""".format(row[0],row[1],row[2], row[3], row[4]))
#17.
elif(art_birth):
    sql = """SELECT * FROM artist WHERE birth_year = '%s'"""%(art_birth)
    cur.execute(sql)
    for row in cur.fetchall():
        print("""<html>
        <body>
        <h3>Artist {} name: {}</h3>
        <p>Birth Year: {} Country: {}</p>
        <p>Description: {}</p>
        </body>
        </html>""".format(row[0],row[1],row[2], row[3], row[4]))
else:
    print("""<html>
    <body>
    <h1>Nothing Inputted</h1>
    <form action = "findormodifypage.py" method = "post">
    <input type = "submit" value = "Return" />
    </form>
    </body>
    </html>""")
