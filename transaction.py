import mysql.connector as co

def inserttransaction():
        while True:
                # os.system("cls")
                print("*"*80)
                print("\t\t\t\t*******TRANSACTION DETAILS***********")
                print("1. INSERT NEW TRANSACTION FOR DEPOSIT")
                print("2. INSERT NEW TRANSACTION FOR WITHDRAWL AND UPDATE BALANCE")
                print("3. DISPLAY ALL TRANSACTION")
                print("4. DISPLAY A TRANSACTION AGAINST A ACCOUNT NUMBER")
                print("5. DELETE TRANSACTION")
                print("6.Exit")
                print("*"*80)
                ch=int(input("enter your choice"))
                if(ch==1):
                        createtransactionfordeposit()
                elif(ch==2):
                        createtransactionforwithdrawn()
                elif(ch==3):
                        displaytransaction()
                elif(ch==4):
                        searchtransaction()
                elif(ch==5):
                        deletetransaction()
                elif(ch==6):
                        break
                else:
                        print("wrong choice")
                        print("want to continue")
k=0
def createtransactionfordeposit():
        while True:
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='bankstar')
                mycursor=mydb.cursor()
                acct_no=int(input("enter Account No"))
                date=input("enter the deposit date")
                balance=int(input("enter initial balance only")) 
                amount_added=int(input("enter amount to deposit"))
                balance=balance+amount_added
                k=balance
                withdrawal_amount=0
                mycursor.execute("insert into transactions values('"+str(acct_no)+"','"+date+"','"+str(withdrawal_amount)+"','"+str(amount_added)+"','"+str(balance)+"')")
                mydb.commit()
                ch=input("want to enter another records")
                if(ch=="N"):
                        break
                mydb.close()
def createtransactionforwithdrawn():
        while True:
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='bankstar')
                mycursor=mydb.cursor()
                acct_no=int(input("enter Account No"))
                date=input("enter the deposit date")
                withdrawal_amt=int(input("enter the withdrawl amount"))
                amount_added=0
                mycursor.execute("select * from transactions")
                row=mycursor.fetchone()
                balance=row[4]
                print(balance)
                mycursor.execute("insert into transactions values('"+str(acct_no)+"','"+date+"','"+str(withdrawal_amt)+"','"+str(amount_added)+"','"+str(balance)+"')")
                mycursor.execute("update transactions SET balance=balance-'"+str(withdrawal_amt)+"' where acct_no='"+str(acct_no)+"'")
                mydb.commit()
                ch=input("want to enter another records")
                if(ch=="N"):
                        break
                mydb.close()
        
def displaytransaction():
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='bankstar')
                mycursor=mydb.cursor()
                mycursor.execute("select * from transactions")
                print("*"*60)
                print("Accno\twithdrawal amount\tamount_addedt\tBalance")
                for x in mycursor:
                        print (x)
                print("*"*60)
def searchtransaction():
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='bankstar')
                mycursor=mydb.cursor()
                acct_no=int(input("enter account no"))
                mycursor.execute("select * from transactions where acct_no='"+str(acct_no)+"'")
                print("*"*60)
                print("Accno\tdate\twithdrawal amount\tamount_addedt\tBalance")
                for x in mycursor:
                        print (x)
                print("*"*60)
def deletetransaction():
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='bankstar')
                mycursor=mydb.cursor()
                acct_no=int(input("enter Account No"))
                mycursor.execute("delete from transactions where acct_no='"+str(acct_no)+"'")
                mydb.commit()
                print("*"*60)

        
                
                
                
