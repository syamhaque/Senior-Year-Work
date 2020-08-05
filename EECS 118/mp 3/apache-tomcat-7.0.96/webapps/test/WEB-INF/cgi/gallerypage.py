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

#18.
timeofday = int(datetime.now().strftime('%H'))
greeting = ''
if(timeofday >= 21 or timeofday < 5):
    greeting = 'Good night'
elif(5 <= timeofday < 12):
    greeting = 'Good morning'
elif(12 <= timeofday < 17):
    greeting = 'Good afternoon'
elif(17 <= timeofday < 21):
    greeting = 'Good evening'

print ("""Content-Type:text/html\r\n\r\n
<html>
<head>
<title>Mini Project 3</title>
</head>
<body>
<h3>{}</h3>
<h1>Mohammed Haque's Mini Project 3</h1>
<h1>Galleries</h1>
</body>
</html>""".format(greeting))

#1.
sql = "SELECT * FROM gallery"
cur.execute(sql)
for row in cur.fetchall():
    print("""<html>
    <body>
    <h3>Gallery {} name: {}</h3>
    <p>Description: {}</p>
    </body>
    </html>""".format(row[0], row[1],row[2]))

print("""<html>
<body>
<form action = "imagepage.py" method = "get">
<h1>List images of a gallery:</h1>
Gallery number: <input type = "text" name = "gallery_id">
<h1></h1>
<input type = "submit" value = "Submit" />
</form>
<form action = "newgallery.py" method = "post">
<h1>Create a new gallery:</h1>
Name: <input type = "text" name = "gallery_name">
<h1></h1>
Description: <input type = "text" name = "gallery_desc">
<h1></h1>
<input type = "submit" value = "Submit" />
</form>
<form action = "newartist.py" method = "post">
<h1>Create a new artist:</h1>
Name: <input type = "text" name = "art_name">
<h1></h1>
Birth Year: <input type = "text" name = "art_birth">
<h1></h1>
Country: <input type = "text" name = "art_country">
<h1></h1>
Description: <input type = "text" name = "art_desc">
<h1></h1>
<input type = "submit" value = "Submit" />
</form>
<form action = "findormodifypage.py" method = "get">
<h1>Find or Modify information:</h1>
<input type = "submit" value = "Click to Proceed" />
</form>
</body>
</html>""")
