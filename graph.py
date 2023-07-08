import  mysql.connector as sql
import matplotlib.pyplot as plt
import numpy as np
def graphical():
        mydb=sql.connect(host='localhost',user='root',passwd='1234',database='bankstar')
        mycursor=mydb.cursor()
        mycursor.execute("select count(*)from account where city='kolkata'")
        x=mycursor.fetchone()
        s1=list(x)
        mycursor.execute("select count(*)from account where City='mumbai'")     
        y=mycursor.fetchone()
        s2=list(y)
        s=s1+s2
        z=['kolkata','mumbai']
        plt.bar(y,s,width=0.3)
        plt.xlabel("city")
        plt.ylabel("no of city")
        plt.show()
