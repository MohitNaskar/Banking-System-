import mysql.connector as co
def printpassbook():
        while True:
                # os.system("cls")
                print("*"*80)
                print("\t\t\t\t*******PASSBOOK PRINT***********")
                print("1. PASSBOOK PRINT")
                print("2.Exit")
                print("*"*80)
                ch=int(input("enter your choice"))
                if(ch==1):
                        passbook()
                
def passbook():
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='bankstar')
                mycursor=mydb.cursor()
                acct_no=int(input("enter Account No"))
                mycursor.execute("SELECT account.Name,transactions.balance from account INNER JOIN transactions ON account.acct_no = transactions.acct_no and account.acct_no='"+str(acct_no)+"'")
                for x in mycursor:
                        print(x)
                mydb.close()


        
                
                
                
