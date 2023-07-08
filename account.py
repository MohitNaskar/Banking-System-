import mysql.connector as co  #  library or module
def customerdetails():
        while True:
                # os.system("cls")
                print("*"*80)
                print("\t\t\t\t*******CUSTOMER DETAILS***********")
                print("1. CREATE NEW CUSTOMER ACCOUNT")
                print("2. DISPLAY CUSTOMER RECORD")
                print("3. SEARCH CUSTOMER RECORD")
                print("4. DELETE CUSTOMER RECORD")
                print("5.Exit")
                print("*"*80)
                ch=int(input("enter your choice"))
                if(ch==1):
                        createcustomer()
                elif(ch==2):
                        displaycustomer()
                elif(ch==3):
                        searchcustomer()
                elif(ch==4):
                        deletecustomer()
                elif(ch==5):
                        break
                else:
                        print("wrong choice")
                        print("want to continue")
def createcustomer():
        while True:
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='bankstar')
                mycursor=mydb.cursor()
                acct_no=int(input("enter Account No"))
                Name=input("enter the Name of Customer")
                Mobile=input("enter mobile no")
                email=input("enter email")
                Address=input("enter address")
                City=input("enter city")
                Country=input("enter Country")
                mycursor.execute("insert into account values('"+str(acct_no)+"','"+Name+"','"+Mobile+"','"+email+"','"+Address+"','"+City+"','"+Country+"')")
                mydb.commit()
                ch=input("want to enter another records")
                if(ch=="N"):
                        break
                mydb.close()
def displaycustomer():
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='bankstar')
                mycursor=mydb.cursor()
                mycursor.execute("select * from account")
                print("#"*75)
                print("Accno\tName\t\Mobile\tE-Mail\tAddress\tCity\tCountry")
                for x in mycursor:
                        print (x)
                print("#"*75)
def searchcustomer():
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='bankstar')
                mycursor=mydb.cursor()
                acct_no=int(input("enter account no"))
                mycursor.execute("select * from account where acct_no='"+str(acct_no)+"'")
                print("#"*75)
                print("Accno\tName\t\Mobile\tE-Mail\tAddress\tCity\tCountry")
                for x in mycursor:
                        print (x)
                print("#"*75)
def deletecustomer():
                mydb=co.connect(host='localhost',user='root',passwd='1234',database='bankstar')
                mycursor=mydb.cursor()
                acct_no=int(input("enter Account No"))
                mycursor.execute("delete from account where acct_no='"+str(acct_no)+"'")
                mydb.commit()
                print("*"*75)

        

        
                
                
                
