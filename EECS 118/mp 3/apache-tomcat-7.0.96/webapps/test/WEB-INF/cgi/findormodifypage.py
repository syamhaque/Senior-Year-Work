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

print("""Content-Type:text/html\r\n\r\n
<head>
<title>Mini Project 3</title>
</head>
<html>
<body>
<h1>Modify details:</h1>
<form action = "modify.py" method = "post">
<h3>Details of an Image:</h3>
Image number: <input type = "text" name = "img_id">
Title: <input type = "text" name = "img_title">
Link: <input type = "text" name = "img_link">
<h1></h1>
Year: <input type = "text" name = "det_year">
Type: <input type = "text" name = "det_type">
Width: <input type = "text" name = "det_width">
Height: <input type = "text" name = "det_height">
Location: <input type = "text" name = "det_loc">
Description: <input type = "text" name = "det_desc">
<h1></h1>
Artist info: Name: <input type = "text" name = "imgart_name">
Birth Year: <input type = "text" name = "imgart_birth">
Country: <input type = "text" name = "imgart_country">
Description: <input type = "text" name = "imgart_desc">
<h1></h1>
<input type = "submit" value = "Submit" />
</form>
<form action = "modify.py" method = "post">
<h3>Details of an Artist:</h3>
Artist number: <input type = "text" name = "art_id">
Name: <input type = "text" name = "art_name">
Birth Year: <input type = "text" name = "art_birth">
Country: <input type = "text" name = "art_country">
Description: <input type = "text" name = "art_desc">
<h1></h1>
<input type = "submit" value = "Submit" />
</form>
<form action = "modify.py" method = "post">
<h3>Details of a Gallery:</h3>
Gallery number: <input type = "text" name = "gallery_id">
Name: <input type = "text" name = "gallery_name">
Description: <input type = "text" name = "gallery_desc">
<h1></h1>
<input type = "submit" value = "Submit" />
</form>
<h1>Find details of an Image:</h1>
<form action = "find.py" method = "post">
Find by Type: <input type = "text" name = "det_type">
<input type = "submit" value = "Submit" />
</form>
<form action = "find.py" method = "post">
Find by range of creation year: <input type = "text" name = "det_year_1">
until <input type = "text" name = "det_year_2">
<input type = "submit" value = "Submit" />
</form>
<form action = "find.py" method = "post">
Find by artist name: <input type = "text" name = "art_name">
<input type = "submit" value = "Submit" />
</form>
<form action = "find.py" method = "post">
Find by location: <input type = "text" name = "det_loc">
<input type = "submit" value = "Submit" />
</form>
<h1>Find details of an Artist:</h1>
<form action = "find.py" method = "post">
Find by country: <input type = "text" name = "art_country">
<input type = "submit" value = "Submit" />
</form>
<form action = "find.py" method = "post">
Find by birth year: <input type = "text" name = "art_birth">
<input type = "submit" value = "Submit" />
</form>
<form action = "gallerypage.py" method = "post">
<input type = "submit" value = "Return to galleries" />
</form>
</body>
</html>
""")
