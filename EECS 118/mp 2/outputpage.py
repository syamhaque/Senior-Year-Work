#EECS118 mp2
#Mohammed Haque
#62655407
#10/21/19
# THIS IS THE PAGE THAT OUTPUTS THE IMAGES #
import cgi

form = cgi.FieldStorage()
pic1_title = form.getvalue('pic1_title')
pic1_url = form.getvalue('pic1_url')
pic1_year  = form.getvalue('pic1_year')
pic1_artist = form.getvalue('pic1_artist')
pic1_desc = form.getvalue('pic1_desc')

pic2_title = form.getvalue('pic2_title')
pic2_url = form.getvalue('pic2_url')
pic2_year  = form.getvalue('pic2_year')
pic2_artist = form.getvalue('pic2_artist')
pic2_desc = form.getvalue('pic2_desc')

print("""Content-Type:text/html\r\n\r\n
<html>
<body>""")

print("""<script>
function FirstImage(){
document.getElementById("pic1_title").innerHTML = "%s";
document.getElementById("pic1_url").src = "%s";
document.getElementById("pic1_year").innerHTML = "%s";
document.getElementById("pic1_artist").innerHTML = "%s";
document.getElementById("pic1_desc").innerHTML = "%s";
}
function SecondImage(){
document.getElementById("pic1_title").innerHTML = "%s";
document.getElementById("pic1_url").src = "%s";
document.getElementById("pic1_year").innerHTML = "%s";
document.getElementById("pic1_artist").innerHTML = "%s";
document.getElementById("pic1_desc").innerHTML = "%s";
}
</script>""" % (pic1_title, pic1_url, pic1_year, pic1_artist, pic1_desc,
                pic2_title, pic2_url, pic2_year, pic2_artist, pic2_desc))
print("""<h1 id="pic1_title">{}</h1>
<img src = {} id = "pic1_url">
<p id="pic1_year">{}</p>
<p id="pic1_artist">{}</p>
<p id="pic1_desc">{}</p>
""".format(pic1_title, pic1_url, pic1_year, pic1_artist, pic1_desc))
print("""<button type="button" onclick='FirstImage()'>First Image</button>""")
print("""<button type="button" onclick='SecondImage()'>Second Image</button>""")
print("""<form action = "inputpage.py" method = "get">
<input type = "submit" value = "Reset" />
</body>
</html>
""")

