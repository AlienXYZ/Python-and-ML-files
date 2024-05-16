#CSV files content uploaded separately
#Through this code, user can book his appointment for Covid Vaccination for the same day,next day or next to next day. The code maintains a record of no. of slots
#left for each day and specific age group. Logging in requires Aadhar no. and password authentication.

from csv import writer
from csv import reader
import os
def vaccinedate(u,n,r,o,p,q):
    while l==u:
        print("\nAge Groups\nA.15-17 years\nB.18-45 years\nC.45-60 years\nD.60+ years\nEnter letter corresponding to appropriate age group (or type E to exit) : ",end="")     
        e=input().upper()
        if e=="E":
            m=1
            return m
        def agegroup(v,t):
            d1=0
            while e==v:
                if d1==0:
                    s=open(t,'r')
                    dt=reader(s)
                    data=list(dt)
                    s.close()
                    print('\n')
                    for i in range(len(data)):
                        print()
                        for j in range(len(data[i])):
                            print(data[i][j],end='\t')
                        print()
                print("\nChoose hospital for vaccination by entering the corresponding SN (or type E to exit) : ",end="")
                f=input().upper()
                if f=="E":
                    m=1
                    return m
                w=0
                for i in data[1::]:
                    if i[0]==f:
                        a=int(i[5])
                        if a<1:
                            print("No slots available for this hospital\nPlease choose different hospital")
                            w=1
                            break
                        g=1
                        break
                    g=0
                if w==1:
                    d1=1
                    continue
                if g==0:
                    print("Incorrect input\n")
                    d1=1
                    continue
                if g==1:
                    print("\nConfirm selection by entering the corresponding SN (or type E to exit) : ",end="")
                    k=input().upper()
                    if k=="E":
                        d1=1
                        continue
                    if k==f:
                        print("Booking slot...")
                        a-=1
                        i[5]=str(a)
                        s=open('temp.csv','a',newline='\n')
                        dt=writer(s)
                        for j in range(10):
                            dt.writerow([data[j][0],data[j][1],data[j][2],data[j][3],data[j][4],data[j][5]])
                        s.close()
                        os.remove(t)
                        os.rename('temp.csv',t)
                        print("\nCongratulations, you have booked a slot for your COVID-19 vaccination in",i[1]+r+".\nPlease wait for some time to receive information about the timing from the hospital.",end="")
                        print("\nThank You")
                        h=0
                        print("\n\nLogging out...")
                        return h
                    else:
                        print("Input mismatch")
                        d1=1
        if e=="A":
            ageA=agegroup("A",n)
            return(ageA)
        elif e=="B":
            ageB=agegroup("B",o)
            return(ageB)
        elif e=="C":
            ageC=agegroup("C",p)
            return(ageC)
        elif e=="D":
            ageD=agegroup("D",q)
            return(ageD)
        else:
            print("Incorrect input")

progress=0


