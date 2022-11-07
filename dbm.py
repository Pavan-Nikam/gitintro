import pymysql as p


def connecta():
    return p.connect(host="localhost",user="root",password="",database="bloggers")

def insertu(t):
    con=connecta()
    cur=con.cursor()
    sql="insert into userdb values (%s,%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()

def login_authu(e):
    con=connecta()
    cur=con.cursor()
    sql= "select u_email,u_password from userdb where u_email=%s"
    cur.execute(sql,e)
    userlogu=cur.fetchall()
    con.commit()
    con.close()
    return userlogu

def inserta(t):
    con=connecta()
    cur=con.cursor()
    sql="insert into authordb values (%s,%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()


def login_autha(e):
    con=connecta()
    cur=con.cursor()
    sql= "select a_email,a_password from authordb where a_email=%s"
    cur.execute(sql,e)
    userloga=cur.fetchall()
    con.commit()
    con.close()
    return userloga

def insert_blog(t):
    con=connecta()
    cur=con.cursor()
    sql="insert into blogdb values (%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()

def showpost():
    con=connecta()
    cur=con.cursor()
    sql="select * from blogdb"
    cur.execute(sql)
    datapost=cur.fetchall()
    con.commit()
    con.close()
    return datapost

def showpost1():
    con=connecta()
    cur=con.cursor()
    sql="select * from blogdb"
    cur.execute(sql)
    datapost1=cur.fetchall()
    con.commit()
    con.close()
    return datapost1

def bdrop(e):
    con=connecta()
    cur = con.cursor()
    sql = "delete from blogdb where p_title=%s"
    cur.execute(sql,e)
    con.commit()
    con.close()

def bupdate(t):
    con=connecta()
    cur = con.cursor()
    sql = "update blogdb set p_uname=%s,p_title=%s,p_post=%s where p_title=%s"
    cur.execute(sql,t)
    con.commit()
    con.close()
    

def beditdetails(t):
    con = connecta()
    cur = con.cursor()
    sql = "select * from blogdb where p_title=%s"
    cur.execute(sql,t)
    blogdetails = cur.fetchall()
    con.commit()
    con.close()
    return blogdetails