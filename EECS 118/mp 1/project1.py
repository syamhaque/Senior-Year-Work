#EECS 118 mp1
#Mohammed Haque
#62655407
#10/8/19
import pymysql

db = pymysql.connect(host='localhost',
user='root',
passwd='xxxxxx',
db= 'project1')
# initialize variables
result = 0
myname = ('HAQUE, MOHAMMED SYAMUL JR.',)
id2d = 7
file = open("output.txt","w")
cur = db.cursor()

# Question 1
sql="SELECT * FROM question"
cur.execute(sql)
file.write("question:\n")
for row in cur.fetchall(): # cur.fetchone() gets one result at a time
    file.write("{}, {}, {}\n".format(row[0],row[1],row[2]))
        
# Question 2
sql="""SELECT A,B FROM question WHERE name = '%s'"""%(myname)
cur.execute(sql)
for row in cur.fetchall():
    result = row[0]*row[1]+id2d
# result should be 94821082

# Question 3
sql = """INSERT IGNORE INTO result(name, id2d, result) VALUES(%s, %s, %s)"""
val = (myname, id2d, result)
cur.execute(sql,val)
db.commit()
file.write("\n")

sql = "SELECT * FROM result"
cur.execute(sql)
file.write("result:\n")
for row in cur.fetchall():
    if row[0] == myname[0]:
        file.write("{}, {}".format(row[0],row[2]))

file.close()
db.close()