while True:

    b1=0
    c1=0
    h=1
    m=2
    print("\n\n\n")
    print('''
     ╔═╗      ╔══╗ ╔══════╗ ╔═╗      ╔═════╗   ╔════╗  ╔══╗   ╔══╗ ╔══════╗
     ║ ║  ╔═╗ ║  ║ ║ ╔════╝ ║ ║      ║ ╔══╗╚╗ ╔╝╔══╗╚╗ ║  ╚╗ ╔╝  ║ ║ ╔════╝
     ╚╗╚╗╔╝ ╚╗║ ╔╝ ║ ╚══╗   ║ ║      ║ ║  ╚═╝ ║ ║  ║ ║ ║ ╔╗╚═╝╔╗ ║ ║ ╚══╗  
      ║ ╚╝╔═╗╚╝ ║  ║ ╔══╝   ║ ║      ║ ║  ╔═╗ ║ ║  ║ ║ ║ ║╚╗ ╔╝║ ║ ║ ╔══╝  
      ╚╗ ╔╝ ╚╗ ╔╝  ║ ╚════╗ ║ ╚════╗ ╚╗╚══╝╔╝ ╚╗╚══╝╔╝ ║ ║ ╚═╝ ║ ║ ║ ╚════╗
       ╚═╝   ╚═╝   ╚══════╝ ╚══════╝  ╚════╝   ╚════╝  ╚═╝     ╚═╝ ╚══════╝
    ''')
    print("\n\nYou can book your vaccination slots here (this webpage is for hospitals located in pincode 500061)")

    if progress==0:
        print("\n\n\n\n\n\nDo you already have an account- Y/N ? ",end="")
        a=input().upper()
        while progress==0:
            if a=="Y":
                progress=1
            elif a=="N":
                progress=0.1
            else:
                print("Please enter Y for Yes and N for No: ",end="")
                a=input().upper()

    if progress==0.1:
        print("\n\n\nEnter details to create account")
        print("\nPlease enter your 12-digit Aadhar Card Number (or type E to exit): ",end="")
        a=input().upper()
        if a=="E":
            progress=0
            continue
        while len(a)!=12 or a.isdigit()==False:
            print("Invalid Number")
            print("Please enter your 12-digit Aadhar Card Number (or type E to exit): ",end="")
            a=input().upper()
            if a=="E":
                progress=0
                break
        if progress==0:
            continue
        s=open('locker.csv','r')
        dt=reader(s)
        data=list(dt)
        s.close()
        for i in data:
            if i[0]==a:
                print("Account for this Aadhar Card Number already exists.\nType E to exit or type N to set new password for this account: ",end="")
                b=input().upper()
                if b=="N":
                    data.remove(i)
                    s=open('temp.csv','a',newline='\n')
                    dt=writer(s)
                    for j in range(len(data)):
                        dt.writerow([data[j][0],data[j][1]])
                    s.close()
                    os.remove('locker.csv')
                    os.rename('temp.csv','locker.csv')
                    b1=1
                    break
                else:
                    progress=0
                    break
        if progress==0:
            continue
        print("Create password (or type E to exit): ",end="")
        b=input()
        if b=="E" or b=="e":
            progress=0
            continue
        while len(b)<8:
            print("Weak Password")
            print("Password should contain at least 8 characters")
            print("Create Password (or type E to exit): ",end="")
            b=input()
            if b=="E" or b=="e":
                progress=0
                break
        if progress==0:
            continue
        s=open('locker.csv','a',newline='\n')
        dt=writer(s)
        dt.writerow([a,b])
        s.close()
        progress=1
        if b1==1:
            print("New password set.")
        print("\n\n\nConfirm details to login")

    if progress==1:
        print("\n\n\nEnter Aadhar Card Number (or type E to exit): ",end="")
        c=input().upper()
        if c=="E":
            progress=0
            continue
        print("Enter Password (or type R to reset password or type E to exit): ",end="")
        d=input()
        if d=="E" or d=="e":
            progress=0
            continue
        elif d=="R" or d=="r":
            s=open('locker.csv','r')
            dt=reader(s)
            data=list(dt)
            s.close()
            for i in data:
                if i[0]==c:
                    print("Create new password (or type E to exit): ",end="")
                    d=input()
                    if d=="E" or d=="e":
                        progress=0
                        c1=2
                        break
                    while len(d)<8:
                        print("Weak Password")
                        print("Password should contain at least 8 characters")
                        print("Create Password (or type E to exit): ",end="")
                        d=input()
                        if d=="E" or d=="e":
                            progress=0
                            c1=2
                            break
                    if progress==0:
                        break
                    c1=1
            if c1==0:
                print("Account for this Aadhar Card Number does not exist.\nPlease create a new account.")
                progress=0
                continue
            if progress==0:
                continue
            data.remove(i)
            s=open('temp.csv','a',newline='\n')
            dt=writer(s)
            for j in range(len(data)):
                dt.writerow([data[j][0],data[j][1]])
            dt.writerow([c,d])
            s.close()
            os.remove('locker.csv')
            os.rename('temp.csv','locker.csv')
            print("Password has been reset.\nPlease login again.")
            progress=0
            continue
        s=open('locker.csv','r')
        dt=reader(s)
        data=list(dt)
        s.close()
        if [c,d] in data:
            print("\nSuccessful Login")
            progress=2
        else:  
            while [c,d] not in data:
                print("Incorrect Aadhar Card Number and Password combination.\nPlease try again.")
                print("\n\n\nEnter Aadhar Card Number (or type E to exit): ",end="")
                c=input().upper()
                if c=="E":
                    progress=0
                    break
                print("Enter Password (or type E to exit): ",end="")
                d=input()
                if d=="E" or d=="e":
                    progress=0
                    break
            if progress==0:
                continue
            print("\nSuccessful Login")
            progress=2

    while progress==2:
        print("\n\n\nYou can now check vaccine slots available in different hospitals by entering preferred day of vaccination and your age group.")
        print("\nDates of vaccination:\n1.Today\n2.Tomorrow\n3.Day after tomorrow")
        print("Choose day by entering corresponding number (or type E to log out): ",end="")
        l=input().upper()
        if l=="E":
            print("\n\nLogging out...")
            progress=0
            e="E"
            break
        while l!="1" and l!="2" and l!="3":
            print("Type 1 or 2 or 3 to choose 'Today' or 'Tomorrow' or 'Day after tomorrow' respectively (or type E to log out): ",end="")
            l=input().upper()
            if l=="E":
                print("\n\nLogging out...")
                progress=0
                e="E"
                break
        x=vaccinedate("1",'n1.csv',"scheduled today",'o1.csv','p1.csv','q1.csv')
        y=vaccinedate("2",'n2.csv',"scheduled tomorrow",'o2.csv','p2.csv','q2.csv')
        z=vaccinedate("3",'n3.csv',"scheduled day after tomorrow",'o3.csv','p3.csv','q3.csv')
        if x==0 or y==0 or z==0:
            e="E"
            progress=0
            break
        if x==1 or y==1 or z==1:
            continue
    if e=="E":
        print("\nSucessful log out")
        continue
