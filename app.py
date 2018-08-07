from flask import Flask, flash, redirect, render_template,request, url_for, session,jsonify
import Dbfun
import os
import datetime

app=Flask(__name__)
app.secret_key=os.urandom(24)



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/loginform')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/Reg_vehicle')
def vehicle():
    return render_template('vehicle.html')

@app.route('/dashboard')
def dash():
    return render_template('Dashboard.html')




@app.route('/process',methods=['POST'])
def get_d():
    mail=request.form['email']
    pw=request.form['pass']
    if(Dbfun.check_exist(mail,'user')):
        return render_template('signup.html',msg1="*Email You Entered is already Registered")
    else:
        Dbfun.register(mail,pw)
        
        return render_template('login.html',msg2="You can now Login")
    

    

@app.route('/login',methods=['POST'])
def get_l():
    mail=request.form['email']
    pw=request.form['pw']
    if(Dbfun.verify(mail,pw)):
        session['user']=mail
        return render_template('Dashboard.html',msg3="Logged in "+session['user'])
    else:
        return render_template('login.html',msg4="*Invalid Email Or Password")
    

    

@app.route('/logout')
def get_logout():
    session.pop('user',None)
    return render_template('home.html',msg="Logged Out")

@app.route('/users')
def users():
    return render_template('adminlogin.html')

@app.route('/registeradmin')
def register_admin():
    return render_template('registeradmin.html')

@app.route('/registeradmindetail',methods=['POST'])
def get_admin():
    print('admin registering')
    uname=request.form['username']
    pw=request.form['pwd']
    if(Dbfun.check_exist(uname,'admin')):
        return render_template('registeradmin.html',message="*Admin You Entered is already Registered")
    else:
        Dbfun.register_admin(uname,pw)
        
        return render_template('adminlogin.html',msg="*You can now use new admin credential")

@app.route('/loginadmin',methods=['POST'])
def verify_admin():
    user=request.form['username']
    pw=request.form['pwd']
    if(Dbfun.verify_admin(user,pw)):
        session['user']=user
        return render_template('admindash.html',message="You are Logged in "+session['user'],list1=Dbfun.get_webuser().items(),list2=Dbfun.get_systemuser().items())
    else:
        return render_template('adminlogin.html',msg1="*Invalid Username Or Password")

@app.route('/bookapt',methods=['POST'])
def book_appointment():
    veh_num=request.form['vhnum']

    veh_typ=request.form['opt']
    mobile=request.form['mob']
    address=request.form['add']
    city=request.form['city']
    date=request.form['date']
    mdate=datetime.datetime.strptime(date,'%m/%d/%Y')
    ndate=datetime.date.strftime(mdate,'%Y/%m/%d')
    time_slot=request.form['sel_apt']
    email=session['user']

    
    if(Dbfun.check_exist(email,'email')):
        return render_template('Dashboard.html',message="*As per New Rules\n1)You can Use One vehicle per Person\n2)You can Register One vehicle with One Email\n3)Instruction:Logout and Register with new Email")
    elif(Dbfun.check_exist(mobile,'mobile')):
        return render_template('vehicle.html',message="*Sorry You Can Register One Vehicle with One Mobile Number")
    elif(Dbfun.check_exist(veh_num,'vehnum')):
        return render_template('vehicle.html',message="*This Vehicle is Already registered")
    else:
        id=Dbfun.book_appointment(veh_num,veh_typ,mobile,address,city,ndate,time_slot,email)
        if id=='':
            return render_template('login.html',msg="Problem occured during Registration.Please Login again.")
        else:
            return render_template('Dashboard.html',msg1="Your Appointment Id is "+str(id))


@app.route('/ajaxcall',methods=['POST'])
def ajaxcall():
    list1=[]
    
    veh_typ=request.form['veh_typ']
    date=request.form['date']
    
    
    list1=Dbfun.available_timeslot(date,veh_typ)
    print list1
    print veh_typ
    print date
    return jsonify({'list':list1})



    

    
    
    
    












if __name__=='__main__':
    app.run(debug=True)