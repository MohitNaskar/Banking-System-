import account
import transaction
import clr
import manipulation
import os
import graph
def cls():
        print("\n"*80)
def mainmenu():
        while True:
                cls()
                print("*"*80)
                print("\t\t\t\tMAIN MENU")
                print("1. NEW CUSTOMER")
                print("2. TRANSACTION OF CUSTOMER ")
                print("3. PASSBOOK PRINT")
                print("4. GRAPHICAL PRESENTATION")
                print("5. Exit")
                print("*"*80)
                ch=int(input("enter your choice"))
                if(ch==1):
                        account.customerdetails()
                        input()
                elif(ch==2):
                        transaction.inserttransaction()
                        input()      
                elif(ch==3):
                        manipulation.printpassbook()
                elif(ch==4):
                        graph.graphical()
                elif(ch==5):
                        break
                else:
                        print("wrong choice/Try again")
                        ans=input("want to continue")

              
