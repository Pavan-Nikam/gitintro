from flask import *
from dbm import *

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def reg():
    return render_template("register.html")

@app.route("/loginuser")
def loginuser():
    return render_template("userlogin.html")

@app.route("/authoruser")
def authoruser():
    return render_template("authorlogin.html")

@app.route("/authorregister")
def authorregister():
    return render_template("authorregister.html")

@app.route("/userregister")
def userregister():
    return render_template("userregister.html")

@app.route("/authoradmin")
def authoradmin():
    return render_template("authoradmin.html")

@app.route("/addpost")
def addpost():
    return render_template("add.html")


@app.route("/details")
def details():
    d=showdata()
    return render_template("details.html",ulist=d)

@app.route("/insertdata_user",methods=["post"])
def insertdata_user():
    name=request.form["username"]
    city=request.form["usercity"]
    email=request.form["useremail"]
    password=request.form["userpassword"]
    t=(id,name,city,email,password)
    insertu(t)
    return render_template("userlogin.html")




#@app.route("/updatedata",methods=["post"])
#def updatedate():
 #   name=request.form["username"]
  #  city=request.form["usercity"]
   # email=request.form["useremail"]
    #password=request.form["userpassword"]
   # t=(name,city,email,password,email)
   # update(t)
    #return redirect("/details")

#@app.route("/delete")
#def delete():
#    email=request.args.get("email")
#   drop(email)
#    return redirect("/details")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login_validation_user",methods=["POST"])
def login_validation_user():
    email=request.form["useremail"]
    password=request.form["userpassword"]
    dataa=(email,password)
    data1=login_authu(email)
    if dataa in data1:
        return redirect("/viewpost_user")
    else:
        return render_template("userregister.html")
    

@app.route("/insertdata_author",methods=["post"])
def insertdata_author():
    name=request.form["username"]
    city=request.form["usercity"]
    email=request.form["useremail"]
    password=request.form["userpassword"]
    t=(id,name,city,email,password)
    inserta(t)
    return render_template("authorlogin.html")

@app.route("/login_validation_author",methods=["POST"])
def login_validation_author():
    email=request.form["useremail"]
    password=request.form["userpassword"]
    dataa=(email,password)
    data1=login_autha(email)
    if dataa in data1:
        return render_template("authoradmin.html")
    else:
        return render_template("userregister.html")

@app.route("/insertblog",methods=["post"])
def insertblog():
    aname=request.form["authorname"]
    title=request.form["blogtitle"]
    msg=request.form["blogmsg"]
    t=(aname,title,msg)
    insert_blog(t)
    return redirect("/viewpost")

@app.route("/viewpost")
def viewpost():
    da=showpost()
    return render_template("viewpost.html",ulist=da)

@app.route("/viewpost1")
def viewpost1():
    da=showpost1()
    return render_template("edit1.html",ulist=da)

@app.route("/viewpost_user")
def viewpost_user():
    da=showpost()
    return render_template("viewpost_user.html",ulist=da)

@app.route("/bdelete")
def bdelete():
    name = request.args.get('Title')
    bdrop(name)
    return redirect("/viewpost")

@app.route("/bedit")
def bedit():
    name=request.args.get("Title")
    data = beditdetails(name)
    print(data)
    return render_template("edit3.html",t=data[0])

@app.route('/bupdatedata',methods=['post'])
def bupdatedata():
    name = request.form['Name']
    title = request.form['Title']
    blog = request.form['Description']
    print(name)
    t=(name,title,blog,title)
    print(t)
    bupdate(t)
    return redirect('/viewpost')



if __name__=='__main__':
    app.run(debug=True)



