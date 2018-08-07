import mysql.connector as mariadb
from mysql.connector import Error
import config as cfg
import bcrypt
import datetime

query="INSERT INTO data (email,pw) VALUES (%s,%s)"
query1="SELECT pw FROM data where email=%(value)s"
query2="SELECT COUNT(*) FROM data where email=%(value)s"
query3="SELECT pass FROM admin where Name=%(value)s"
query4="SELECT * FROM data"
query5="SELECT COUNT(*) FROM admin where Name=%(value)s"
query6="INSERT INTO admin (Name,Pass) VALUES (%s,%s)"
query7="SELECT * FROM admin"
query8="INSERT INTO appointment (vehnum,vehtype,mobile,address,city,date,timeslot,email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
query9="SELECT COUNT(*) FROM appointment where vehnum=%(value)s"
query10="SELECT COUNT(*) FROM appointment where mobile=%(value)s"
query11="SELECT COUNT(*) FROM appointment where email=%(value)s"
query12="SELECT COUNT(*) FROM appointment where date=%(value1)s AND vehtype=%(value2)s AND timeslot=%(value3)s "



def register(email,pw):
    try:
        print "Connectin to mysql..."
        conn=mariadb.connect(host=cfg.mysql['host'],user=cfg.mysql['user'],password=cfg.mysql['password'],database=cfg.mysql['db'])
        if conn.is_connected():
            print "Connection established"
        else:
            print "Connection fail"
        cursor=conn.cursor()
        print pw
        hashed=bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt(14))
        
        args=(email,hashed)
        cursor.execute(query,args)
        conn.commit()
        id=cursor.lastrowid
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
        print "Connection closed"
    return id


def get_data(email,que):
    print('abc')
    pw='$2b$14$QDan8ghNWl7UaCg.2yKx6.zNKYpnxpd5hH5XRcJ7zTqoRYMrq7t72'
    try:
        print "Connectin to mysql..."
        conn=mariadb.connect(host=cfg.mysql['host'],user=cfg.mysql['user'],password=cfg.mysql['password'],database=cfg.mysql['db'])
        if conn.is_connected():
            print "Connection established"
        else:
            print "Connection fail"
        cursor=conn.cursor()
        params = {'value':email}
        cursor.execute(que,params)
        rows=cursor.fetchall();
        for row in rows:
            pw=str(row[0])
            
    except Error as error:
        print(error)
    finally:
        print('xyz')
        conn.close()
        cursor.close()
        print "Connection closed"
    return pw





def verify(email,pw):
    pwd=get_data(email,query1)
    print pw
    print pwd
    if bcrypt.checkpw(pw.encode('utf-8'), pwd):
        return True
    else:
        return False


def check_exist(value,flag):
    if(flag=='user'):
        que=query2
    elif(flag=='admin'):
        que=query5
    elif(flag=='vehnum'):
        que=query9
    elif(flag=='mobile'):
        que=query10
    elif(flag=='email'):
        que=query11


    count=0

    try:
        print "Connectin to mysql..."
        conn=mariadb.connect(host=cfg.mysql['host'],user=cfg.mysql['user'],password=cfg.mysql['password'],database=cfg.mysql['db'])
        if conn.is_connected():
            print "Connection established"
        else:
            print "Connection fail"
        cursor=conn.cursor()
        params1 = {'value':value}
        cursor.execute(que,params1)
        rows=cursor.fetchall()
        for row in rows:
            count=row[0]
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
        print "Connection closed"
    if(count>=1):
        print count
        return True
    else:
        print count
        return False

def verify_admin(name,pw):
    pwd=get_data(name,query3)
    print pw
    print pwd
    if bcrypt.checkpw(pw.encode('utf-8'), pwd):
        return True
    else:
        return False

def get_webuser():
    list_user={}
    
    try:
        print "Connectin to mysql..."
        conn=mariadb.connect(host=cfg.mysql['host'],user=cfg.mysql['user'],password=cfg.mysql['password'],database=cfg.mysql['db'])
        if conn.is_connected():
            print "Connection established"
        else:
            print "Connection fail"
        cursor=conn.cursor()
        cursor.execute(query4)
        rows=cursor.fetchall();
        for row in rows:
            list_user[str(row[0])]=str(row[1])
            
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
        print "Connection closed"
    return list_user


def register_admin(uname,pw):
    try:
        print "Connectin to mysql..."
        conn=mariadb.connect(host=cfg.mysql['host'],user=cfg.mysql['user'],password=cfg.mysql['password'],database=cfg.mysql['db'])
        if conn.is_connected():
            print "Connection established"
        else:
            print "Connection fail"
        cursor=conn.cursor()
        print pw
        hashed=bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt(14))
        
        args=(uname,hashed)
        cursor.execute(query6,args)
        conn.commit()
        
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
        print "Connection closed"

def get_systemuser():
    list_sysuser={}
    
    try:
        print "Connectin to mysql..."
        conn=mariadb.connect(host=cfg.mysql['host'],user=cfg.mysql['user'],password=cfg.mysql['password'],database=cfg.mysql['db'])
        if conn.is_connected():
            print "Connection established"
        else:
            print "Connection fail"
        cursor=conn.cursor()
        cursor.execute(query7)
        rows=cursor.fetchall();
        for row in rows:
            list_sysuser[str(row[0])]=str(row[1])
            
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
        print "Connection closed"
    return list_sysuser

def book_appointment(vehnum,vehtype,mobile,address,city,date,timeslot,email):
    try:
        print "Connectin to mysql..."
        conn=mariadb.connect(host=cfg.mysql['host'],user=cfg.mysql['user'],password=cfg.mysql['password'],database=cfg.mysql['db'])
        if conn.is_connected():
            print "Connection established"
        else:
            print "Connection fail"
        cursor=conn.cursor()
        args=(vehnum,vehtype,mobile,address,city,date,timeslot,email)
        cursor.execute(query8,args)
        conn.commit()
        id=cursor.lastrowid
        print id
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
        print "Connection closed"
    return id


def count_timeslot(date,vehtyp):
    time_slot=['9-11','11-1','2-4','4-6']
    count={}
    mdate=datetime.datetime.strptime(date,'%m/%d/%Y')
    ndate=datetime.date.strftime(mdate,'%Y/%m/%d')
    try:
        print "Connectin to mysql..."
        conn=mariadb.connect(host=cfg.mysql['host'],user=cfg.mysql['user'],password=cfg.mysql['password'],database=cfg.mysql['db'])
        if conn.is_connected():
            print "Connection established"
        else:
            print "Connection fail"
        cursor=conn.cursor()
        for time in time_slot:
            params1 = {'value1':ndate,'value2':vehtyp,'value3':time}
            cursor.execute(query12,params1)
            rows=cursor.fetchall()
            for row in rows:
                count[time]=row[0]
        
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
        print "Connection closed"
    return count

def available_timeslot(date,vehtyp):
    time_slots_2=[]
    time_slots_4=[]


    if(vehtyp=='Two Wheeler'):
        for key,value in count_timeslot(date,vehtyp).items():
            if(value<1):
                time_slots_2.append(key)
        
        return time_slots_2

    if(vehtyp=='Four Wheeler'):
        for key,value in count_timeslot(date,vehtyp).items():
            if(value<1):
                time_slots_4.append(key)
        
        return time_slots_4


    



    

    





    



