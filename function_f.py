import hashlib
import sys
import sqlite3
from data import password_h
from encrp_f import decrypt, encrypt
from help_c import wel, syn_create

#variable
username=''
Commend=''
conn=object
ck=0



#default username = 'hdbuser' password = 'hdb'
def pass_ck(username,password):
    if(username=="hdbuser" and password==password_h):
        print(wel)
    else:
        print("Error:\tUsername and password incorret")
        sys.exit()

#exit function
def exit():
    global username,conn
    if (Commend == "exit" or Commend == "bye"):
        conn.close()
        sys.exit("Good bye Have a nice day " + username)

    return 0


def init_db():
    global conn,username
    conn=sqlite3.connect('DB_file/'+str(username)+'.db')
    conn.execute('create table if not exists isPassword(table_n text,password text)')
    conn.commit()


#function built
def end(ck):
    if(ck==0):
        print("Commend is Not found. Type 'help;' or '\h' for help.")


def create_sql_f(comm):
    global conn
    com_t = comm.split(",")
    com_t = [x for x in com_t if x != '']

    ck=0
    key=''
    for val in com_t:
        com_tt = val.split(":")
        com_tt = [x for x in com_tt if x != '']
        if (len(com_t) > 1 and com_tt[0]=='key'):
            ck=1
            key=com_t[1]
    cnd = 'create table '+com_t[0]+'('
    if(ck==1):
        com_t.remove('key:'+key)
        cursor=conn.execute("select * from isPassword where table_n='"+com_t[0]+"'")
        cursor_ck=0
        for c in cursor:
            cursor_ck+=1
        cursor=conn.execute("select name from sqlite_master where name='"+com_t[0]+"'")
        for c in cursor:
            cursor_ck+=1
        if(cursor_ck==0):
            conn.execute("insert into isPassword values ('"+com_t[0]+"','"+hashlib.md5(str(key).encode()).hexdigest()+"')")
    for val in com_t[1:]:
        cnd=cnd+''+val+' TEXT,'
    cnd =cnd+' isPassword TEXT)'
    try:
        conn.execute(cnd)
        conn.commit()
    except Exception as ex:
        print("Error in code "+(ex).__class__.__name__+" "+str(ex.args)+syn_create)
        return 0

    print("Success create table "+com_t[0])


def create_f(param):
    com_t = param.split(")")
    com_t=[x for x in com_t if x!='']

    if (len(com_t) == 1):
        comm = com_t[0]
        create_sql_f(comm)

    else:
        print("systax Error : "+syn_create)


def insert_sql_f(comm):
    global conn
    com_t = comm.split(",")
    com_t = [x for x in com_t if x != '']

    ck=0
    key=''
    for val in com_t:
        com_tt = val.split(":")
        com_tt = [x for x in com_tt if x != '']
        if (len(com_t) > 1 and com_tt[0]=='key'):
            ck=1
            key=com_t[1]
    cnd = 'insert into '+com_t[0]+' vlaues('
    if(ck==1):
        com_t.remove('key:'+key)
        cursor_ck=0
        for val in com_t[1:]:
            cnd = cnd + "'" + decrypt(key,val) + "',"
        cnd = cnd + "'" + decrypt(key,'true_key') + "')"
    else:

        for val in com_t[1:]:
            cnd = cnd + "'" + decrypt(username,val) + "',"
        cnd = cnd + "'no')"
    try:
        conn.execute(cnd)
        conn.commit()
    except Exception as ex:
        print("Error in code "+(ex).__class__.__name__+" "+str(ex.args)+syn_create)
        return 0

    print("Success value insert on table "+com_t[0])


def insert_f(param):
    com_t = param.split(")")
    com_t=[x for x in com_t if x!='']

    if (len(com_t) == 1):
        comm = com_t[0]
        insert_sql_f(comm)

    else:
        print("systax Error : "+syn_create)




def comd_f():
    global username,Commend,ck
    com_t=Commend.split("(")
    if(len(com_t)==2):
        comm=com_t[0]
        if(comm=="create"):
            create_f(com_t[1])
        elif(comm=="insert"):
            insert_f(com_t[1])
        ck=1



def commend(comm,user):
    global username,Commend
    username=user
    Commend=comm
    init_db()
    exit()
    #function start
    comd_f()

    #function end
    end(ck)




