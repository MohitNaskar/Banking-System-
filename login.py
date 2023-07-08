import mysql.connector as sql , random , datetime as dt
import bank
import clr
import matplotlib.pyplot as plt
conn=sql.connect(host='localhost',user='root',passwd='1234',database='bank')
print("#"*80)
print('\t\tWELCOME TO BANKING MANAGEMENT SYSTEM')
print("#"*80)
if conn.is_connected():
    print("\n\nYou have successfully connected with Bank database")
c1=conn.cursor()
def cls():
    print("\n"*80)
    

while True:
        print('\t1.ENTER LOGIN DETAILS')
        choice1=int(input('\tENTER YOUR CHOICE:'))
    
        if choice1==1:
                login=input('Enter your username:')
                paswd=input('Enter your password:')
                info2="select * from user where login='{}' and paswd='{}'".format(login,paswd)
                c1.execute(info2)
                bank.mainmenu()
                input()
                cls()
        elif choice1!=1:
                break
        else:
                print("try again")
                choice1=int(input("enter choice again"))
        
print(dt.datetime.now())


