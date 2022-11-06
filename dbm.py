import pymysql as p


def connect():
    return p.connect(host="localhost",user="root",password="",database="pavan")

def connecta():
    return p.connect(host="localhost",user="root",password="",database="trial")

def insertu(t):
    con=connecta()
    cur=con.cursor()
    sql="insert into sky4 values (%s,%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()

def login_authu(e):
    con=connecta()
    cur=con.cursor()
    sql= "SELECT * FROM sky4 WHERE a_email = %s"
    cur.execute(sql,e)
    userlogu=cur.fetchall()
    con.commit()
    con.close()
    return userlogu

def showdata():
    con=connect()
    cur=con.cursor()
    sql="select * from emp"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data


def editdetails(e):
    con=connect()
    cur=con.cursor()
    sql="select * from emp where email=%s"
    cur.execute(sql,e)
    userdetails=cur.fetchall()
    con.commit()
    con.close()
    return userdetails


def update(t):
    con=connect()
    cur=con.cursor()
    sql="update emp set name=%s,city=%s,email=%s,pasword=%s where email=%s"
    cur.execute(sql,t)
    con.commit()
    con.close()


def drop(e):
    con=connect()
    cur=con.cursor()
    sql="delete from emp where email=%s"
    cur.execute(sql,e)
    con.commit()
    con.close()
    

def login_auth(e):
    con=connect()
    cur=con.cursor()
    sql= "SELECT * FROM emp WHERE email = %s"
    cur.execute(sql,e)
    userlog=cur.fetchall()
    con.commit()
    con.close()
    return userlog



def inserta(t):
    con=connecta()
    cur=con.cursor()
    sql="insert into sky1 values (%s,%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()


def login_autha(e):
    con=connecta()
    cur=con.cursor()
    sql= "SELECT * FROM sky1 WHERE a_email = %s"
    cur.execute(sql,e)
    userloga=cur.fetchall()
    con.commit()
    con.close()
    return userloga

def insert_blog(t):
    con=connecta()
    cur=con.cursor()
    sql="insert into sky3 values (%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()

def showpost():
    con=connecta()
    cur=con.cursor()
    sql="select * from sky3"
    cur.execute(sql)
    datapost=cur.fetchall()
    con.commit()
    con.close()
    print(datapost)
    return datapost