#EECS118 mp2
#Mohammed Haque
#62655407
#10/21/19
# THIS IS THE PAGE TO INPUT INFORMATION #

print ("""Content-Type:text/html\r\n\r\n
<html>
<head>
<title>Mini Project 2</title>
</head>
<body>
<h1>Mini Project 2 by Mohammed Haque (62655407)</h1>
</body>
</html>
<html>
<body>
<h3>Image 1:</h3>
<form action = "outputpage.py" method = "get">
URL: <input type = "text" name = "pic1_url">
<h1></h1>
Title: <input type = "text" name = "pic1_title">
<h1></h1>
Year: <input type = "text" name = "pic1_year">
<h1></h1>
Artist: <input type = "text" name = "pic1_artist">
<h1></h1>
Brief Description: <input type = "text" name = "pic1_desc">
<h3>Image 2:</h3>
URL: <input type = "text" name = "pic2_url">
<h1></h1>
Title: <input type = "text" name = "pic2_title">
<h1></h1>
Year: <input type = "text" name = "pic2_year">
<h1></h1>
Artist: <input type = "text" name = "pic2_artist">
<h1></h1>
Brief Description: <input type = "text" name = "pic2_desc">
<h1></h1>
<input type = "submit" value = "Submit" />
</form>
</body>
</html>""")

