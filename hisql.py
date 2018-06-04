import hashlib
import sys


from function_f import pass_ck, commend

username=''



if __name__ == '__main__':
    s_arg=sys.argv[1:]
    username=s_arg[1]
    password=hashlib.md5(str(s_arg[3]).encode()).hexdigest()
    pass_ck(username,password)
    if(len(s_arg)==4):
        while True:
            print("HideSql [("+username+")] > ",end='')
            comm=input()
            commend(comm,username)
    else:
        print("Error :\n\tCommend : python Hsql -u <username> -p <password>")
        print("\t   -u commend to user name <username> \n\t   -p commend of a password of hsql <password>")

